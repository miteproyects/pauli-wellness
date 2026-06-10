"""Build the production static site for luzentucuerpo.com.

Strategy
--------
1. Stub Streamlit and re-import app.py 8 times (one per page×lang) to capture
   the rendered HTML each combo would produce.
2. Apply production hardening (harden.py): self-host all images with srcset,
   replace iframes with click-to-load video facades, preload LCP + critical fonts.
3. Emit ONE self-contained HTML file per (page, lang) at clean URL paths:
       /            /ghk/        /resultados/      /estudios/         (ES)
       /en/         /en/ghk/     /en/results/      /en/studies/       (EN)
   Each file has its own <title>, <meta description>, single <h1>, canonical,
   hreflang pairs, JSON-LD structured data.
4. Emit sitemap.xml, robots.txt, llms.txt, 404.html, _redirects, _headers.

The theme (light/dark) is JS-only (localStorage), not in URLs — keeps URLs SEO-
clean (no duplicate-content issues from ?theme=).
"""
from __future__ import annotations
import importlib.util
import re
import sys
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.resolve()))
import harden  # noqa: E402

ROOT = Path(__file__).parent.resolve()
APP_PY = ROOT / "app.py"
OUT_DIR = ROOT / "site"
OUT_DIR.mkdir(exist_ok=True)

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

# ───── slice fragments out of each render ─────────────────────────────────────
_anchor_re = re.compile(r"(?s)(<style>.*?</style>)")
_nav_re = re.compile(r'(?s)<nav class="topnav">.*?</nav>\s*<div class="nav-spacer"></div>')
_wa_re = re.compile(r'(?s)<a href="https://wa\.me/[^"]+" target="_blank" rel="noopener" class="wa-float"[\s\S]*?</a>')
_script_re = re.compile(r"(?s)<script>.*?</script>")
_footer_re = re.compile(r'(?s)<div class="footer">.*?</div>\s*$', re.MULTILINE)


def split_render(html: str) -> dict[str, str]:
    styles = _anchor_re.findall(html)
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

    content = html
    if wa:
        content = content.split(wa, 1)[-1]
    if persist_js:
        content = content.split(persist_js, 1)[-1]
    if footer:
        content = content.rsplit(footer, 1)[0]
    if arrows_js:
        content = content.rsplit(arrows_js, 1)[0]

    return dict(
        base_css=base_css, light_css=light_css, nav=nav, wa=wa,
        persist_js=persist_js, content=content.strip(),
        footer=footer, arrows_js=arrows_js,
    )


parts = {k: split_render(v) for k, v in renders.items()}
first = parts["home-es"]
BASE_CSS = harden.harden_css(first["base_css"])
LIGHT_CSS = harden.harden_css(first["light_css"])
ARROWS_JS = first["arrows_js"]

# Re-scope LIGHT_CSS to apply when html lacks .theme-dark
LIGHT_CSS_SCOPED = (
    LIGHT_CSS
    .replace(":root{", "html:not(.theme-dark){")
    .replace(".test-arrow{", "html:not(.theme-dark) .test-arrow{")
    .replace(".study-item,.fact-card{", "html:not(.theme-dark) .study-item,html:not(.theme-dark) .fact-card{")
    .replace(".theme-tgl{", "html:not(.theme-dark) .theme-tgl{")
)

# ───── URL mapping: clean paths + per-page metadata ───────────────────────────
# Path: served at /<path>/index.html, browser sees /<path>/
URL_PATHS = {
    "home-es":       "",
    "ghk-es":        "ghk",
    "resultados-es": "resultados",
    "estudios-es":   "estudios",
    "home-en":       "en",
    "ghk-en":        "en/ghk",
    "resultados-en": "en/results",
    "estudios-en":   "en/studies",
}

