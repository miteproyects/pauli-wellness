"""Build a self-contained static index.html from app.py.

Stubs `streamlit` and re-imports app.py 8 times (one per page×lang),
captures the rendered HTML strings, then emits site/index.html with
a tiny JS router that picks the right block based on URL params.

URL pattern is preserved verbatim:
    ?page={home|ghk|resultados|estudios}&lang={es|en}&theme={light|dark}

Run from the Pauli repo root:
    python3 build_static.py
"""
from __future__ import annotations
import importlib.util
import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
APP_PY = ROOT / "app.py"
OUT_DIR = ROOT / "site"
OUT_DIR.mkdir(exist_ok=True)
OUT_HTML = OUT_DIR / "index.html"

# ───── streamlit stub ─────────────────────────────────────────────────────────
_qp_storage: dict[str, str] = {}
_buffer: list[str] = []


class _QP:
    def get(self, k, default=None):
        return _qp_storage.get(k, default)

    def __contains__(self, k):
        return k in _qp_storage

    def __getitem__(self, k):
        return _qp_storage[k]


def _markdown(html, unsafe_allow_html=False):
    _buffer.append(str(html))


def _comp_html(html, height=0):
    _buffer.append(str(html))


# Build streamlit + streamlit.components + streamlit.components.v1 as real
# ModuleType objects so `import streamlit.components.v1 as X` works.
fake_st = types.ModuleType("streamlit")
fake_st.query_params = _QP()
fake_st.set_page_config = lambda **kw: None
fake_st.markdown = _markdown

fake_components = types.ModuleType("streamlit.components")
fake_v1 = types.ModuleType("streamlit.components.v1")
fake_v1.html = _comp_html
fake_components.v1 = fake_v1
fake_st.components = fake_components

sys.modules["streamlit"] = fake_st
sys.modules["streamlit.components"] = fake_components
sys.modules["streamlit.components.v1"] = fake_v1

# ───── render each combo ──────────────────────────────────────────────────────
spec = importlib.util.spec_from_file_location("pauli_app", APP_PY)


def render(page: str, lang: str, theme: str = "light") -> str:
    global _qp_storage, _buffer
    _qp_storage = {"page": page, "lang": lang, "theme": theme}
    _buffer = []
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return "".join(_buffer)


COMBOS = [
    ("home", "es"), ("ghk", "es"), ("resultados", "es"), ("estudios", "es"),
    ("home", "en"), ("ghk", "en"), ("resultados", "en"), ("estudios", "en"),
]

print(f"[build] rendering {len(COMBOS)} (page, lang) combos…")
renders = {f"{p}-{l}": render(p, l, "light") for (p, l) in COMBOS}

# ───── slice out the per-block fragments ──────────────────────────────────────
# Each render is:
#   <style>BASE_CSS</style>      ← shared
#   <style>LIGHT_CSS</style>     ← we toggle via .theme-dark class on <html>
#   <nav class="topnav">…</nav>  ← per page+lang
#   <div class="nav-spacer">…</div>
#   <a … class="wa-float">…</a>  ← per lang (WA text differs)
#   <script>persist…</script>    ← shared (height=0 component)
#   <section …>…content…</section>×N
#   <div class="footer">…</div>
#   <script>arrows…</script>     ← shared

_anchor_re = re.compile(r"(?s)(<style>.*?</style>)")
_nav_re = re.compile(r'(?s)<nav class="topnav">.*?</nav>\s*<div class="nav-spacer"></div>')
_wa_re = re.compile(r'(?s)<a href="https://wa\.me/[^"]+" target="_blank" rel="noopener" class="wa-float"[\s\S]*?</a>')
_script_re = re.compile(r"(?s)<script>.*?</script>")
_footer_re = re.compile(r'(?s)<div class="footer">.*?</div>\s*$', re.MULTILINE)


def split_render(html: str) -> dict[str, str]:
    styles = _anchor_re.findall(html)  # first = BASE, second = LIGHT
    base_css = styles[0] if styles else ""
    light_css = styles[1] if len(styles) > 1 else ""

    nav_match = _nav_re.search(html)
    nav = nav_match.group(0) if nav_match else ""

    wa_match = _wa_re.search(html)
    wa = wa_match.group(0) if wa_match else ""

    scripts = _script_re.findall(html)
    persist_js = scripts[0] if scripts else ""
    arrows_js = scripts[-1] if len(scripts) > 1 else ""

    footer_match = _footer_re.search(html)
    footer = footer_match.group(0) if footer_match else ""

    # Content = everything after the WA FAB and persist JS, up to (but not
    # including) the footer.
    content = html
    if wa:
        content = content.split(wa, 1)[-1]
    if persist_js:
        content = content.split(persist_js, 1)[-1]
    if footer:
        content = content.rsplit(footer, 1)[0]
    if arrows_js:
        content = content.rsplit(arrows_js, 1)[0]

    return {
        "base_css": base_css,
        "light_css": light_css,
        "nav": nav,
        "wa": wa,
        "persist_js": persist_js,
        "content": content.strip(),
        "footer": footer,
        "arrows_js": arrows_js,
    }


