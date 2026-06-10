"""Post-processing pipeline that takes the rendered HTML and applies all
production perf hardening: self-hosted WebP images with srcset/width/height,
video facades (no iframes load until clicked), font preload, LCP preload, CSP/
security/cache headers ready.

Public entry: harden_html(html: str, *, page: str, lang: str) -> str
Also exports: FACADE_CSS, FACADE_JS, EXTRA_HEAD (caller injects), HERO_CSS_PATCH
"""
from __future__ import annotations
import re

# ───── image meta: substring → (slug, intrinsic w, h, srcset widths, lazy) ─
# `src_substr` is matched against the URL the renderer emits.
IMG_META = {
    "womanAging-battery-1-1024x981.png":               {"slug": "aging-battery",   "w": 1024, "h": 981,  "widths": [400, 800, 1024]},
    "3-MinuteVideo-thumbnail-2-1.png":                  {"slug": "video-thumb",     "w": 1920, "h": 1080, "widths": [400, 800]},
    "SN-Patch-placement-scaled-1-690x1024.jpg":         {"slug": "patch-placement", "w": 690,  "h": 1024, "widths": [400, 690]},
    "490141872_10162757194347458_245241563246855534_n-1024x1024.jpg": {"slug": "couple", "w": 1024, "h": 1024, "widths": [400, 800, 1024]},
    "ManWoman-Kitchen-swirl-1024x645.png":              {"slug": "kitchen",         "w": 1024, "h": 645,  "widths": [400, 800, 1024]},
    "Man-frontOfMtn-819x1024.png":                      {"slug": "mountain",        "w": 819,  "h": 1024, "widths": [400, 819]},
    "Phototherapy-LifeWave-patches-clean-1024x1024.jpg":{"slug": "patches",         "w": 1024, "h": 1024, "widths": [400, 800, 1024]},
    "timeline-firstFewDays-2.png":                      {"slug": "tl-days",         "w": 600,  "h": 300,  "widths": [240, 480]},
    "timeline-6weeks-2.png":                            {"slug": "tl-4w",           "w": 600,  "h": 300,  "widths": [240, 480]},
    "timeline-3women.png":                              {"slug": "tl-6w",           "w": 600,  "h": 301,  "widths": [240, 480]},
    "timeline-3months-2.png":                           {"slug": "tl-3m",           "w": 600,  "h": 301,  "widths": [240, 480]},
    "timeline-meditation.png":                          {"slug": "tl-12m",          "w": 600,  "h": 301,  "widths": [240, 480]},
    "HoldingPatch-clean-cropped-1024x759.png":          {"slug": "holding",         "w": 1024, "h": 759,  "widths": [340, 680]},
    "90-dayGuarantee.png":                              {"slug": "badge",           "w": 500,  "h": 500,  "widths": [160, 320]},
}