# Per-page <title>, meta description, single <h1> hint
PAGE_META = {
    "home-es": {
        "title": "Luz en tu cuerpo · Pauli Wellness",
        "desc":  "Fototerapia LifeWave X39 + GHK-Cu. Dos décadas de ciencia, +200 patentes. Sin químicos, sin agujas. Despierta tu reparación celular con luz.",
        "h1":    "Dos décadas de ciencia. Más de 200 patentes en todo el mundo.",
    },
    "ghk-es": {
        "title": "GHK-Cu · El péptido de cobre · Pauli Wellness",
        "desc":  "GHK-Cu, el tripéptido de cobre que tu cuerpo ya produce. Qué es, por qué baja con la edad, y cómo el parche LifeWave X39 ayuda a elevarlo.",
        "h1":    "GHK-Cu · el péptido que tu cuerpo ya conoce",
    },
    "resultados-es": {
        "title": "Resultados reales · Pauli Wellness",
        "desc":  "Testimonios en video de personas que probaron los parches LifeWave X39 y comparten sus resultados — dolor, sueño, energía, piel, recuperación.",
        "h1":    "Resultados que cuentan las personas",
    },
    "estudios-es": {
        "title": "Estudios y patentes · LifeWave · Pauli Wellness",
        "desc":  "+200 patentes globales, +70 en regeneración. Estudios independientes de PSY-TEK, Center for Biofield Sciences y más. Premio Biotech Breakthrough 2025.",
        "h1":    "Estudios y patentes",
    },
    "home-en": {
        "title": "Light in your body · Pauli Wellness",
        "desc":  "LifeWave X39 phototherapy + GHK-Cu. Two decades of science, 200+ patents. No drugs, no needles. Wake up your cellular repair with light.",
        "h1":    "Two decades of science. More than 200 patents worldwide.",
    },
    "ghk-en": {
        "title": "GHK-Cu · The copper peptide · Pauli Wellness",
        "desc":  "GHK-Cu, the copper tripeptide your body already makes. What it is, why levels drop with age, how the LifeWave X39 patch helps raise it.",
        "h1":    "GHK-Cu · the peptide your body already knows",
    },
    "resultados-en": {
        "title": "Real results · Pauli Wellness",
        "desc":  "Video testimonials from people who tried the LifeWave X39 patches and shared their results — pain, sleep, energy, skin, recovery.",
        "h1":    "Results people share",
    },
    "estudios-en": {
        "title": "Studies and patents · LifeWave · Pauli Wellness",
        "desc":  "200+ global patents, 70+ in regeneration. Independent studies from PSY-TEK, Center for Biofield Sciences and more. 2025 Biotech Breakthrough Award.",
        "h1":    "Studies and patents",
    },
}

PAGE_LANG = {k: k.rsplit("-", 1)[1] for k in URL_PATHS}
SITE_ORIGIN = "https://luzentucuerpo.com"


def page_url(key: str) -> str:
    p = URL_PATHS[key]
    return SITE_ORIGIN + ("/" if not p else f"/{p}/")


def page_relurl(key: str) -> str:
    p = URL_PATHS[key]
    return "/" if not p else f"/{p}/"


# ───── nav URL rewriter — replace ?page=X&lang=Y → clean path ─────────────────
def _query_to_path(href: str) -> str:
    """Given an internal href like '?page=ghk&lang=en&theme=light', return the
    clean path equivalent like '/en/ghk/'."""
    if not href.startswith("?"):
        return href
    from urllib.parse import parse_qs
    params = parse_qs(href[1:])
    page = (params.get("page") or ["home"])[0]
    lang = (params.get("lang") or ["es"])[0]
    if page not in ("home", "ghk", "resultados", "estudios"):
        page = "home"
    if lang not in ("es", "en"):
        lang = "es"
    return page_relurl(f"{page}-{lang}")


_HREF_QUERY_RE = re.compile(r'href="(\?[^"]+)"')
_THEME_TGL_RE = re.compile(
    r'<a\s+href="\?[^"]*theme=[^"]*"[^>]*class="theme-tgl"[^>]*>([^<]*)</a>',
    re.IGNORECASE,
)


def rewrite_nav(nav_html: str, lang: str) -> str:
    """Convert all query-param hrefs to clean paths; convert theme toggle to
    a button (theme is JS-only now)."""
    # Rewrite the theme-toggle anchor to a real <button>
    title_es = "Cambiar de tema"
    title_en = "Toggle theme"
    title = title_es if lang == "es" else title_en
    btn = (
        f'<button type="button" class="theme-tgl" data-toggle-theme '
        f'aria-label="{title}" title="{title}">'
        f'<span class="theme-icon" aria-hidden="true">☀️</span>'
        f'</button>'
    )
    nav_html = _THEME_TGL_RE.sub(btn, nav_html)
    # Rewrite all remaining ?page=...&lang=... links to clean paths
    nav_html = _HREF_QUERY_RE.sub(lambda m: f'href="{_query_to_path(m.group(1))}"', nav_html)
    return nav_html