parts = {k: split_render(v) for k, v in renders.items()}

# Shared blocks — pull from the first render
first = parts["home-es"]
BASE_CSS = first["base_css"]
LIGHT_CSS = first["light_css"]
PERSIST_JS = first["persist_js"]
ARROWS_JS = first["arrows_js"]

# Per-lang WA buttons
WA_ES = parts["home-es"]["wa"]
WA_EN = parts["home-en"]["wa"]

# Per-lang footer
FOOTER_ES = parts["home-es"]["footer"]
FOOTER_EN = parts["home-en"]["footer"]

# Per page+lang content + nav
CONTENT_BLOCKS = {key: parts[key]["content"] for key in parts}
NAV_BLOCKS = {key: parts[key]["nav"] for key in parts}

# ───── adapt LIGHT_CSS so it activates only when <html> lacks .theme-dark ────
# Original LIGHT_CSS just redefines :root vars. We re-scope it to
# html:not(.theme-dark) :root → wait, that doesn't work. We scope it to
# html:not(.theme-dark) and override the selectors that use :root vars by
# putting LIGHT_CSS inside html:not(.theme-dark) selector wrapper, like:
#   html:not(.theme-dark){--bg:…} (no :root needed)
# So we replace `:root{` with `html:not(.theme-dark){` and prepend a
# `html.theme-dark` block with the dark defaults (which BASE_CSS already
# provides via :root). The simplest fix: keep BASE_CSS as the dark default
# via :root, and make LIGHT_CSS apply when html does NOT have .theme-dark.

LIGHT_CSS_SCOPED = LIGHT_CSS.replace(":root{", "html:not(.theme-dark){")
# Also re-scope the specific selectors that don't use :root
LIGHT_CSS_SCOPED = LIGHT_CSS_SCOPED.replace(
    ".test-arrow{",
    "html:not(.theme-dark) .test-arrow{",
).replace(
    ".study-item,.fact-card{",
    "html:not(.theme-dark) .study-item,html:not(.theme-dark) .fact-card{",
).replace(
    ".theme-tgl{",
    "html:not(.theme-dark) .theme-tgl{",
)

# ───── emit the final index.html ──────────────────────────────────────────────
META = (
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '<meta name="theme-color" content="#000000">\n'
    '<meta name="description" content="Pauli Wellness — fototerapia LifeWave X39, GHK-Cu y bienestar natural. Sin químicos, sin agujas, sin efectos secundarios conocidos.">\n'
    '<meta property="og:title" content="Luz en tu cuerpo · Pauli Wellness">\n'
    '<meta property="og:description" content="Dos décadas de ciencia. +200 patentes. Una idea simple: usar la luz para despertar la reparación celular que tu cuerpo ya sabe hacer.">\n'
    '<meta property="og:type" content="website">\n'
    '<title>Luz en tu cuerpo · Pauli Wellness</title>\n'
    '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'%3E%3Ctext y=\'26\' font-size=\'26\'%3E%E2%9C%A8%3C/text%3E%3C/svg%3E">\n'
)

# Render content blocks as <template> tags so they are NOT shown by default;
# JS clones the right one into <main> based on URL params.
template_blocks = "\n".join(
    f'<template id="page-{key}">{html}</template>'
    for key, html in CONTENT_BLOCKS.items()
)
nav_blocks = "\n".join(
    f'<template id="nav-{key}">{html}</template>'
    for key, html in NAV_BLOCKS.items()
)

# WA + footer templates (lang-scoped)
wa_templates = (
    f'<template id="wa-es">{WA_ES}</template>\n'
    f'<template id="wa-en">{WA_EN}</template>\n'
)
footer_templates = (
    f'<template id="footer-es">{FOOTER_ES}</template>\n'
    f'<template id="footer-en">{FOOTER_EN}</template>\n'
)