# ───── facade CSS — styles the click-to-load video poster ─────────────────
FACADE_CSS = """
<style>
.video-facade{position:absolute;inset:0;width:100%;height:100%;border:0;padding:0;margin:0;cursor:pointer;
  background-color:#000;overflow:hidden;
  display:flex;align-items:center;justify-content:center;transition:opacity .2s}
.video-facade>img{position:absolute;inset:0;width:100%!important;height:100%!important;object-fit:cover;z-index:0}
.video-facade::before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(0,0,0,.05) 0%,rgba(0,0,0,.35) 100%);transition:background .2s}
.video-facade:hover::before{background:linear-gradient(180deg,rgba(0,0,0,.1) 0%,rgba(0,0,0,.5) 100%)}
.video-facade .play-icon{position:relative;z-index:2;width:68px;height:48px;background:rgba(0,0,0,.7);border-radius:14px;
  display:flex;align-items:center;justify-content:center;transition:background .2s}
.video-facade:hover .play-icon{background:rgba(220,40,40,.92)}
.video-facade .play-icon svg{width:22px;height:22px;fill:#fff;margin-left:3px}
.video-wrap .video-facade,.test-card .video-facade{display:flex}
.video-wrap{position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:12px;
  box-shadow:0 12px 40px rgba(0,0,0,.25)}
.test-card{position:relative}
@media(prefers-reduced-motion:reduce){
  .video-facade,.video-facade::before,.video-facade .play-icon{transition:none}
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
}
/* A11y: visible keyboard focus on all interactive elements */
:focus{outline:none}
:focus-visible{outline:3px solid var(--accent,#d4a94a);outline-offset:3px;border-radius:4px}
button:focus-visible,a:focus-visible,iframe:focus-visible,.video-facade:focus-visible,.theme-tgl:focus-visible{
  outline:3px solid var(--accent,#d4a94a);outline-offset:3px}
.video-facade:focus-visible{outline-offset:-3px}
/* Media correctness: width/height attrs reserve space; CSS keeps ratio */
main img:not(.hero-bg){height:auto}
/* Hero as a real <img> (LCP paints earlier than a ::before background).
   The ::before that used to carry the photo is disabled; the veil ::after
   stays on top of the img (z-index -2 < veil -1). */
.hero-wrap::before{content:none!important}
/* contrast(1.75) is PRE-BAKED into the WebP — no CSS filter, cheaper paint */
.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  object-position:center 30%;z-index:-2}
/* ghk hero: contrast(1.1) likewise baked into ghk-hero-*.webp */
.page-hero-ghk::before{filter:none!important}
/* Zero-CLS font swap: Arial with Inter-matched metrics as the fallback,
   so the swap to Inter doesn't reflow text (the H1 was shifting 0.156). */
@font-face{font-family:'Inter-fallback';size-adjust:107%;ascent-override:90.44%;
  descent-override:22.52%;line-gap-override:0%;src:local('Arial')}
html,body{font-family:'Inter','Inter-fallback',sans-serif!important}
/* ── WCAG AA color contrast ──────────────────────────────────────────
   Light theme: #b8923c gold on near-white = 2.9:1 (fails 4.5:1).
   Use a darker bronze for light mode; switch solid-accent components
   to white text (7.3:1 on the bronze). Dark mode keeps #d4a94a on
   black (≈9:1) untouched. */
html:not(.theme-dark){--accent:#6e511a;--accent-hover:#543d13}
/* Buttons are <a> tags and the base CSS forces a{color:inherit!important},
   so these need anchor selectors + !important to actually win. */
html:not(.theme-dark) a.btn{color:#fff!important}
html:not(.theme-dark) a.btn-outline{color:var(--accent)!important;background:transparent}
html:not(.theme-dark) a.btn-outline:hover{background:var(--accent);color:#fff!important}
html:not(.theme-dark) .step-num{color:#fff}
html:not(.theme-dark) .lang-switch a.active{color:#fff!important}
/* Dark theme: gold solid buttons need DARK text (white on #d4a94a = 2.2:1) */
html.theme-dark a.btn{color:#111!important}
html.theme-dark a.btn-outline{color:var(--accent)!important;background:transparent}
html.theme-dark a.btn-outline:hover{background:var(--accent);color:#111!important}
/* WhatsApp-green buttons: dark green text in BOTH themes (white fails AA) */
a.btn-wa{color:#0b3d2e!important}
a.btn-wa:hover{color:#06281e!important}
html.theme-dark a.btn-wa{color:#0b3d2e!important}
/* Cards keep a fixed WHITE background in BOTH themes → always dark gold */
.tl-card h3{color:#6e511a}
/* WhatsApp-green CTAs: white on #25D366 is 2:1 — use dark green text */
.nav-contact,.nav-links a.nav-contact,.nav-links a.nav-contact:link,.nav-links a.nav-contact:visited{color:#0b3d2e!important}
.nav-contact:hover{color:#06281e!important}
.btn-wa{color:#0b3d2e}.btn-wa:hover{color:#06281e}
/* Hero bg: serve the 400w variant on small screens (matches the
   media-scoped preload; avoids double-download + oversized LCP). */
@media(max-width:600px){
  .hero-wrap::before{background-image:url('/img/patch-placement-400.webp')}
  .page-hero-ghk::before{background-image:url('/img/ghk-hero-400.webp')}
}
</style>
"""