# Apply nav rewriter to every nav template
NAV_BLOCKS = {key: rewrite_nav(parts[key]["nav"], lang=PAGE_LANG[key]) for key in parts}
# Same for content (content blocks contain internal <a href="?page=...&lang=..."> too)
CONTENT_BLOCKS = {
    key: harden.harden_html(
        _HREF_QUERY_RE.sub(lambda m: f'href="{_query_to_path(m.group(1))}"', parts[key]["content"])
    )
    for key in parts
}
WA_BLOCKS = {key: parts[key]["wa"] for key in parts}
FOOTER_BLOCKS = {key: parts[key]["footer"] for key in parts}

# ───── legacy ?page=X&lang=Y redirect (homepage only, sync, pre-paint) ────────
LEGACY_PARAM_JS = """
<script>
(function(){
  var q = new URLSearchParams(location.search);
  var p = q.get('page'), l = q.get('lang') || 'es';
  if (!p) return;
  var map = {home:'', ghk:'ghk', resultados:'resultados', estudios:'estudios'};
  if (!(p in map)) return;
  var en = {ghk:'en/ghk', resultados:'en/results', estudios:'en/studies', home:'en'};
  var path = l === 'en' ? (en[p] || 'en') : map[p];
  location.replace('/' + (path ? path + '/' : ''));
})();
</script>
"""

# ───── theme + carousel + nav-active JS (per-page, no router needed) ──────────
PAGE_JS = """
<script>
(function(){
  // Theme: read localStorage → apply class → wire toggle button
  try {
    var t = localStorage.getItem('pauli-theme') || 'light';
    if (t === 'dark') document.documentElement.classList.add('theme-dark');
  } catch(e) {}
  function applyTheme(t){
    document.documentElement.classList.toggle('theme-dark', t === 'dark');
    var icon = document.querySelector('.theme-icon');
    if (icon) icon.textContent = t === 'dark' ? '🌙' : '☀️';
    try { localStorage.setItem('pauli-theme', t); } catch(e) {}
  }
  // Set the icon to match the initial theme
  document.addEventListener('DOMContentLoaded', function(){
    var t = document.documentElement.classList.contains('theme-dark') ? 'dark' : 'light';
    var icon = document.querySelector('.theme-icon');
    if (icon) icon.textContent = t === 'dark' ? '🌙' : '☀️';
  });
  // Theme toggle click
  document.addEventListener('click', function(ev){
    var btn = ev.target.closest('[data-toggle-theme]');
    if (!btn) return;
    var current = document.documentElement.classList.contains('theme-dark') ? 'dark' : 'light';
    applyTheme(current === 'dark' ? 'light' : 'dark');
  });

  // Testimonial-carousel arrows
  function wireArrows(){
    document.querySelectorAll('.test-scroll-wrap').forEach(function(wrap){
      if (wrap.dataset.wired) return;
      var scroll = wrap.querySelector('.test-scroll');
      var left = wrap.querySelector('.test-arrow-left');
      var right = wrap.querySelector('.test-arrow-right');
      if (!scroll || !left || !right) return;
      var card = scroll.querySelector('.test-card');
      var step = (card ? card.offsetWidth : 260) + 22;
      [left, right].forEach(function(b){ b.style.cursor = 'pointer'; b.style.pointerEvents = 'auto'; });
      left.addEventListener('click', function(e){ e.preventDefault(); scroll.scrollBy({left:-step, behavior:'smooth'}); });
      right.addEventListener('click', function(e){ e.preventDefault(); scroll.scrollBy({left:step, behavior:'smooth'}); });
      wrap.dataset.wired = '1';
    });
  }
  if (document.readyState === 'loading')
    document.addEventListener('DOMContentLoaded', wireArrows);
  else wireArrows();
})();
</script>
"""


# ───── per-page HTML emitter ──────────────────────────────────────────────────
def hreflang_links(key: str) -> str:
    """Return <link rel="alternate" hreflang="…"> tags for both langs +
    x-default (Spanish home as default since site is Latin-Am focused)."""
    page = key.rsplit("-", 1)[0]
    out = []
    for lang in ("es", "en"):
        k = f"{page}-{lang}"
        out.append(
            f'<link rel="alternate" hreflang="{lang}" href="{page_url(k)}">'
        )
    # x-default → Spanish version
    out.append(f'<link rel="alternate" hreflang="x-default" href="{page_url(f"{page}-es")}">')
    return "\n".join(out)


def canonical_link(key: str) -> str:
    return f'<link rel="canonical" href="{page_url(key)}">'


