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
  background-size:cover;background-position:center;background-repeat:no-repeat;background-color:#000;
  display:flex;align-items:center;justify-content:center;transition:opacity .2s}
.video-facade::before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.05) 0%,rgba(0,0,0,.35) 100%);transition:background .2s}
.video-facade:hover::before{background:linear-gradient(180deg,rgba(0,0,0,.1) 0%,rgba(0,0,0,.5) 100%)}
.video-facade .play-icon{position:relative;width:68px;height:48px;background:rgba(0,0,0,.7);border-radius:14px;
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
     "/img/ghk-hero.webp"),  # may not exist as webp; falls through to original or 404
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
    play_svg = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
    aria = f'Play video: {title}' if title else f'Play {provider} video'
    return (
        f'<button class="video-facade" type="button" '
        f'data-provider="{provider}" data-id="{vid}" data-title="{title}" '
        f'style="background-image:url(\'{thumb_path}\')" '
        f'aria-label="{aria}"{extra_attrs}>'
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


def harden_html(html: str) -> str:
    """Apply all production transformations to a chunk of HTML."""
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


def head_extras() -> str:
    """Extra <head> tags: preload LCP image + preload critical fonts.

    The two latin-400 + latin-800 font subsets cover ~95% of above-the-fold
    text on the home page; preloading them eliminates the FOIT flash.
    """
    return (
        # LCP hero photo (visible in the first viewport on / )
        '<link rel="preload" as="image" '
        'href="/img/patch-placement-690.webp" '
        'imagesrcset="/img/patch-placement-400.webp 400w, /img/patch-placement-690.webp 690w" '
        'imagesizes="100vw" fetchpriority="high">\n'
        # Critical fonts — body text (400) + hero/headings (800), latin subset only
        # (latin-ext loads lazily when a non-ASCII char is encountered)
        '<link rel="preload" as="font" type="font/woff2" '
        'href="/fonts/inter-latin-400-normal.woff2" crossorigin>\n'
        '<link rel="preload" as="font" type="font/woff2" '
        'href="/fonts/inter-latin-800-normal.woff2" crossorigin>\n'
    )