# ───── facade JS — swaps button → iframe on click + preconnects on hover ──
# Inert until user intent: zero third-party requests until click.
FACADE_JS = """
<script>
(function(){
  var preconnects = {vimeo: 'https://player.vimeo.com', youtube: 'https://www.youtube.com'};
  var preconnectsCdn = {vimeo: 'https://i.vimeocdn.com', youtube: 'https://i.ytimg.com'};
  var preconnected = {};
  function preconnect(provider){
    if (preconnected[provider]) return;
    preconnected[provider] = true;
    [preconnects[provider], preconnectsCdn[provider]].forEach(function(href){
      if (!href) return;
      var l = document.createElement('link');
      l.rel = 'preconnect'; l.href = href; l.crossOrigin = ''; document.head.appendChild(l);
    });
  }
  function swap(btn){
    var provider = btn.dataset.provider, id = btn.dataset.id, title = btn.dataset.title || '';
    var iframe = document.createElement('iframe');
    if (provider === 'youtube') {
      iframe.src = 'https://www.youtube.com/embed/' + id + '?autoplay=1&rel=0&modestbranding=1';
    } else {
      iframe.src = 'https://player.vimeo.com/video/' + id + '?autoplay=1&title=0&byline=0&portrait=0&dnt=1';
    }
    iframe.title = title;
    iframe.allow = 'autoplay;fullscreen;picture-in-picture';
    iframe.setAttribute('allowfullscreen', '');
    iframe.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;border:0;display:block';
    btn.parentNode.replaceChild(iframe, btn);
  }
  document.addEventListener('click', function(ev){
    var btn = ev.target.closest('.video-facade');
    if (!btn) return;
    ev.preventDefault();
    preconnect(btn.dataset.provider);
    swap(btn);
  });
  document.addEventListener('pointerover', function(ev){
    var btn = ev.target.closest('.video-facade');
    if (!btn) return;
    preconnect(btn.dataset.provider);
  }, {passive: true});
  document.addEventListener('keydown', function(ev){
    if (ev.key !== 'Enter' && ev.key !== ' ') return;
    var btn = ev.target.closest('.video-facade');
    if (!btn) return;
    ev.preventDefault();
    preconnect(btn.dataset.provider);
    swap(btn);
  });
})();
</script>
"""

# ───── HERO CSS PATCH: rewrite whythelight URLs in inline <style> blocks ──
# CSS background-image references in BASE_CSS use whythelight; redirect to local
HERO_CSS_REPLACEMENTS = [
    ("https://whythelight.com/wp-content/uploads/2025/09/SN-Patch-placement-scaled-1-690x1024.jpg",
     "/img/patch-placement-690.webp"),
    ("https://raw.githubusercontent.com/miteproyects/pauli-wellness/main/assets/ghk-hero.png",
     "/img/ghk-hero-800.webp"),
]


def _build_img_tag(meta: dict, alt: str, eager: bool = False, sizes_attr: str = "(max-width: 900px) 100vw, 50vw") -> str:
    """Return <img …> with srcset/sizes/width/height/loading/decoding."""
    slug, w, h, widths = meta["slug"], meta["w"], meta["h"], meta["widths"]
    srcset_parts = [f"/img/{slug}-{wx}.webp {wx}w" for wx in widths]
    src = f"/img/{slug}-{widths[-1]}.webp"
    loading = "eager" if eager else "lazy"
    fp = ' fetchpriority="high"' if eager else ""
    return (
        f'<img src="{src}" '
        f'srcset="{", ".join(srcset_parts)}" '
        f'sizes="{sizes_attr}" '
        f'width="{w}" height="{h}" '
        f'alt="{alt}" '
        f'loading="{loading}" decoding="async"{fp}>'
    )