def jsonld_blocks(key: str, meta: dict) -> str:
    """Return one or more JSON-LD <script> blocks for the page."""
    import json
    page = key.rsplit("-", 1)[0]
    lang = PAGE_LANG[key]

    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Pauli Wellness",
        "url": SITE_ORIGIN,
        "logo": f"{SITE_ORIGIN}/img/og.png",
        "sameAs": [],
        "contactPoint": [{
            "@type": "ContactPoint",
            "contactType": "customer support",
            "telephone": "+593-93-989-0499",
            "availableLanguage": ["Spanish", "English"],
        }],
    }
    product = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "LifeWave X39 Phototherapy Patch",
        "image": f"{SITE_ORIGIN}/img/patches.webp",
        "description": ("Coin-sized non-transdermic phototherapy patch that reflects "
                        "specific wavelengths to the skin, supporting natural GHK-Cu "
                        "elevation — no drugs, no needles, no known side effects."),
        "brand": {"@type": "Brand", "name": "LifeWave"},
        "category": "Wellness / Phototherapy",
    }
    blocks = [org, product]

    # Add FAQPage on the GHK page (rich, factoid-style content)
    if page == "ghk":
        faq = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "¿Qué es el GHK-Cu?" if lang == "es" else "What is GHK-Cu?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": ("Es un pequeño péptido formado por tres aminoácidos — glicina, "
                                 "histidina y lisina — unidos a un átomo de cobre. Circula de "
                                 "forma natural en tu organismo y la investigación lo asocia con "
                                 "regeneración, cicatrización y renovación celular.") if lang == "es" else
                                ("It's a small peptide of three amino acids — glycine, histidine "
                                 "and lysine — bound to a copper atom. It circulates naturally in "
                                 "the body and research links it to regeneration, wound healing "
                                 "and cellular renewal."),
                    },
                },
                {
                    "@type": "Question",
                    "name": ("¿Por qué importa a partir de los 30?" if lang == "es"
                             else "Why does it matter after 30?"),
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": ("Los niveles de GHK-Cu bajan ~60% entre los 20 y los 60 años, "
                                 "y con ellos la capacidad natural del cuerpo para regenerarse.") if lang == "es"
                                else ("GHK-Cu levels drop ~60% between ages 20 and 60, and with "
                                      "them the body's natural capacity to regenerate."),
                    },
                },
                {
                    "@type": "Question",
                    "name": ("¿El parche contiene GHK-Cu?" if lang == "es"
                             else "Does the patch contain GHK-Cu?"),
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": ("No. El parche no contiene GHK-Cu ni lo libera en el cuerpo. "
                                 "Su superficie patentada refleja longitudes de onda específicas "
                                 "que estimulan al organismo a elevar el GHK-Cu que produce "
                                 "naturalmente.") if lang == "es" else
                                ("No. The patch contains no GHK-Cu and releases none into the body. "
                                 "Its patented surface reflects specific wavelengths that stimulate "
                                 "the body to raise the GHK-Cu it naturally produces."),
                    },
                },
            ],
        }
        blocks.append(faq)

    return "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
        for b in blocks
    )


def render_page(key: str) -> str:
    meta = PAGE_META[key]
    lang = PAGE_LANG[key]
    nav_html = NAV_BLOCKS[key]
    content_html = CONTENT_BLOCKS[key]
    wa_html = WA_BLOCKS[key]
    footer_html = FOOTER_BLOCKS[key]

    head_meta = (
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<meta name="theme-color" content="#000000">\n'
        f'<meta name="description" content="{meta["desc"]}">\n'
        f'<meta property="og:title" content="{meta["title"]}">\n'
        f'<meta property="og:description" content="{meta["desc"]}">\n'
        '<meta property="og:type" content="website">\n'
        f'<meta property="og:url" content="{page_url(key)}">\n'
        f'<meta property="og:image" content="{SITE_ORIGIN}/img/og.png">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{meta["title"]}">\n'
        f'<meta name="twitter:description" content="{meta["desc"]}">\n'
        f'<meta name="twitter:image" content="{SITE_ORIGIN}/img/og.png">\n'
        f'<title>{meta["title"]}</title>\n'
        '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'%3E%3Ctext y=\'26\' font-size=\'26\'%3E%E2%9C%A8%3C/text%3E%3C/svg%3E">\n'
        f'{canonical_link(key)}\n'
        f'{hreflang_links(key)}\n'
    )

    # Legacy ?page= redirect script only on the two homepages (where old links land)
    legacy_js = LEGACY_PARAM_JS if key in ("home-es", "home-en") else ""
    page_kind = key.rsplit("-", 1)[0]

    return f"""<!doctype html>
<html lang="{lang}">
<head>
{head_meta}{legacy_js}{harden.head_extras(page=page_kind)}{BASE_CSS}
{LIGHT_CSS_SCOPED}
<style>
html.theme-dark{{color-scheme:dark}}
html:not(.theme-dark){{color-scheme:light}}
</style>
{harden.FACADE_CSS}
{jsonld_blocks(key, meta)}
</head>
<body>
{nav_html}
<main>{content_html}</main>
{footer_html}
{wa_html}
{ARROWS_JS}
{harden.FACADE_JS}
{PAGE_JS}
</body>
</html>
"""