# Router JS — picks block by URL params, applies theme class, persists prefs
ROUTER_JS = """
<script>
(function(){
  var qp = new URLSearchParams(window.location.search);
  // page is NEVER persisted to localStorage — always default to home if absent.
  var page  = qp.get('page')  || 'home';
  // lang + theme persist across visits so user prefs stick (matches Streamlit).
  var lang  = qp.get('lang')  || localStorage.getItem('pauli-lang')  || 'es';
  var theme = qp.get('theme') || localStorage.getItem('pauli-theme') || 'light';

  if (!['home','ghk','resultados','estudios'].includes(page)) page = 'home';
  if (!['es','en'].includes(lang)) lang = 'es';
  if (!['dark','light'].includes(theme)) theme = 'light';

  // Apply theme + lang ASAP to <html> to avoid FOUC
  document.documentElement.classList.toggle('theme-dark', theme === 'dark');
  document.documentElement.lang = lang;

  // Persist lang + theme only
  try {
    localStorage.setItem('pauli-lang', lang);
    localStorage.setItem('pauli-theme', theme);
  } catch(e) {}

  // Helper: clone a <template> into a host
  function mount(templateId, hostId) {
    var tpl = document.getElementById(templateId);
    var host = document.getElementById(hostId);
    if (!tpl || !host) return;
    host.innerHTML = '';
    host.appendChild(tpl.content.cloneNode(true));
  }

  var key = page + '-' + lang;
  mount('nav-' + key, 'nav-mount');
  mount('page-' + key, 'main');
  mount('footer-' + lang, 'footer-mount');
  mount('wa-' + lang, 'wa-mount');

  // Nav templates were baked with theme=light. Post-mount, rewrite every
  // internal nav href so it preserves the CURRENT theme, and update the
  // theme-toggle icon + href so it points to the OPPOSITE of current theme.
  function fixNavLinks(){
    var otherTheme = theme === 'dark' ? 'light' : 'dark';
    var nav = document.getElementById('nav-mount');
    if (!nav) return;
    nav.querySelectorAll('a[href^="?"]').forEach(function(a){
      var u = new URL(a.getAttribute('href'), window.location.href);
      // Theme toggle: explicitly flip to other theme
      if (a.classList.contains('theme-tgl')) {
        u.searchParams.set('theme', otherTheme);
        a.setAttribute('href', '?' + u.searchParams.toString());
        a.textContent = theme === 'dark' ? '🌙' : '☀️';
        var title = theme === 'dark'
          ? (lang === 'es' ? 'Cambiar a modo claro' : 'Switch to light mode')
          : (lang === 'es' ? 'Cambiar a modo oscuro' : 'Switch to dark mode');
        a.setAttribute('title', title);
        a.setAttribute('aria-label', title);
      } else {
        // Every other nav link: preserve current theme on navigation
        u.searchParams.set('theme', theme);
        a.setAttribute('href', '?' + u.searchParams.toString());
      }
    });
  }
  fixNavLinks();

  // Update <title> for the active page+lang
  var titles = {
    'home-es':'Luz en tu cuerpo · Pauli Wellness',
    'ghk-es':'GHK-Cu · Pauli Wellness',
    'resultados-es':'Resultados · Pauli Wellness',
    'estudios-es':'Estudios y patentes · Pauli Wellness',
    'home-en':'Light in your body · Pauli Wellness',
    'ghk-en':'GHK-Cu · Pauli Wellness',
    'resultados-en':'Results · Pauli Wellness',
    'estudios-en':'Studies and patents · Pauli Wellness',
  };
  if (titles[key]) document.title = titles[key];

  // Wire carousel arrows after content is mounted
  function wireArrows(){
    var wraps = document.querySelectorAll('.test-scroll-wrap');
    wraps.forEach(function(wrap){
      if (wrap.dataset.wired) return;
      var scroll = wrap.querySelector('.test-scroll');
      var left = wrap.querySelector('.test-arrow-left');
      var right = wrap.querySelector('.test-arrow-right');
      if (!scroll || !left || !right) return;
      var card = scroll.querySelector('.test-card');
      var step = (card ? card.offsetWidth : 260) + 22;
      [left, right].forEach(function(b){
        b.style.cursor = 'pointer';
        b.style.pointerEvents = 'auto';
      });
      left.addEventListener('click', function(e){ e.preventDefault(); scroll.scrollBy({left:-step, behavior:'smooth'}); });
      right.addEventListener('click', function(e){ e.preventDefault(); scroll.scrollBy({left:step, behavior:'smooth'}); });
      wrap.dataset.wired = '1';
    });
  }
  wireArrows();

  // Internal anchors (href="?page=…") work via normal browser navigation —
  // no interception needed; the new URL triggers a reload which re-runs
  // this router with the new params.
})();
</script>
"""

html_out = f"""<!doctype html>
<html lang="es">
<head>
{META}{BASE_CSS}
{LIGHT_CSS_SCOPED}
<style>
/* keep dark vars active when html.theme-dark explicitly set */
html.theme-dark{{color-scheme:dark}}
html:not(.theme-dark){{color-scheme:light}}
/* hide template placeholders */
template{{display:none!important}}
</style>
</head>
<body>
<div id="nav-mount"></div>
<main id="main"></main>
<div id="footer-mount"></div>
<div id="wa-mount"></div>

{nav_blocks}
{template_blocks}
{wa_templates}
{footer_templates}

{PERSIST_JS}
{ARROWS_JS}
{ROUTER_JS}
</body>
</html>
"""

OUT_HTML.write_text(html_out, encoding="utf-8")
print(f"[build] wrote {OUT_HTML}  ({len(html_out):,} bytes)")
print(f"[build] pages: {list(parts.keys())}")