# Pattern matches <img ... src="https://whythelight.com/.../FILENAME" ... [alt="..."] ...>
_IMG_RE = re.compile(
    r'<img\b([^>]*?)\bsrc="https://whythelight\.com/[^"]*?/([^/"]+)"([^>]*)>',
    re.IGNORECASE,
)
_ALT_RE = re.compile(r'\balt="([^"]*)"', re.IGNORECASE)
_CLASS_RE = re.compile(r'\bclass="([^"]*)"', re.IGNORECASE)
_STYLE_RE = re.compile(r'\bstyle="([^"]*)"', re.IGNORECASE)

# Iframe patterns
_VIMEO_IFRAME_RE = re.compile(
    r'<iframe([^>]*?)\bsrc="https://player\.vimeo\.com/video/(\d+)[^"]*"([^>]*)></iframe>',
    re.IGNORECASE,
)
_YT_IFRAME_RE = re.compile(
    r'<iframe([^>]*?)\bsrc="https://www\.youtube\.com/embed/([\w\-]+)[^"]*"([^>]*)></iframe>',
    re.IGNORECASE,
)
_TITLE_ATTR_RE = re.compile(r'\btitle="([^"]*)"', re.IGNORECASE)


def _facade_button(provider: str, vid: str, title: str, thumb_path: str, extra_attrs: str = "") -> str:
    """Poster is a lazy <img>, NOT a CSS background — browsers eager-load
    background-image regardless of viewport; with 62 facades that was
    ~180 KB of thumbnails competing with the LCP image on first load."""
    play_svg = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
    aria = f'Play video: {title}' if title else f'Play {provider} video'
    # Thumb intrinsic sizes: vimeo posters 400×~225 (16:9-ish), youtube 800×450
    w, h = (800, 450) if provider == "youtube" else (400, 225)
    return (
        f'<button class="video-facade" type="button" '
        f'data-provider="{provider}" data-id="{vid}" data-title="{title}" '
        f'aria-label="{aria}"{extra_attrs}>'
        f'<img src="{thumb_path}" alt="" width="{w}" height="{h}" '
        f'loading="lazy" decoding="async">'
        f'<span class="play-icon">{play_svg}</span>'
        f'</button>'
    )


def _replace_img(match: re.Match) -> str:
    pre_attrs, filename, post_attrs = match.group(1), match.group(2), match.group(3)
    meta = IMG_META.get(filename)
    if not meta:
        return match.group(0)
    full_tag_attrs = pre_attrs + post_attrs
    alt_m = _ALT_RE.search(full_tag_attrs)
    alt = alt_m.group(1) if alt_m else ""
    class_m = _CLASS_RE.search(full_tag_attrs)
    style_m = _STYLE_RE.search(full_tag_attrs)
    cls_extra = f' class="{class_m.group(1)}"' if class_m else ""
    style_extra = f' style="{style_m.group(1)}"' if style_m else ""
    # Build base img tag
    base = _build_img_tag(meta, alt=alt, eager=False)
    # Re-inject class + style if they were on the original
    base = base.replace("<img ", f"<img{cls_extra}{style_extra} ")
    return base


def _replace_vimeo(match: re.Match) -> str:
    pre_attrs, vid, post_attrs = match.group(1), match.group(2), match.group(3)
    full = pre_attrs + post_attrs
    title_m = _TITLE_ATTR_RE.search(full)
    title = title_m.group(1) if title_m else "Video"
    thumb = f"/thumbs/vimeo-{vid}.webp"
    return _facade_button("vimeo", vid, title, thumb)