# ───── emit per-page HTML files ───────────────────────────────────────────────
total_bytes = 0
for key in URL_PATHS:
    path = URL_PATHS[key]
    out_file = OUT_DIR / path / "index.html" if path else OUT_DIR / "index.html"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    html = render_page(key)
    out_file.write_text(html, encoding="utf-8")
    total_bytes += len(html)
    print(f"[build] {out_file.relative_to(OUT_DIR)}  {len(html):>6,} bytes")

print(f"[build] total HTML: {total_bytes:,} bytes across {len(URL_PATHS)} pages")

# ───── sitemap.xml ────────────────────────────────────────────────────────────
sitemap_urls = []
for key in URL_PATHS:
    page = key.rsplit("-", 1)[0]
    url = page_url(key)
    alternates = "\n".join(
        f'    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(f"{page}-{l}")}"/>'
        for l in ("es", "en")
    )
    alternates += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(f"{page}-es")}"/>'
    sitemap_urls.append(f"""  <url>
    <loc>{url}</loc>
{alternates}
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if page == 'home' else '0.8'}</priority>
  </url>""")

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(sitemap_urls)}
</urlset>
"""
(OUT_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")

# ───── robots.txt — allow AI crawlers explicitly ──────────────────────────────
robots = f"""# robots.txt for luzentucuerpo.com

User-agent: *
Allow: /
Disallow: /img/.tmp-orig/

# AI / LLM crawlers — explicitly allowed
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Bingbot
Allow: /

Sitemap: {SITE_ORIGIN}/sitemap.xml
"""
(OUT_DIR / "robots.txt").write_text(robots, encoding="utf-8")

# ───── IndexNow key file — instant push to Bing/Yandex/Seznam/Naver ────────────
# Must be served at https://luzentucuerpo.com/<KEY>.txt containing exactly the key.
# Pair with indexnow_ping.py after each deploy to notify search engines of changes.
INDEXNOW_KEY = "b95ba6055d330203b26848096f2d15c0"
(OUT_DIR / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")

# ───── llms.txt — concise summary for LLMs ────────────────────────────────────
llms = f"""# Pauli Wellness — Luz en tu cuerpo

> Pauli Wellness es una pequeña distribuidora ecuatoriana de los parches de
> fototerapia LifeWave X39 (basados en GHK-Cu), una tecnología con más de 200
> patentes globales y dos décadas de desarrollo. El sitio explica qué hace la
> tecnología, muestra testimonios reales en video y conecta a los visitantes
> con Pauli vía WhatsApp para preguntas y pedidos.
>
> Pauli Wellness is a small Ecuadorian distributor of LifeWave X39 phototherapy
> patches (GHK-Cu based), a 200+ patent technology developed over two decades.
> The site explains the science, shows real video testimonials, and connects
> visitors to Pauli via WhatsApp for questions and orders.

## Pages

- [Inicio (ES)]({page_url("home-es")}) — La página principal con el resumen, video explicativo y testimonios.
- [GHK-Cu (ES)]({page_url("ghk-es")}) — Qué es el péptido de cobre GHK-Cu y por qué importa con la edad.
- [Resultados (ES)]({page_url("resultados-es")}) — Testimonios en video y patrones de cambios reportados.
- [Estudios (ES)]({page_url("estudios-es")}) — Patentes, investigación independiente y reconocimientos.
- [Home (EN)]({page_url("home-en")}) — English overview.
- [GHK-Cu (EN)]({page_url("ghk-en")}) — English copper-peptide explainer.
- [Results (EN)]({page_url("resultados-en")}) — English testimonials page.
- [Studies (EN)]({page_url("estudios-en")}) — English studies + patents page.