def _replace_youtube(match: re.Match) -> str:
    pre_attrs, vid, post_attrs = match.group(1), match.group(2), match.group(3)
    full = pre_attrs + post_attrs
    title_m = _TITLE_ATTR_RE.search(full)
    title = title_m.group(1) if title_m else "Video"
    thumb = f"/thumbs/youtube-{vid}.webp"
    return _facade_button("youtube", vid, title, thumb)


_HERO_OPEN_RE = re.compile(r'(<section class="sec hero-wrap"[^>]*>)')
_HERO_IMG = (
    '<img class="hero-bg" src="/img/patch-placement-690.webp" '
    'srcset="/img/patch-placement-400.webp 400w, /img/patch-placement-690.webp 690w" '
    'sizes="100vw" width="690" height="1024" alt="" '
    'fetchpriority="high" decoding="async">'
)


def harden_html(html: str) -> str:
    """Apply all production transformations to a chunk of HTML."""
    # 0. Hero photo becomes a real <img> right inside the hero section
    #    (only the home pages contain .hero-wrap)
    html = _HERO_OPEN_RE.sub(lambda m: m.group(1) + _HERO_IMG, html)
    # 1. Replace whythelight image hotlinks → self-hosted WebP with srcset/dims
    html = _IMG_RE.sub(_replace_img, html)
    # 2. Replace Vimeo iframes with click-to-load facades
    html = _VIMEO_IFRAME_RE.sub(_replace_vimeo, html)
    # 3. Replace YouTube iframes with click-to-load facades
    html = _YT_IFRAME_RE.sub(_replace_youtube, html)
    # 4. Move PDF off raw.githubusercontent.com → self-host
    html = html.replace(
        "https://raw.githubusercontent.com/miteproyects/pauli-wellness/main/Packages-and-Pricing.pdf",
        "/Packages-and-Pricing.pdf",
    )
    # 5. Ensure all external links (wa.me, etc.) carry rel="noopener"
    html = re.sub(
        r'<a([^>]*?\btarget="_blank"[^>]*?)(?<!rel=")(>)',
        lambda m: m.group(1).rstrip() + (' rel="noopener noreferrer">'
                                          if 'rel=' not in m.group(1) else '>'),
        html,
    )
    return html


def harden_css(css: str) -> str:
    """Replace whythelight URLs in inline <style> CSS with local /img/* paths."""
    for src, dst in HERO_CSS_REPLACEMENTS:
        css = css.replace(src, dst)
    return css


def head_extras(page: str = "home") -> str:
    """Extra <head> tags: media-scoped LCP-image preloads + critical fonts.

    Per-page hero preloads (preloading another page's hero wastes bytes and
    competes with the real LCP):
      home → patch-placement (400w mobile / 690w desktop, matching the CSS
              media query in FACADE_CSS)
      ghk  → ghk-hero (400w mobile / 800w desktop)
      other pages → no image preload (text-only heroes)

    Fonts: latin-400 + latin-800 cover ~95% of above-the-fold text;
    latin-ext subsets load on demand via unicode-range.
    """
    hero = ""
    # home: NO preload — the hero is a real early-<body> <img fetchpriority=high>
    # with its own srcset; a media-scoped preload would pick a different
    # variant than the img's DPR-aware srcset and double-download.
    if page == "ghk":
        hero = (
            '<link rel="preload" as="image" href="/img/ghk-hero-400.webp" '
            'media="(max-width:600px)" fetchpriority="high">\n'
            '<link rel="preload" as="image" href="/img/ghk-hero-800.webp" '
            'media="(min-width:601px)" fetchpriority="high">\n'
        )
    return (
        hero
        + '<link rel="preload" as="font" type="font/woff2" '
        'href="/fonts/inter-latin-400-normal.woff2" crossorigin>\n'
        '<link rel="preload" as="font" type="font/woff2" '
        'href="/fonts/inter-latin-800-normal.woff2" crossorigin>\n'
    )