## Contacto / Contact

- WhatsApp: +593 93 989 0499 (Pauli, Ecuador)

## Key claims (from manufacturer LifeWave, not medical advice)

- The X39 patch uses light reflection (no drugs, no needles, nothing crosses the skin) to support the body's natural GHK-Cu production.
- GHK-Cu is a copper-bound tripeptide (Gly-His-Lys-Cu) the body produces naturally; levels drop ~60% from age 20 → 60.
- LifeWave holds 200+ global patents; David Schmidt (founder) is named on 70+ regeneration-specific patents.
- LifeWave received the 2025 Biotech Breakthrough Award in "Stem Cell Innovation of the Year".
- 30/90-day money-back guarantee on patches.

The site contains testimonial videos hosted on Vimeo and one Spanish explainer hosted on YouTube; the videos are presented as click-to-load thumbnails to keep first-paint fast.
"""
(OUT_DIR / "llms.txt").write_text(llms, encoding="utf-8")

# ───── 404.html ──────────────────────────────────────────────────────────────
# Cloudflare Pages auto-serves /404.html for unknown paths with status 404.
not_found = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex">
<title>Página no encontrada · Pauli Wellness</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'%3E%3Ctext y=\'26\' font-size=\'26\'%3E%E2%9C%A8%3C/text%3E%3C/svg%3E">
<style>
body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Inter',sans-serif;background:#0a0a0a;color:#fff;
  min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:2rem}}
.wrap{{max-width:560px}}
h1{{font-size:clamp(28px,4vw,48px);margin:0 0 1rem;color:#d4a94a}}
p{{font-size:clamp(16px,1.6vw,20px);line-height:1.6;opacity:.9;margin:0 0 2rem}}
a{{color:#d4a94a;text-decoration:none;font-weight:700;border-bottom:2px solid #d4a94a;padding-bottom:2px}}
a:hover{{color:#b8923c;border-color:#b8923c}}
</style>
</head>
<body>
<main class="wrap">
<h1>404 — Página no encontrada</h1>
<p>La página que buscas no existe o fue movida.<br>Volvamos al inicio.</p>
<p><a href="/">← Volver a la página principal</a></p>
<p style="font-size:14px;opacity:.6;margin-top:2rem">English: <a href="/en/">Back to homepage</a></p>
</main>
</body>
</html>
"""
(OUT_DIR / "404.html").write_text(not_found, encoding="utf-8")

# ───── _redirects ─────────────────────────────────────────────────────────────
# IMPORTANT: Cloudflare Pages `_redirects` does NOT support query strings in
# the source path — a line like `/?page=home  /  301` is parsed as `/ → /`,
# which 301-loops the homepage (learned the hard way). Legacy ?page=X&lang=Y
# URLs are instead handled by a tiny client-side script injected into the two
# homepage files (see LEGACY_PARAM_JS) — humans get redirected, crawlers just
# see the homepage, and the clean paths are what's in the sitemap.
(OUT_DIR / "_redirects").write_text(
    "# (intentionally empty — see build_static.py for why)\n", encoding="utf-8"
)

# ───── _headers — security + cache ────────────────────────────────────────────
headers = """# Global security headers
/*
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=(), interest-cohort=()
  X-Frame-Options: SAMEORIGIN

# Long cache for fingerprint-able static assets (versioned by filename)
/img/*
  Cache-Control: public, max-age=31536000, immutable
  Access-Control-Allow-Origin: *

/thumbs/*
  Cache-Control: public, max-age=31536000, immutable
  Access-Control-Allow-Origin: *

/fonts/*
  Cache-Control: public, max-age=31536000, immutable
  Access-Control-Allow-Origin: *

# HTML: must-revalidate (so updates ship fast)
/*.html
  Cache-Control: public, max-age=0, must-revalidate

# robots/sitemap/llms — short TTL
/robots.txt
  Content-Type: text/plain; charset=utf-8
  Cache-Control: public, max-age=3600

/sitemap.xml
  Content-Type: application/xml; charset=utf-8
  Cache-Control: public, max-age=3600

/llms.txt
  Content-Type: text/plain; charset=utf-8
  Cache-Control: public, max-age=3600
"""
(OUT_DIR / "_headers").write_text(headers, encoding="utf-8")

print(f"[build] emitted sitemap.xml, robots.txt, llms.txt, 404.html, _redirects, _headers")
print(f"[build] DONE")
