"""Pauli Wellness — multi-page landing (ES/EN) with top nav + dark/light theme.
All Spanish copy is Pauli Wellness's own original wording.
All navigation links are internal (no external links to whythelight.com).
"""
import streamlit as st

st.set_page_config(
    page_title="Pauli Wellness",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Routing, language & theme from query params ─────────────────────────────
qp = st.query_params
page = qp.get("page", "home")
if page not in ("home", "ghk", "resultados", "estudios"):
    page = "home"
lang = qp.get("lang", "es")
if lang not in ("es", "en"):
    lang = "es"
theme = qp.get("theme", "dark")
if theme not in ("dark", "light"):
    theme = "dark"
theme_other = "light" if theme == "dark" else "dark"
theme_icon = "🌙" if theme == "dark" else "☀️"
theme_title_es = "Cambiar a modo claro" if theme == "dark" else "Cambiar a modo oscuro"
theme_title_en = "Switch to light mode" if theme == "dark" else "Switch to dark mode"
theme_title = theme_title_es if lang == "es" else theme_title_en

# ─── Config ──────────────────────────────────────────────────────────────────
WA_NUM = "593939890499"
WA_TXT_ES = "Hola%20Pauli!%20Vi%20tu%20pagina%20y%20me%20gustaria%20saber%20mas%20sobre%20los%20parches%20LifeWave"
WA_TXT_EN = "Hi%20Pauli!%20I%20saw%20your%20site%20and%20I%27d%20love%20to%20learn%20more%20about%20the%20LifeWave%20patches"
WA = f"https://wa.me/{WA_NUM}?text=" + (WA_TXT_ES if lang == "es" else WA_TXT_EN)

# Internal page routes (replaces prior whythelight.com links)
# All routes preserve current lang + theme so theme persists across navigation.
_q = f"lang={lang}&theme={theme}"
LINK_HOME = f"?page=home&{_q}"
LINK_GHK = f"?page=ghk&{_q}"
LINK_RESULTS = f"?page=resultados&{_q}"
LINK_STUDIES = f"?page=estudios&{_q}"
LINK_THEME_TOGGLE = f"?page={page}&lang={lang}&theme={theme_other}"
LINK_LANG_ES = f"?page={page}&lang=es&theme={theme}"
LINK_LANG_EN = f"?page={page}&lang=en&theme={theme}"

# Image URLs (same asset hosts used by whythelight.com; no text mirroring)
IMG_AGING = "https://whythelight.com/wp-content/uploads/2025/11/womanAging-battery-1-1024x981.png"
IMG_VIDEO_THUMB = "https://whythelight.com/wp-content/uploads/2025/11/3-MinuteVideo-thumbnail-2-1.png"
IMG_PATCH_PLACEMENT = "https://whythelight.com/wp-content/uploads/2025/09/SN-Patch-placement-scaled-1-690x1024.jpg"
IMG_COUPLE = "https://whythelight.com/wp-content/uploads/2025/09/490141872_10162757194347458_245241563246855534_n-1024x1024.jpg"
IMG_KITCHEN = "https://whythelight.com/wp-content/uploads/2025/09/ManWoman-Kitchen-swirl-1024x645.png"
IMG_MOUNTAIN = "https://whythelight.com/wp-content/uploads/2025/11/Man-frontOfMtn-819x1024.png"
IMG_PATCHES = "https://whythelight.com/wp-content/uploads/2025/09/Phototherapy-LifeWave-patches-clean-1024x1024.jpg"
IMG_TL_DAYS = "https://whythelight.com/wp-content/uploads/2025/09/timeline-firstFewDays-2.png"
IMG_TL_4W = "https://whythelight.com/wp-content/uploads/2025/09/timeline-6weeks-2.png"
IMG_TL_6W = "https://whythelight.com/wp-content/uploads/2025/09/timeline-3women.png"
IMG_TL_3M = "https://whythelight.com/wp-content/uploads/2025/09/timeline-3months-2.png"
IMG_TL_12M = "https://whythelight.com/wp-content/uploads/2025/09/timeline-meditation.png"
IMG_HOLDING = "https://whythelight.com/wp-content/uploads/2025/11/HoldingPatch-clean-cropped-1024x759.png"
IMG_BADGE = "https://whythelight.com/wp-content/uploads/2025/09/90-dayGuarantee.png"

VIMEO_MAIN = "1133694650"
VIMEO_DAVID = "1131910398"
TESTIMONIALS = [
    ("1133177065", "Tendinitis en codo"),
    ("1118432346", "Ojos, digestión, piel"),
    ("1118418371", "Energía y cabello"),
    ("1118429044", "Dedos doloridos"),
    ("1118429946", "Túnel carpiano, vista, piel"),
    ("1118433583", "Escaneado claro"),
    ("1118418475", "Tratamientos con células madre"),
    ("1118426413", "Bienestar general"),
    ("1153060029", "Experiencia cliente"),
    ("1118427670", "Testimonio"),
]

# ─── I18N (nav + common labels) ──────────────────────────────────────────────
I18N = {
    "es": {
        "nav_home": "Inicio",
        "nav_howit": "¿Cómo funciona?",
        "nav_ghk": "GHK-Cu",
        "nav_results": "Resultados",
        "nav_studies": "Estudios",
        "nav_contact": "Contacto",
        "en_soon_title": "English version — coming soon",
        "en_soon_body": "We're working on the English translation. Meanwhile you can contact us directly on WhatsApp and we'll reply in English.",
        "en_soon_cta": "Write us on WhatsApp",
    },
    "en": {
        "nav_home": "Home",
        "nav_howit": "How it works",
        "nav_ghk": "GHK-Cu",
        "nav_results": "Results",
        "nav_studies": "Studies",
        "nav_contact": "Contact",
        "en_soon_title": "English version — coming soon",
        "en_soon_body": "We're working on the English translation. Meanwhile you can contact us directly on WhatsApp and we'll reply in English.",
        "en_soon_cta": "Write us on WhatsApp",
    },
}
t = I18N[lang]

# ─── CSS (theme variables + nav + components) ────────────────────────────────
CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

:root{
  --bg:#000;--bg-2:#0a0a0a;--text:#fff;--muted:#bdbdbd;
  --accent:#d4a94a;--accent-hover:#b8923c;
  --card-bg:#fff;--card-text:#111;--card-sub:#666;
  --nav-bg:rgba(0,0,0,.92);--nav-border:#1a1a1a;
  --footer-text:#8a8a8a;--footer-border:#1a1a1a;
  --tl-title:#1B2A4A;
}

*{box-sizing:border-box;margin:0;padding:0}
html,body,.stApp{background:var(--bg)!important;font-family:'Inter',sans-serif!important;color:var(--text)!important;transition:background .25s,color .25s}
.block-container{padding:0!important;max-width:100%!important}
header[data-testid="stHeader"],#MainMenu,footer,.stDeployButton{display:none!important}
div[data-testid="stSidebarCollapsedControl"],section[data-testid="stSidebar"]{display:none!important}
.stApp > div:first-child > div:first-child > div:first-child > div:first-child{gap:0!important}
a,a:link,a:visited,a:hover,a:active{color:inherit!important;text-decoration:none!important}
.nav-logo,.nav-logo:link,.nav-logo:visited,.nav-logo:hover,.nav-logo:active{color:var(--text)!important;text-decoration:none!important}
.nav-logo span{color:var(--accent)!important}
.nav-links a,.nav-links a:link,.nav-links a:visited{color:var(--text)!important;text-decoration:none!important}
.nav-links a:hover{color:var(--accent)!important}
.nav-links a.active{color:var(--accent)!important}
.nav-links a.nav-contact,.nav-links a.nav-contact:link,.nav-links a.nav-contact:visited{color:#fff!important}
.lang-switch a,.lang-switch a:link,.lang-switch a:visited{color:var(--muted)!important;text-decoration:none!important}
.lang-switch a.active,.lang-switch a:hover{color:var(--accent)!important}

/* ─── Top Nav ─────────────────────────────────────────────────── */
.topnav{position:sticky;top:0;z-index:1000;background:var(--nav-bg);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--nav-border)}
.nav-inner{display:flex;align-items:center;justify-content:space-between;max-width:1400px;margin:0 auto;padding:14px 5%;gap:24px}
.nav-logo{font-weight:900;font-size:21px;color:var(--text);letter-spacing:.6px;white-space:nowrap}
.nav-logo span{color:var(--accent);font-weight:700}
.nav-links{display:flex;gap:22px;align-items:center;flex:1;justify-content:center}
.nav-links a{font-size:13px;font-weight:600;color:var(--text);text-transform:uppercase;letter-spacing:.9px;transition:color .2s;padding:4px 0;white-space:nowrap}
.nav-links a:hover{color:var(--accent)}
.nav-links a.active{color:var(--accent);border-bottom:2px solid var(--accent);padding-bottom:2px}
.nav-contact{background:#25D366;padding:8px 18px!important;border-radius:24px;color:#fff!important;font-weight:700!important;letter-spacing:.5px!important}
.nav-contact:hover{background:#1da851;color:#fff!important}
.nav-tools{display:flex;gap:12px;align-items:center}
.theme-tgl{background:transparent;border:1px solid var(--nav-border);width:38px;height:38px;border-radius:50%;font-size:16px;cursor:pointer;color:var(--text);display:inline-flex;align-items:center;justify-content:center;transition:transform .35s cubic-bezier(.4,.14,.3,1),border-color .2s,background .2s,color .2s;padding:0;line-height:1;user-select:none}
.theme-tgl:hover{border-color:var(--accent)!important;color:var(--accent)!important;transform:rotate(20deg) scale(1.06)}
.theme-tgl:active{transform:scale(.92)}
.lang-switch{display:inline-flex;background:var(--bg-2);border:1px solid var(--nav-border);border-radius:999px;padding:3px;font-size:12px;font-weight:700;align-items:center;gap:0;letter-spacing:.4px}
.lang-switch a{color:var(--muted)!important;padding:5px 12px;border-radius:999px;transition:background .2s,color .2s;line-height:1}
.lang-switch a.active{background:var(--accent);color:#111!important}
.lang-switch a:hover:not(.active){color:var(--text)!important}
.lang-switch .sep{display:none}

@media(max-width:900px){
  .nav-links{display:none}
  .nav-inner{padding:12px 5%;gap:12px}
  .nav-logo{font-size:18px}
  .theme-tgl{width:34px;height:34px;font-size:15px}
}

/* ─── WhatsApp FAB ─────────────────────────────────────────────── */
.wa-float{position:fixed;bottom:25px;right:25px;z-index:9999;width:60px;height:60px;border-radius:50%;
  background:#25D366;display:flex;align-items:center;justify-content:center;
  box-shadow:0 4px 15px rgba(37,211,102,.4);transition:transform .3s}
.wa-float:hover{transform:scale(1.1)}
.wa-float svg{width:35px;height:35px;fill:#fff}

/* ─── Sections ─────────────────────────────────────────────────── */
.sec{padding:70px 8%;width:100%;background:var(--bg);color:var(--text)}
.sec-alt{background:var(--bg-2)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center}
.grid2-rev{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center}

.hero-wrap{padding:100px 8% 90px;text-align:center}
.hero-top{font-size:clamp(26px,4vw,52px);font-weight:800;line-height:1.2;max-width:1100px;margin:0 auto 35px;letter-spacing:.5px;color:var(--text)}
.hero-highlight{color:var(--accent)}
.hero-sub{font-size:clamp(18px,2.2vw,28px);max-width:950px;margin:0 auto;line-height:1.55;color:var(--text);opacity:.85}

.ttl{font-size:clamp(28px,3.6vw,48px);font-weight:800;text-transform:uppercase;line-height:1.15;margin-bottom:20px;letter-spacing:.4px;color:var(--text)}
.ttl-center{text-align:center}
.stxt{font-size:clamp(16px,1.4vw,20px);line-height:1.7;color:var(--text);opacity:.9}
.stxt + .stxt{margin-top:14px}
.stxt-it{font-style:italic}
.stxt-lg{font-size:clamp(18px,1.8vw,24px);line-height:1.6}

.check-list{list-style:none;padding:0;margin:22px 0}
.check-list li{font-size:clamp(16px,1.3vw,19px);padding:6px 0;display:flex;align-items:flex-start;gap:12px;line-height:1.5;color:var(--text)}
.check-list li::before{content:"›";font-size:26px;color:var(--accent);font-weight:bold;line-height:1;min-width:18px}

.benefit-list{list-style:none;padding:0;margin:22px 0}
.benefit-list li{font-size:clamp(16px,1.35vw,19px);padding:8px 0;display:flex;align-items:flex-start;gap:12px;line-height:1.5;color:var(--text)}
.benefit-list li::before{content:"✓";color:#4CAF50;font-weight:800;font-size:20px;min-width:20px}

.img-full{width:100%;height:auto;display:block;border-radius:12px}

.btn{display:inline-block;padding:15px 34px;background:var(--accent);color:#111;border-radius:50px;
  font-weight:800;font-size:14px;text-transform:uppercase;letter-spacing:1.2px;
  transition:all .3s;cursor:pointer;border:none}
.btn:hover{background:var(--accent-hover);transform:translateY(-2px);color:#111}
.btn-outline{background:transparent;color:var(--accent);border:2px solid var(--accent)}
.btn-outline:hover{background:var(--accent);color:#111}
.btn-wa{background:#25D366;color:#fff}.btn-wa:hover{background:#1da851;color:#fff}

.video-wrap{position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:12px;
  box-shadow:0 12px 40px rgba(0,0,0,.25)}
.video-wrap iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}

.step-row{display:flex;align-items:center;gap:20px;margin:22px 0}
.step-num{width:48px;height:48px;border-radius:50%;background:var(--accent);color:#111;
  display:flex;align-items:center;justify-content:center;font-weight:800;font-size:20px;flex-shrink:0}
.step-txt{font-size:clamp(16px,1.4vw,20px);color:var(--text)}

.tl-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:22px;margin-top:35px}
.tl-card{background:var(--card-bg);border-radius:14px;padding:22px 18px;text-align:center;color:var(--card-text);
  box-shadow:0 6px 24px rgba(0,0,0,.12)}
.tl-card img{width:100%;height:auto;border-radius:10px;margin-bottom:14px}
.tl-card h3{font-size:clamp(15px,1.3vw,18px);color:var(--accent);margin-bottom:6px;font-weight:700}
.tl-card h4{font-size:clamp(15px,1.35vw,19px);font-weight:700;margin-bottom:8px;color:var(--tl-title);line-height:1.3}
.tl-card p{font-size:13px;color:var(--card-sub);line-height:1.5}

.test-scroll-wrap{position:relative;padding:0 56px}
.test-scroll{display:flex;gap:22px;overflow-x:auto;padding:24px 4px 32px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.test-scroll::-webkit-scrollbar{display:none}
.test-card{flex:0 0 260px;aspect-ratio:9/16;position:relative;scroll-snap-align:center;border-radius:18px;overflow:hidden;
  box-shadow:0 14px 40px rgba(0,0,0,.45);background:#000;
  transition:transform .35s cubic-bezier(.4,.14,.3,1),box-shadow .35s}
.test-card:hover{transform:translateY(-5px);box-shadow:0 20px 48px rgba(0,0,0,.55)}
.test-card iframe{position:absolute;inset:0;width:100%;height:100%;border:0;display:block}
.test-arrow{position:absolute;top:50%;transform:translateY(-50%);z-index:3;width:44px;height:44px;border-radius:50%;
  background:rgba(255,255,255,.92);color:#111;display:flex;align-items:center;justify-content:center;
  font-size:26px;line-height:1;box-shadow:0 4px 16px rgba(0,0,0,.25);user-select:none;pointer-events:none;font-weight:300}
.test-arrow-left{left:8px}.test-arrow-right{right:8px}
.scroll-hint{text-align:center;color:var(--muted);font-size:14px;font-style:italic;margin-top:8px}

.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:45px;align-items:start}
.about-txt{font-size:clamp(15px,1.3vw,17px);line-height:1.75;color:var(--text);opacity:.9}
.about-txt b{color:var(--text);opacity:1}

.risk-box{text-align:center;max-width:1100px;margin:0 auto}
.risk-img-row{display:flex;gap:25px;align-items:center;justify-content:center;margin-bottom:30px;flex-wrap:wrap}
.risk-img-row img{max-width:340px;width:100%}
.badge-img{max-width:160px;width:100%}

.cta-grid{display:grid;grid-template-columns:1.1fr 1fr;gap:45px;align-items:center}
.cta-btns{display:flex;gap:14px;flex-wrap:wrap;margin-top:25px}

.footer{background:var(--bg);color:var(--footer-text);padding:45px 8%;text-align:center;font-size:13px;line-height:1.75;border-top:1px solid var(--footer-border)}
.footer a{color:var(--footer-text)}
.footer a:hover{color:var(--accent)}

/* ─── Subpage-specific ─────────────────────────────────────────── */
.page-hero{padding:90px 8% 55px;text-align:center}
.page-hero h1{font-size:clamp(32px,4vw,56px);font-weight:800;color:var(--text);letter-spacing:.5px;margin-bottom:18px}
.page-hero .kicker{color:var(--accent);font-size:14px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px}
.page-hero .lede{font-size:clamp(18px,2vw,24px);color:var(--text);opacity:.8;max-width:800px;margin:0 auto;line-height:1.55}

.fact-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:22px;margin:30px 0}
.fact-card{background:var(--bg-2);border-radius:14px;padding:26px 22px;border:1px solid var(--nav-border)}
.fact-card h3{color:var(--accent);font-size:15px;font-weight:800;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}
.fact-card p{font-size:15px;line-height:1.65;color:var(--text);opacity:.85}
.fact-card .big{font-size:clamp(28px,3vw,42px);font-weight:800;color:var(--text);display:block;margin-bottom:6px}

.study-list{max-width:950px;margin:0 auto}
.study-item{background:var(--bg-2);border-radius:14px;padding:28px 28px;margin-bottom:18px;border-left:4px solid var(--accent)}
.study-item h3{font-size:clamp(18px,2vw,24px);color:var(--text);margin-bottom:10px;font-weight:800}
.study-item .org{color:var(--accent);font-weight:700;font-size:14px;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;display:block}
.study-item p{color:var(--text);opacity:.85;line-height:1.7;font-size:15px}

.coming-soon{padding:120px 8%;text-align:center;min-height:60vh;display:flex;flex-direction:column;justify-content:center;align-items:center}
.coming-soon h1{font-size:clamp(32px,4vw,52px);color:var(--text);margin-bottom:18px;font-weight:800}
.coming-soon p{color:var(--text);opacity:.8;max-width:700px;margin:0 auto 30px;font-size:clamp(16px,1.6vw,20px);line-height:1.6}

@media(max-width:900px){
  .grid2,.grid2-rev,.about-grid,.cta-grid{grid-template-columns:1fr;gap:30px}
  .grid2-rev > div:first-child{order:2}
  .sec{padding:50px 6%}
  .hero-wrap,.page-hero{padding:70px 6% 55px}
  .tl-grid{grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}
  .test-card{flex-basis:220px}
  .test-scroll-wrap{padding:0 14px}
  .test-arrow{display:none}
}
</style>"""

# ─── Conditional light-theme override (server-side, no JS) ───────────────────
LIGHT_CSS = """<style>
:root{
  --bg:#fafafa;--bg-2:#f0f0f0;--text:#1a1a1a;--muted:#555;
  --accent:#b8923c;--accent-hover:#8f6e2b;
  --card-bg:#ffffff;--card-text:#111;--card-sub:#555;
  --nav-bg:rgba(255,255,255,.96);--nav-border:#e2e2e2;
  --footer-text:#555;--footer-border:#e2e2e2;
  --tl-title:#1B2A4A;
}
.test-arrow{background:rgba(255,255,255,.96)!important;color:#111!important;box-shadow:0 4px 14px rgba(0,0,0,.12)!important}
.study-item,.fact-card{background:#f5f5f5!important}
.theme-tgl{box-shadow:0 2px 10px rgba(0,0,0,.06)}
</style>"""

# ─── Nav HTML ────────────────────────────────────────────────────────────────
def active(p): return " active" if page == p else ""

NAV = f"""
<nav class="topnav">
  <div class="nav-inner">
    <a href="{LINK_HOME}" target="_self" class="nav-logo">Pauli <span>Wellness</span></a>
    <div class="nav-links">
      <a href="{LINK_HOME}" target="_self" class="{active('home').strip()}">{t['nav_home']}</a>
      <a href="{LINK_GHK}" target="_self" class="{active('ghk').strip()}">{t['nav_ghk']}</a>
      <a href="{LINK_RESULTS}" target="_self" class="{active('resultados').strip()}">{t['nav_results']}</a>
      <a href="{LINK_STUDIES}" target="_self" class="{active('estudios').strip()}">{t['nav_studies']}</a>
      <a href="{WA}" target="_self" class="nav-contact">{t['nav_contact']}</a>
    </div>
    <div class="nav-tools">
      <a href="{LINK_THEME_TOGGLE}" target="_self" class="theme-tgl" aria-label="{theme_title}" title="{theme_title}">{theme_icon}</a>
      <div class="lang-switch">
        <a href="{LINK_LANG_ES}" target="_self" class="{'active' if lang == 'es' else ''}">ES</a>
        <span class="sep">·</span>
        <a href="{LINK_LANG_EN}" target="_self" class="{'active' if lang == 'en' else ''}">EN</a>
      </div>
    </div>
  </div>
</nav>
"""

WA_BTN = f'''<a href="{WA}" target="_self" class="wa-float" aria-label="WhatsApp Pauli">
<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>'''


def footer():
    if lang == "en":
        return '''
<div class="footer">
  <p><b>Important notice:</b> our patches work on the principles of phototherapy.<br>
  They have not been validated under conventional medical standards and are not a substitute for professional medical care.</p>
  <p style="margin-top:12px">*90-day money-back guarantee for Retail and Preferred Customers. 30-day guarantee for Wholesale Brand Partners.</p>
  <p style="margin-top:12px;font-size:11px;max-width:1000px;margin-left:auto;margin-right:auto">Our products are not intended to diagnose, treat, cure or prevent any disease or medical condition. The information on this site is shared for general and informational purposes only.</p>
  <p style="margin-top:22px;font-size:14px;color:var(--muted)">©2026 Pauli Wellness · All rights reserved.</p>
</div>
'''
    return '''
<div class="footer">
  <p><b>Aviso importante:</b> nuestros parches se basan en los principios de la fototerapia.<br>
  Los parches no han sido validados bajo los estándares de la medicina convencional y no sustituyen la atención médica profesional.</p>
  <p style="margin-top:12px">*Garantía de devolución de 90 días para Clientes Minoristas y Preferidos. Garantía de 30 días para Socios de Marca Mayoristas.</p>
  <p style="margin-top:12px;font-size:11px;max-width:1000px;margin-left:auto;margin-right:auto">Nuestros productos no están destinados a diagnosticar, tratar, curar o prevenir enfermedad o condición médica alguna. La información de este sitio se comparte con fines generales e informativos.</p>
  <p style="margin-top:22px;font-size:14px;color:var(--muted)">©2026 Pauli Wellness · Todos los derechos reservados.</p>
</div>
'''


# ─── Render shell ────────────────────────────────────────────────────────────
st.markdown(CSS, unsafe_allow_html=True)
if theme == "light":
    st.markdown(LIGHT_CSS, unsafe_allow_html=True)
st.markdown(NAV, unsafe_allow_html=True)
st.markdown(WA_BTN, unsafe_allow_html=True)

# Persist theme & language across visits via localStorage (runs in iframe
# so <script> actually executes). Reads saved preference and redirects
# parent URL if it's missing the theme param. Writes current URL prefs back
# to localStorage on each load.
import streamlit.components.v1 as _components
_persist_js = """
<script>
(function(){
  try {
    var top = window.parent;
    var url = new URL(top.location.href);
    var qp = url.searchParams;
    var savedTheme = localStorage.getItem('pauli-theme');
    var savedLang = localStorage.getItem('pauli-lang');
    var changed = false;
    if (!qp.get('theme') && savedTheme && (savedTheme === 'light' || savedTheme === 'dark')) {
      qp.set('theme', savedTheme); changed = true;
    }
    if (!qp.get('lang') && savedLang && (savedLang === 'es' || savedLang === 'en')) {
      qp.set('lang', savedLang); changed = true;
    }
    if (changed) {
      top.location.replace(url.toString());
      return;
    }
    // Persist current selection
    var t = qp.get('theme'); if (t) localStorage.setItem('pauli-theme', t);
    var l = qp.get('lang'); if (l) localStorage.setItem('pauli-lang', l);
  } catch(e) { /* privacy mode / cross-origin — fail silently */ }
})();
</script>
"""
_components.html(_persist_js, height=0)


# ─── Page: Home (Spanish) ────────────────────────────────────────────────────
def render_home_es():
    # 1. HERO
    st.markdown(f'''
<section class="sec hero-wrap" id="inicio">
  <h1 class="hero-top">Dos décadas de ciencia. Más de <span class="hero-highlight">200 patentes en todo el mundo</span>. Y una idea simple: usar <span class="hero-highlight">la luz — no químicos</span> — para despertar la producción celular que tu cuerpo ya sabe hacer.</h1>
  <p class="hero-sub">Como devolverle a tu organismo una señal que había olvidado — <i>segura, silenciosa y desde adentro.</i></p>
</section>
''', unsafe_allow_html=True)

    # 2. WHY SO MUCH RESEARCH
    st.markdown(f'''
<section class="sec">
  <div class="grid2">
    <div>
      <h2 class="ttl">¿POR QUÉ TANTA CIENCIA DETRÁS?</h2>
      <p class="stxt">Con los años, las células que se encargan de repararte pierden ritmo.</p>
      <p class="stxt">Menos actividad celular = tu cuerpo sana más despacio y los signos del tiempo aparecen más pronto.</p>
      <p class="stxt stxt-it">Y de a poco… empiezas a notarlo —</p>
      <ul class="check-list">
        <li>Rigidez, molestias y dolores que antes no estaban</li>
        <li>Sueño ligero, recuperación más lenta</li>
        <li>Energía que cae a media tarde</li>
        <li>Piel apagada, cabello que se afina, inflamación que no se va</li>
      </ul>
      <p class="stxt">Y si existiera una forma segura y accesible de encender de nuevo tu propia maquinaria de reparación desde dentro… <b><i>¿no te gustaría probarla?</i></b></p>
    </div>
    <div><img src="{IMG_AGING}" class="img-full" alt="Envejecimiento celular"></div>
  </div>
</section>
''', unsafe_allow_html=True)

    # 3. NOT A PILL (+ main video)
    st.markdown(f'''
<section class="sec" id="como-funciona">
  <div class="grid2">
    <div>
      <h2 class="ttl">NO ES OTRA PASTILLA, CREMA, INYECCIÓN NI MODA.</h2>
      <p class="stxt stxt-lg">Es una categoría completamente distinta.</p>
      <p class="stxt">Un parche del tamaño de una moneda, portable y no transdérmico, con resultados documentados en estudios clínicos y protegidos por patentes en todo el mundo.</p>
      <p class="stxt"><b>Sin fármacos. Sin agujas. Sin suplementos. Sin efectos secundarios conocidos.</b></p>
      <p class="stxt stxt-it">Solo luz — una señal que tu cuerpo ya sabe leer… solo había dejado de escucharla.</p>
    </div>
    <div class="video-wrap">
      <iframe src="https://player.vimeo.com/video/{VIMEO_MAIN}?title=0&byline=0&portrait=0" allow="autoplay;fullscreen" allowfullscreen></iframe>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)

    # 4. 3-MINUTE VIDEO CTA
    st.markdown(f'''
<section class="sec" style="padding-top:20px">
  <div style="max-width:850px;margin:0 auto;text-align:center">
    <img src="{IMG_VIDEO_THUMB}" alt="Video de 3 minutos" style="max-width:420px;width:100%;margin-bottom:10px">
    <p style="font-size:clamp(20px,2.4vw,30px);font-weight:800;color:var(--text);margin-top:15px">Entiende cómo funciona en 3 minutos</p>
    <p style="font-size:clamp(16px,1.6vw,20px);color:var(--accent);font-weight:600;margin-top:6px">Dale play al video</p>
  </div>
</section>
''', unsafe_allow_html=True)

    # 5. WHY LIGHT
    st.markdown(f'''
<section class="sec">
  <div class="grid2">
    <div>
      <h2 class="ttl">¿POR QUÉ LUZ?</h2>
      <p class="stxt stxt-lg">La luz es información. Y tu cuerpo la está escuchando siempre.</p>
      <p class="stxt">Pensalo como acupuntura moderna — pero sin agujas y sin sesiones.</p>
      <p class="stxt">La superficie patentada del parche refleja longitudes de onda precisas hacia tu piel, ayudando a que tu cuerpo eleve naturalmente el <b>GHK-Cu</b>, el péptido de cobre que la literatura científica asocia con la reparación y la renovación celular.</p>
      <p class="stxt">Nada atraviesa la piel. Solo un estímulo limpio que activa lo que ya estaba listo dentro de ti.</p>
      <p class="stxt stxt-it"><b>Tu cuerpo sabe qué hacer. El parche solo le recuerda el camino.</b></p>
    </div>
    <div><img src="{IMG_PATCHES}" class="img-full" alt="Parches LifeWave"></div>
  </div>
</section>
''', unsafe_allow_html=True)

    # 6. NOT QUICK FIXES
    st.markdown(f'''
<section class="sec">
  <div class="grid2-rev">
    <div><img src="{IMG_COUPLE}" class="img-full" alt="Pareja viviendo con vitalidad"></div>
    <div>
      <h2 class="ttl">NO HABLAMOS DE PARCHES SOBRE SÍNTOMAS NI DE ATAJOS RÁPIDOS</h2>
      <p class="stxt">Hablamos de despertarte con energía de verdad — no la que sube y baja con cada café. Piel que acompaña a cómo te sientes por dentro. Un cuerpo que vuelve a responder como cuando todo fluía.</p>
      <ul class="benefit-list">
        <li>Energía sostenida durante todo el día</li>
        <li>Sueño más profundo y mañanas con la cabeza despejada</li>
        <li>Piel con más luminosidad y apoyo natural al colágeno</li>
        <li>Recuperación más ágil — del ejercicio o del día</li>
        <li>Reparación que empieza por dentro y se nota por fuera</li>
        <li>y lo mejor… <b><i>¡volver a reconocerte!</i></b></li>
      </ul>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)

    # 7. GHK-Cu  (button goes to internal /ghk page)
    st.markdown(f'''
<section class="sec">
  <div class="grid2">
    <div>
      <h2 class="ttl">GHK-Cu · EL PÉPTIDO DE COBRE</h2>
      <p class="stxt stxt-lg" style="color:var(--accent);font-weight:700">Tu cuerpo ya lo produce. Solo necesita un pequeño empujón.</p>
      <p class="stxt">Piénsalo como el interruptor maestro que reactiva la capacidad de tu cuerpo para repararse.</p>
      <p class="stxt">Con la edad, los niveles de <b>GHK-Cu</b> bajan — y con ellos, también baja nuestra capacidad natural de reparar, renovar y regenerar.</p>
      <p class="stxt">El parche está diseñado para ayudarte a elevar el GHK-Cu en tu cuerpo, acercándolo a los niveles que tenías en tu juventud.</p>
      <a href="{LINK_GHK}" target="_self" class="btn" style="margin-top:22px">Más sobre el GHK ›</a>
    </div>
    <div><img src="{IMG_MOUNTAIN}" class="img-full" alt="Hombre frente a la montaña"></div>
  </div>
</section>
''', unsafe_allow_html=True)

    # 8. SKEPTICAL + TESTIMONIALS
    test_cards = ""
    for vid_id, label in TESTIMONIALS:
        test_cards += (
            f'<div class="test-card" aria-label="{label}">'
            f'<iframe src="https://player.vimeo.com/video/{vid_id}?title=0&byline=0&portrait=0&dnt=1" '
            f'title="{label}" allow="autoplay;fullscreen;picture-in-picture" allowfullscreen loading="lazy"></iframe>'
            f'</div>'
        )
    test_html = (
        '<div class="test-scroll-wrap">'
        '<span class="test-arrow test-arrow-left" aria-hidden="true">‹</span>'
        f'<div class="test-scroll">{test_cards}</div>'
        '<span class="test-arrow test-arrow-right" aria-hidden="true">›</span>'
        '</div>'
    )

    st.markdown(f'''
<section class="sec" style="text-align:center">
  <h2 class="ttl ttl-center">¿ESCÉPTICO/A? BIEN. NOSOTROS TAMBIÉN LO FUIMOS.</h2>
  <p class="stxt stxt-lg" style="text-align:center">La mayoría de quienes hoy están aquí, empezaron igual. Estas son sus historias.</p>
  {test_html}
  <p class="scroll-hint">(Deslizá para ver más experiencias)</p>
  <div style="margin-top:28px">
    <a href="{LINK_RESULTS}" target="_self" class="btn btn-outline">Ver más experiencias reales ›</a>
  </div>
</section>
''', unsafe_allow_html=True)

    # 9. HOW TO WEAR
    st.markdown(f'''
<section class="sec">
  <div class="grid2">
    <div>
      <h2 class="ttl">CÓMO SE USA</h2>
      <p class="stxt stxt-lg" style="color:var(--accent);font-weight:700;margin-bottom:18px">Despega, pega, listo.</p>
      <div class="step-row"><div class="step-num">1</div><div class="step-txt">Aplícalo sobre piel limpia y seca.</div></div>
      <div class="step-row"><div class="step-num">2</div><div class="step-txt">Déjalo puesto hasta 12 horas; después descansa otras 12.</div></div>
      <div class="step-row"><div class="step-num">3</div><div class="step-txt">Retíralo (si quieres, luego puedes ponerlo sobre tu mascota).</div></div>
      <div class="step-row"><div class="step-num">4</div><div class="step-txt">Al día siguiente, un parche nuevo — y así cada día.</div></div>
      <p class="stxt" style="margin-top:18px">Para mejores resultados, acompaña el parche con <b>buena hidratación</b> a lo largo del día.</p>
    </div>
    <div><img src="{IMG_PATCH_PLACEMENT}" class="img-full" alt="Colocación del parche"></div>
  </div>
</section>
''', unsafe_allow_html=True)

    # 10. TIMELINE
    st.markdown(f'''
<section class="sec" style="text-align:center">
  <h2 class="ttl ttl-center">QUÉ PUEDES ESPERAR CON EL TIEMPO</h2>
  <div class="tl-grid">
    <div class="tl-card">
      <img src="{IMG_TL_DAYS}" alt="Primeros días">
      <h3>En los primeros días</h3>
      <h4>Miles de genes empiezan a ajustar su expresión</h4>
    </div>
    <div class="tl-card">
      <img src="{IMG_TL_4W}" alt="4 semanas">
      <h3>A las 4 semanas</h3>
      <h4>Arranca la reparación celular</h4>
      <p>Tu cuerpo dedica recursos a lo que más necesita, sin que tengas que pensarlo</p>
    </div>
    <div class="tl-card">
      <img src="{IMG_TL_6W}" alt="6 semanas">
      <h3>A las 6 semanas</h3>
      <h4>Cerebro y energía encuentran su equilibrio</h4>
      <p>*Observaciones respaldadas por PSY-TEK Labs y The Center for Biofield Sciences</p>
    </div>
    <div class="tl-card">
      <img src="{IMG_TL_3M}" alt="3-6 meses">
      <h3>Entre 3 y 6 meses</h3>
      <h4>Sube el colágeno</h4>
      <p>La piel gana tersura y la recuperación se acorta</p>
    </div>
    <div class="tl-card">
      <img src="{IMG_TL_12M}" alt="12 meses">
      <h3>A los 12 meses</h3>
      <h4>Ya no es solo cómo te sientes…</h4>
      <p>también se ve y se refleja en cómo vives</p>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)

    # 11. ABOUT
    st.markdown(f'''
<section class="sec">
  <div class="about-grid">
    <div class="video-wrap">
      <iframe src="https://player.vimeo.com/video/{VIMEO_DAVID}?title=0&byline=0&portrait=0" allow="autoplay;fullscreen" allowfullscreen></iframe>
    </div>
    <div>
      <h2 class="ttl">SOBRE LA EMPRESA</h2>
      <h3 style="font-size:clamp(18px,2vw,24px);margin-bottom:18px;color:var(--text)">David Schmidt<br>Fundador, inventor y CEO</h3>
      <p class="about-txt">Desde 2004, LifeWave acompaña a personas en más de cien países a sentirse mejor, verse más jóvenes y vivir con más presencia — con tecnologías de bienestar que potencian la energía y la resiliencia que tu cuerpo ya tiene.</p>
      <p class="about-txt" style="margin-top:14px">A nivel global, David figura hoy como titular de más de <b>200 patentes otorgadas</b> — con varias más en trámite. De ese total, más de setenta corresponden al campo de la ciencia y la tecnología de la regeneración.</p>
      <p class="about-txt" style="margin-top:14px">LifeWave ha recibido varios reconocimientos a lo largo de los años; entre los más recientes, el <b>Premio Biotech Breakthrough 2025</b> en la categoría «Innovación en células madre del año».</p>
      <div style="margin-top:22px"><a href="{LINK_STUDIES}" target="_self" class="btn btn-outline">Patentes y estudios ›</a></div>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)

    # 12. RISK-FREE
    st.markdown(f'''
<section class="sec">
  <div class="risk-box">
    <div class="risk-img-row">
      <img src="{IMG_HOLDING}" alt="Sosteniendo el parche" style="border-radius:14px">
      <img src="{IMG_BADGE}" class="badge-img" alt="Garantía 30/90 días">
    </div>
    <h2 class="ttl ttl-center" style="font-size:clamp(24px,3vw,38px)">Pruébalo con tranquilidad total</h2>
    <p class="stxt stxt-lg" style="margin-top:8px">Sin riesgo durante <b>30/90 días*</b></p>
  </div>
</section>
''', unsafe_allow_html=True)

    # 13. CTA
    st.markdown(f'''
<section class="sec">
  <div class="cta-grid">
    <div>
      <h2 class="ttl">¿TE INTRIGA CÓMO ESTO ENCAJA EN LO QUE YA HACES POR TI?</h2>
      <p class="stxt stxt-lg">No tienes que decidir solo/a.</p>
      <p class="stxt stxt-lg">Escríbele a quien te compartió esta página — estamos aquí para responderte.</p>
      <div class="cta-btns">
        <a href="{WA}" target="_self" class="btn btn-wa">💬 Hablar por WhatsApp</a>
        <a href="{WA}" target="_self" class="btn">Paquetes y precios ›</a>
      </div>
    </div>
    <div><img src="{IMG_KITCHEN}" class="img-full" alt="Pareja feliz en la cocina"></div>
  </div>
</section>
''', unsafe_allow_html=True)


# ─── Page: GHK-Cu (Spanish) ──────────────────────────────────────────────────
def render_ghk_es():
    st.markdown(f'''
<section class="sec page-hero">
  <div class="kicker">Péptido de cobre</div>
  <h1>GHK-Cu · el péptido que tu cuerpo ya conoce</h1>
  <p class="lede">Un tripéptido natural de tu organismo, enlazado a cobre, que la ciencia relaciona con la reparación de tejidos. Aquí te contamos qué es, por qué importa con la edad, y cómo el parche ayuda a elevarlo.</p>
</section>

<section class="sec">
  <div style="max-width:900px;margin:0 auto">
    <h2 class="ttl">¿QUÉ ES EL GHK-Cu?</h2>
    <p class="stxt">Es un pequeño péptido formado por tres aminoácidos — glicina, histidina y lisina — unidos a un átomo de cobre. Circula de forma natural en tu organismo, y la investigación publicada desde los años setenta lo asocia con procesos de regeneración, cicatrización y renovación celular.</p>
    <p class="stxt">El GHK-Cu fue descrito por primera vez en 1973 por el Dr. Loren Pickart, quien notó que el suero de personas jóvenes aplicado sobre tejido hepático envejecido parecía ayudar a su recuperación. Ese hallazgo abrió una línea de investigación que sigue activa hoy.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div style="max-width:1100px;margin:0 auto">
    <h2 class="ttl ttl-center">POR QUÉ IMPORTA A PARTIR DE LOS 30</h2>
    <p class="stxt ttl-center" style="text-align:center;max-width:750px;margin:0 auto 20px">Los niveles de GHK-Cu en sangre no son constantes a lo largo de la vida. Con los años, bajan — y con ellos, la capacidad natural de tu cuerpo para regenerarse.</p>
    <div class="fact-grid">
      <div class="fact-card">
        <span class="big">~200 ng/mL</span>
        <h3>A los 20 años</h3>
        <p>Nivel de referencia reportado en la literatura para adultos jóvenes sanos.</p>
      </div>
      <div class="fact-card">
        <span class="big">~80 ng/mL</span>
        <h3>A los 60 años</h3>
        <p>Caída de aproximadamente un 60% respecto a los niveles de juventud.</p>
      </div>
      <div class="fact-card">
        <span class="big">-60%</span>
        <h3>Capacidad regenerativa</h3>
        <p>La baja del GHK-Cu coincide con una reducción visible de la recuperación y reparación de tejidos.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div style="max-width:950px;margin:0 auto">
    <h2 class="ttl">QUÉ DICE LA INVESTIGACIÓN</h2>
    <p class="stxt">En publicaciones científicas revisadas por pares, el GHK-Cu ha sido observado en relación con:</p>
    <ul class="check-list">
      <li>Estimulación de fibroblastos y síntesis de colágeno</li>
      <li>Apoyo en la cicatrización y cierre de heridas</li>
      <li>Actividad antioxidante y modulación de la inflamación</li>
      <li>Señalización en procesos de regeneración nerviosa</li>
      <li>Expresión de genes asociados a reparación de tejidos</li>
    </ul>
    <p class="stxt">La literatura es amplia — si te interesa profundizar, buscá «GHK-Cu» en PubMed y vas a encontrar cientos de estudios publicados.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="grid2">
    <div>
      <h2 class="ttl">Y EL PARCHE · ¿DÓNDE ENCAJA?</h2>
      <p class="stxt">El parche <b>no contiene GHK-Cu</b>. Tampoco lo libera al interior del cuerpo.</p>
      <p class="stxt">Su superficie patentada refleja hacia tu piel determinadas longitudes de onda de luz. Esa señal — según la evidencia presentada por LifeWave — estimula al propio organismo para que eleve los niveles de GHK-Cu que produce de forma natural.</p>
      <p class="stxt"><b>Sin fármacos. Sin inyecciones. Sin absorción a través de la piel.</b> Solo luz.</p>
      <p class="stxt stxt-it">Piénsalo como una acupuntura moderna, sin agujas, que le recuerda a tu cuerpo un proceso que siempre supo hacer.</p>
    </div>
    <div><img src="{IMG_PATCHES}" class="img-full" alt="Parches"></div>
  </div>
</section>

<section class="sec">
  <div style="text-align:center;max-width:800px;margin:0 auto">
    <h2 class="ttl ttl-center" style="font-size:clamp(24px,3vw,38px)">¿Querés ver cómo esto cambia la vida de personas reales?</h2>
    <div class="cta-btns" style="justify-content:center">
      <a href="{LINK_RESULTS}" target="_self" class="btn">Ver resultados reales ›</a>
      <a href="{LINK_STUDIES}" target="_self" class="btn btn-outline">Ver estudios y patentes ›</a>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)


# ─── Page: Resultados (Spanish) ──────────────────────────────────────────────
def render_resultados_es():
    cards = ""
    for vid_id, label in TESTIMONIALS:
        cards += (
            f'<div class="test-card" aria-label="{label}">'
            f'<iframe src="https://player.vimeo.com/video/{vid_id}?title=0&byline=0&portrait=0&dnt=1" '
            f'title="{label}" allow="autoplay;fullscreen;picture-in-picture" allowfullscreen loading="lazy"></iframe>'
            f'</div>'
        )
    grid_html = (
        '<div class="test-scroll-wrap">'
        '<span class="test-arrow test-arrow-left" aria-hidden="true">‹</span>'
        f'<div class="test-scroll">{cards}</div>'
        '<span class="test-arrow test-arrow-right" aria-hidden="true">›</span>'
        '</div>'
    )

    st.markdown(f'''
<section class="sec page-hero">
  <div class="kicker">Experiencias reales</div>
  <h1>Resultados que cuentan las personas</h1>
  <p class="lede">Cada testimonio acá es de alguien que probó los parches y quiso compartir lo que le pasó. Nada guionado, nada pagado. Mirá, escuchá, y sacá tus propias conclusiones.</p>
</section>

<section class="sec sec-alt">
  <div style="max-width:1200px;margin:0 auto">
    <h2 class="ttl ttl-center">Testimonios en video</h2>
    <p class="stxt ttl-center" style="text-align:center;max-width:750px;margin:0 auto 30px">Distintas personas, distintos motivos para empezar. Lo que comparten es que cada una notó algo que vale la pena contar.</p>
    {grid_html}
  </div>
</section>

<section class="sec">
  <div style="max-width:900px;margin:0 auto">
    <h2 class="ttl">QUÉ TIPO DE CAMBIOS SE CUENTAN CON MÁS FRECUENCIA</h2>
    <p class="stxt">Las historias son diversas, pero hay patrones que se repiten entre quienes usan los parches de forma constante durante semanas o meses:</p>
    <ul class="benefit-list">
      <li><b>Dolor y rigidez:</b> molestias que estaban hace tiempo empiezan a ceder, y la recuperación después del ejercicio se acorta.</li>
      <li><b>Sueño:</b> más profundidad, menos interrupciones, despertar con la cabeza despejada.</li>
      <li><b>Energía y ánimo:</b> una estabilidad distinta — sin los picos y caídas del café.</li>
      <li><b>Piel y cabello:</b> textura más uniforme, más luminosidad, menos caída de pelo.</li>
      <li><b>Digestión:</b> procesos más parejos y menos inflamación tras las comidas.</li>
      <li><b>Visión y concentración:</b> algunas personas notan mejor enfoque visual y claridad mental.</li>
    </ul>
    <p class="stxt stxt-it" style="margin-top:22px">Importante: cada cuerpo es distinto. Lo que le funciona a una persona puede expresarse diferente en otra, tanto en qué mejora como en cuánto tarda en notarse. Estas son experiencias individuales — no son promesas médicas.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div style="text-align:center;max-width:800px;margin:0 auto">
    <h2 class="ttl ttl-center">¿Querés probarlo?</h2>
    <p class="stxt" style="text-align:center">Lo más sencillo es escribirnos — te contamos qué parche corresponde a lo que buscás, cómo pedirlo, y cómo funciona la garantía.</p>
    <div class="cta-btns" style="justify-content:center;margin-top:20px">
      <a href="{WA}" target="_self" class="btn btn-wa">💬 Hablar por WhatsApp</a>
      <a href="{LINK_GHK}" target="_self" class="btn btn-outline">¿Qué es el GHK-Cu? ›</a>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)


# ─── Page: Estudios (Spanish) ────────────────────────────────────────────────
STUDIES = [
    ("PSY-TEK Subtle Energy Sciences Laboratory · California, EE.UU.",
     "Análisis biofotónicos y de respuesta energética",
     "Mediciones de cambios en la respuesta biofotónica de sujetos antes y después del uso de los parches, utilizando técnicas de imagen y análisis del campo biofísico. Observaron variaciones consistentes en marcadores energéticos."),
    ("The Center for Biofield Sciences · India",
     "Mediciones de respuesta biofísica",
     "Estudios sobre variables fisiológicas y subjetivas en usuarios de los parches, con protocolos aplicados por investigadores independientes, centrados en bienestar percibido y marcadores de equilibrio energético."),
    ("Estudios de seguridad dérmica",
     "Hipoalergenicidad y compatibilidad con la piel",
     "Pruebas realizadas por laboratorios independientes de certificación dermatológica para evaluar la seguridad del adhesivo y del material del parche en pieles sensibles. Los parches utilizan adhesivo acrílico hipoalergénico de grado médico de 3M."),
    ("Medición del GHK-Cu",
     "Evaluación pre/post del péptido de cobre",
     "Estudios piloto que analizaron los niveles de GHK-Cu en usuarios antes y después del uso continuado del parche X39, con el objetivo de documentar la elevación del péptido asociada a la exposición a longitudes de onda específicas."),
    ("Regulación génica",
     "Cambios en la expresión de genes asociados a reparación",
     "Observaciones sobre la expresión de miles de genes relacionados con reparación tisular y respuesta celular en sujetos tras el uso del parche durante períodos cortos, documentados en informes técnicos de la empresa."),
    ("Recuperación en deporte",
     "Observaciones en atletas y personas activas",
     "Reportes sobre recuperación después del entrenamiento y tolerancia al esfuerzo en deportistas que usan los parches, incluyendo tiempos de cicatrización de micro-lesiones y retorno a la actividad."),
]


def render_estudios_es():
    # Hero
    st.markdown(
        '<section class="sec page-hero">'
        '<div class="kicker">Ciencia y patentes</div>'
        '<h1>Estudios y patentes</h1>'
        '<p class="lede">A lo largo de más de dos décadas, LifeWave ha invertido en investigación independiente y en protección intelectual de su tecnología. Estos son los puntos más relevantes.</p>'
        '</section>',
        unsafe_allow_html=True,
    )

    # Numbers / facts
    st.markdown(
        '<section class="sec"><div style="max-width:1100px;margin:0 auto">'
        '<h2 class="ttl ttl-center">EN NÚMEROS</h2>'
        '<div class="fact-grid">'
        '<div class="fact-card"><span class="big">+200</span><h3>Patentes otorgadas</h3><p>A nivel global, con varias adicionales en trámite.</p></div>'
        '<div class="fact-card"><span class="big">+70</span><h3>Patentes en regeneración</h3><p>Directamente ligadas a ciencia y tecnología de regeneración celular.</p></div>'
        '<div class="fact-card"><span class="big">20+</span><h3>Años de desarrollo</h3><p>Investigación continua desde la fundación de la empresa en 2004.</p></div>'
        '<div class="fact-card"><span class="big">2025</span><h3>Biotech Breakthrough Award</h3><p>Categoría «Innovación en células madre del año».</p></div>'
        '</div></div></section>',
        unsafe_allow_html=True,
    )

    # Independent research — built as one single-line string to avoid markdown
    # code-block trap (4-space indent after blank line → interpreted as code).
    items_html = "".join(
        f'<div class="study-item"><span class="org">{org}</span><h3>{title}</h3><p>{desc}</p></div>'
        for (org, title, desc) in STUDIES
    )
    st.markdown(
        '<section class="sec sec-alt"><div class="study-list">'
        '<h2 class="ttl ttl-center">INVESTIGACIÓN INDEPENDIENTE</h2>'
        '<p class="stxt ttl-center" style="text-align:center;max-width:750px;margin:0 auto 30px">'
        'Distintos laboratorios y centros de investigación han evaluado la tecnología de los parches. A continuación, una selección.'
        '</p>'
        + items_html +
        '</div></section>',
        unsafe_allow_html=True,
    )

    # Recognitions
    st.markdown(
        '<section class="sec"><div style="max-width:950px;margin:0 auto">'
        '<h2 class="ttl ttl-center">RECONOCIMIENTOS</h2>'
        '<ul class="check-list" style="max-width:750px;margin:0 auto">'
        '<li><b>Premio Biotech Breakthrough 2025</b> — «Innovación en células madre del año»</li>'
        '<li>Múltiples premios a la innovación en tecnología de bienestar en ediciones previas</li>'
        '<li>Presencia en más de cien países con red de distribuidores y socios de marca</li>'
        '<li>David Schmidt, fundador, es autor e inventor titular de más de 200 patentes a nivel global</li>'
        '</ul></div></section>',
        unsafe_allow_html=True,
    )

    # CTA
    st.markdown(
        f'<section class="sec sec-alt"><div style="text-align:center;max-width:800px;margin:0 auto">'
        f'<h2 class="ttl ttl-center" style="font-size:clamp(24px,3vw,38px)">¿Querés entender cómo esto te aplica a ti?</h2>'
        f'<p class="stxt" style="text-align:center">Escribinos y te contamos qué hay detrás, con calma y con datos.</p>'
        f'<div class="cta-btns" style="justify-content:center;margin-top:20px">'
        f'<a href="{WA}" target="_self" class="btn btn-wa">💬 Hablar por WhatsApp</a>'
        f'<a href="{LINK_GHK}" target="_self" class="btn btn-outline">Más sobre el GHK-Cu ›</a>'
        f'</div></div></section>',
        unsafe_allow_html=True,
    )


# ─── English testimonial labels ──────────────────────────────────────────────
TESTIMONIALS_EN = [
    ("1133177065", "Elbow tendinitis"),
    ("1118432346", "Eyes, digestion, skin"),
    ("1118418371", "Energy and hair"),
    ("1118429044", "Sore fingers"),
    ("1118429946", "Carpal tunnel, sight, skin"),
    ("1118433583", "Clear scan"),
    ("1118418475", "Stem-cell treatments"),
    ("1118426413", "Overall wellbeing"),
    ("1153060029", "Customer experience"),
    ("1118427670", "Testimonial"),
]


# ─── Page: Home (English) ────────────────────────────────────────────────────
def render_home_en():
    # 1. HERO
    st.markdown(
        '<section class="sec hero-wrap" id="home">'
        '<h1 class="hero-top">Two decades of science. More than <span class="hero-highlight">200 patents worldwide</span>. And one simple idea: use <span class="hero-highlight">light — not chemicals</span> — to wake up the cellular repair your body already knows how to do.</h1>'
        '<p class="hero-sub">Like returning a signal your body had forgotten — <i>safe, silent, and from the inside.</i></p>'
        '</section>',
        unsafe_allow_html=True,
    )

    # 2. WHY SO MUCH RESEARCH
    st.markdown(
        f'<section class="sec"><div class="grid2">'
        f'<div>'
        f'<h2 class="ttl">WHY SO MUCH SCIENCE BEHIND IT?</h2>'
        f'<p class="stxt">As years pass, the cells in charge of repairing you slow their rhythm.</p>'
        f'<p class="stxt">Less cellular activity = your body heals more slowly and the marks of time start showing up earlier.</p>'
        f'<p class="stxt stxt-it">And little by little, you start to notice —</p>'
        f'<ul class="check-list">'
        f'<li>Stiffness, aches and pains that weren\'t there before</li>'
        f'<li>Lighter sleep, slower recovery</li>'
        f'<li>Energy that dips mid-afternoon</li>'
        f'<li>Dull skin, thinning hair, inflammation that won\'t fade</li>'
        f'</ul>'
        f'<p class="stxt">And if there were a safe, accessible way to switch your own repair machinery back on from within… <b><i>wouldn\'t you want to try it?</i></b></p>'
        f'</div>'
        f'<div><img src="{IMG_AGING}" class="img-full" alt="Cellular aging"></div>'
        f'</div></section>',
        unsafe_allow_html=True,
    )

    # 3. NOT A PILL (+ main video)
    st.markdown(
        f'<section class="sec" id="how-it-works"><div class="grid2">'
        f'<div>'
        f'<h2 class="ttl">NOT ANOTHER PILL, CREAM, SHOT OR TREND.</h2>'
        f'<p class="stxt stxt-lg">It\'s a whole different category.</p>'
        f'<p class="stxt">A coin-sized, portable, non-transdermic patch with results documented in clinical studies and protected by patents around the world.</p>'
        f'<p class="stxt"><b>No drugs. No needles. No supplements. No known side effects.</b></p>'
        f'<p class="stxt stxt-it">Just light — a signal your body already knows how to read… it had only stopped listening.</p>'
        f'</div>'
        f'<div class="video-wrap"><iframe src="https://player.vimeo.com/video/{VIMEO_MAIN}?title=0&byline=0&portrait=0" allow="autoplay;fullscreen" allowfullscreen></iframe></div>'
        f'</div></section>',
        unsafe_allow_html=True,
    )

    # 4. 3-MINUTE VIDEO CTA
    st.markdown(
        f'<section class="sec" style="padding-top:20px">'
        f'<div style="max-width:850px;margin:0 auto;text-align:center">'
        f'<img src="{IMG_VIDEO_THUMB}" alt="3-minute video" style="max-width:420px;width:100%;margin-bottom:10px">'
        f'<p style="font-size:clamp(20px,2.4vw,30px);font-weight:800;color:var(--text);margin-top:15px">Understand how it works in 3 minutes</p>'
        f'<p style="font-size:clamp(16px,1.6vw,20px);color:var(--accent);font-weight:600;margin-top:6px">Press play on the video</p>'
        f'</div></section>',
        unsafe_allow_html=True,
    )

    # 5. WHY LIGHT
    st.markdown(
        f'<section class="sec"><div class="grid2">'
        f'<div>'
        f'<h2 class="ttl">WHY LIGHT?</h2>'
        f'<p class="stxt stxt-lg">Light is information. And your body is always listening.</p>'
        f'<p class="stxt">Think of it as modern acupuncture — no needles, no sessions.</p>'
        f'<p class="stxt">The patented surface of the patch reflects precise wavelengths back to your skin, helping your body naturally raise <b>GHK-Cu</b>, the copper peptide the scientific literature links to cellular repair and renewal.</p>'
        f'<p class="stxt">Nothing crosses the skin. Just a clean stimulus that switches on what was already ready inside you.</p>'
        f'<p class="stxt stxt-it"><b>Your body knows what to do. The patch just reminds it of the path.</b></p>'
        f'</div>'
        f'<div><img src="{IMG_PATCHES}" class="img-full" alt="LifeWave patches"></div>'
        f'</div></section>',
        unsafe_allow_html=True,
    )

    # 6. NOT QUICK FIXES
    st.markdown(
        f'<section class="sec"><div class="grid2-rev">'
        f'<div><img src="{IMG_COUPLE}" class="img-full" alt="Couple living with vitality"></div>'
        f'<div>'
        f'<h2 class="ttl">WE\'RE NOT TALKING ABOUT PATCHES FOR SYMPTOMS OR QUICK SHORTCUTS</h2>'
        f'<p class="stxt">We\'re talking about waking up with real energy — not the kind that spikes and crashes with every coffee. Skin that matches how you feel inside. A body that responds the way it used to when everything flowed.</p>'
        f'<ul class="benefit-list">'
        f'<li>Sustained energy throughout the day</li>'
        f'<li>Deeper sleep and clear mornings</li>'
        f'<li>Skin with more glow and natural collagen support</li>'
        f'<li>Faster recovery — from exercise or the day</li>'
        f'<li>Repair that starts inside and shows on the outside</li>'
        f'<li>and best of all… <b><i>recognizing yourself again!</i></b></li>'
        f'</ul>'
        f'</div></div></section>',
        unsafe_allow_html=True,
    )

    # 7. GHK-Cu
    st.markdown(
        f'<section class="sec"><div class="grid2">'
        f'<div>'
        f'<h2 class="ttl">GHK-Cu · THE COPPER PEPTIDE</h2>'
        f'<p class="stxt stxt-lg" style="color:var(--accent);font-weight:700">Your body already makes it. It just needs a small nudge.</p>'
        f'<p class="stxt">Think of it as the master switch that reactivates your body\'s ability to repair itself.</p>'
        f'<p class="stxt">With age, <b>GHK-Cu</b> levels drop — and with them, our natural capacity to repair, renew and regenerate.</p>'
        f'<p class="stxt">The patch is designed to help you raise GHK-Cu in your body, closer to the levels you had in your youth.</p>'
        f'<a href="{LINK_GHK}" target="_self" class="btn" style="margin-top:22px">More about GHK ›</a>'
        f'</div>'
        f'<div><img src="{IMG_MOUNTAIN}" class="img-full" alt="Man in front of the mountain"></div>'
        f'</div></section>',
        unsafe_allow_html=True,
    )

    # 8. SKEPTICAL + TESTIMONIALS
    test_cards = ""
    for vid_id, label in TESTIMONIALS_EN:
        test_cards += (
            f'<div class="test-card" aria-label="{label}">'
            f'<iframe src="https://player.vimeo.com/video/{vid_id}?title=0&byline=0&portrait=0&dnt=1" '
            f'title="{label}" allow="autoplay;fullscreen;picture-in-picture" allowfullscreen loading="lazy"></iframe>'
            f'</div>'
        )
    test_html = (
        '<div class="test-scroll-wrap">'
        '<span class="test-arrow test-arrow-left" aria-hidden="true">‹</span>'
        f'<div class="test-scroll">{test_cards}</div>'
        '<span class="test-arrow test-arrow-right" aria-hidden="true">›</span>'
        '</div>'
    )
    st.markdown(
        f'<section class="sec" style="text-align:center">'
        f'<h2 class="ttl ttl-center">SKEPTICAL? GOOD. SO WERE WE.</h2>'
        f'<p class="stxt stxt-lg" style="text-align:center">Most of the people here today started the same way. These are their stories.</p>'
        f'{test_html}'
        f'<p class="scroll-hint">(Swipe to see more experiences)</p>'
        f'<div style="margin-top:28px"><a href="{LINK_RESULTS}" target="_self" class="btn btn-outline">See more real experiences ›</a></div>'
        f'</section>',
        unsafe_allow_html=True,
    )

    # 9. HOW TO WEAR
    st.markdown(
        f'<section class="sec"><div class="grid2">'
        f'<div>'
        f'<h2 class="ttl">HOW TO USE IT</h2>'
        f'<p class="stxt stxt-lg" style="color:var(--accent);font-weight:700;margin-bottom:18px">Peel, stick, done.</p>'
        f'<div class="step-row"><div class="step-num">1</div><div class="step-txt">Apply on clean, dry skin.</div></div>'
        f'<div class="step-row"><div class="step-num">2</div><div class="step-txt">Leave it on up to 12 hours; then rest for another 12.</div></div>'
        f'<div class="step-row"><div class="step-num">3</div><div class="step-txt">Remove it (you can then use it on your pet if you like).</div></div>'
        f'<div class="step-row"><div class="step-num">4</div><div class="step-txt">A fresh patch the next day — and every day after.</div></div>'
        f'<p class="stxt" style="margin-top:18px">For best results, pair the patch with <b>good hydration</b> throughout the day.</p>'
        f'</div>'
        f'<div><img src="{IMG_PATCH_PLACEMENT}" class="img-full" alt="Patch placement"></div>'
        f'</div></section>',
        unsafe_allow_html=True,
    )

    # 10. TIMELINE
    st.markdown(
        f'<section class="sec" style="text-align:center">'
        f'<h2 class="ttl ttl-center">WHAT TO EXPECT OVER TIME</h2>'
        f'<div class="tl-grid">'
        f'<div class="tl-card"><img src="{IMG_TL_DAYS}" alt="First days"><h3>In the first days</h3><h4>Thousands of genes begin adjusting their expression</h4></div>'
        f'<div class="tl-card"><img src="{IMG_TL_4W}" alt="4 weeks"><h3>At 4 weeks</h3><h4>Cellular repair starts</h4><p>Your body puts resources where they\'re needed most, without you having to think about it</p></div>'
        f'<div class="tl-card"><img src="{IMG_TL_6W}" alt="6 weeks"><h3>At 6 weeks</h3><h4>Brain and energy find their balance</h4><p>*Observations backed by PSY-TEK Labs and The Center for Biofield Sciences</p></div>'
        f'<div class="tl-card"><img src="{IMG_TL_3M}" alt="3-6 months"><h3>Between 3 and 6 months</h3><h4>Collagen rises</h4><p>Skin gains firmness and recovery shortens</p></div>'
        f'<div class="tl-card"><img src="{IMG_TL_12M}" alt="12 months"><h3>At 12 months</h3><h4>It\'s no longer just how you feel…</h4><p>it also shows in how you live</p></div>'
        f'</div></section>',
        unsafe_allow_html=True,
    )

    # 11. ABOUT
    st.markdown(
        f'<section class="sec"><div class="about-grid">'
        f'<div class="video-wrap"><iframe src="https://player.vimeo.com/video/{VIMEO_DAVID}?title=0&byline=0&portrait=0" allow="autoplay;fullscreen" allowfullscreen></iframe></div>'
        f'<div>'
        f'<h2 class="ttl">ABOUT THE COMPANY</h2>'
        f'<h3 style="font-size:clamp(18px,2vw,24px);margin-bottom:18px;color:var(--text)">David Schmidt<br>Founder, inventor and CEO</h3>'
        f'<p class="about-txt">Since 2004, LifeWave has supported people in over one hundred countries to feel better, look younger and live more present — with wellness technologies that amplify the energy and resilience your body already has.</p>'
        f'<p class="about-txt" style="margin-top:14px">Globally, David holds more than <b>200 granted patents</b> — with several more pending. Of those, over seventy are in the field of regeneration science and technology.</p>'
        f'<p class="about-txt" style="margin-top:14px">LifeWave has received multiple awards over the years; among the most recent, the <b>2025 Biotech Breakthrough Award</b> in the "Stem Cell Innovation of the Year" category.</p>'
        f'<div style="margin-top:22px"><a href="{LINK_STUDIES}" target="_self" class="btn btn-outline">Patents and studies ›</a></div>'
        f'</div></div></section>',
        unsafe_allow_html=True,
    )

    # 12. RISK-FREE
    st.markdown(
        f'<section class="sec"><div class="risk-box">'
        f'<div class="risk-img-row">'
        f'<img src="{IMG_HOLDING}" alt="Holding the patch" style="border-radius:14px">'
        f'<img src="{IMG_BADGE}" class="badge-img" alt="30/90-day guarantee">'
        f'</div>'
        f'<h2 class="ttl ttl-center" style="font-size:clamp(24px,3vw,38px)">Try it with total peace of mind</h2>'
        f'<p class="stxt stxt-lg" style="margin-top:8px">Risk-free for <b>30/90 days*</b></p>'
        f'</div></section>',
        unsafe_allow_html=True,
    )

    # 13. CTA
    st.markdown(
        f'<section class="sec"><div class="cta-grid">'
        f'<div>'
        f'<h2 class="ttl">CURIOUS HOW THIS FITS INTO WHAT YOU ALREADY DO FOR YOURSELF?</h2>'
        f'<p class="stxt stxt-lg">You don\'t have to decide alone.</p>'
        f'<p class="stxt stxt-lg">Write to whoever shared this page with you — we\'re here to answer.</p>'
        f'<div class="cta-btns">'
        f'<a href="{WA}" target="_self" class="btn btn-wa">💬 Chat on WhatsApp</a>'
        f'<a href="{WA}" target="_self" class="btn">Packages and pricing ›</a>'
        f'</div>'
        f'</div>'
        f'<div><img src="{IMG_KITCHEN}" class="img-full" alt="Happy couple in the kitchen"></div>'
        f'</div></section>',
        unsafe_allow_html=True,
    )


# ─── Page: GHK-Cu (English) ──────────────────────────────────────────────────
def render_ghk_en():
    st.markdown(
        '<section class="sec page-hero">'
        '<div class="kicker">Copper peptide</div>'
        '<h1>GHK-Cu · the peptide your body already knows</h1>'
        '<p class="lede">A natural tripeptide made by your body, bound to copper, which science links to tissue repair. Here\'s what it is, why it matters with age, and how the patch helps raise it.</p>'
        '</section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<section class="sec"><div style="max-width:900px;margin:0 auto">'
        '<h2 class="ttl">WHAT IS GHK-Cu?</h2>'
        '<p class="stxt">It\'s a small peptide made of three amino acids — glycine, histidine and lysine — bound to a copper atom. It circulates naturally in your body, and research published since the 1970s links it to processes of regeneration, wound healing and cellular renewal.</p>'
        '<p class="stxt">GHK-Cu was first described in 1973 by Dr. Loren Pickart, who noticed that serum from younger people applied to aged liver tissue seemed to help it recover. That finding opened a line of research still active today.</p>'
        '</div></section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<section class="sec sec-alt"><div style="max-width:1100px;margin:0 auto">'
        '<h2 class="ttl ttl-center">WHY IT MATTERS AFTER 30</h2>'
        '<p class="stxt ttl-center" style="text-align:center;max-width:750px;margin:0 auto 20px">GHK-Cu levels in the blood are not constant through life. Over time, they drop — and with them, your body\'s natural capacity to regenerate.</p>'
        '<div class="fact-grid">'
        '<div class="fact-card"><span class="big">~200 ng/mL</span><h3>At age 20</h3><p>Reference range reported in the literature for healthy young adults.</p></div>'
        '<div class="fact-card"><span class="big">~80 ng/mL</span><h3>At age 60</h3><p>A drop of roughly 60% compared with youth levels.</p></div>'
        '<div class="fact-card"><span class="big">-60%</span><h3>Regenerative capacity</h3><p>The drop in GHK-Cu coincides with a visible reduction in tissue recovery and repair.</p></div>'
        '</div></div></section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<section class="sec"><div style="max-width:950px;margin:0 auto">'
        '<h2 class="ttl">WHAT THE RESEARCH SAYS</h2>'
        '<p class="stxt">In peer-reviewed scientific publications, GHK-Cu has been observed in connection with:</p>'
        '<ul class="check-list">'
        '<li>Fibroblast stimulation and collagen synthesis</li>'
        '<li>Support in wound healing and closure</li>'
        '<li>Antioxidant activity and inflammation modulation</li>'
        '<li>Signaling in nerve regeneration processes</li>'
        '<li>Expression of genes linked to tissue repair</li>'
        '</ul>'
        '<p class="stxt">The literature is broad — if you want to dig deeper, search "GHK-Cu" on PubMed and you\'ll find hundreds of published studies.</p>'
        '</div></section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<section class="sec sec-alt"><div class="grid2">'
        f'<div>'
        f'<h2 class="ttl">AND THE PATCH · WHERE DOES IT FIT?</h2>'
        f'<p class="stxt">The patch <b>does not contain GHK-Cu</b>. It doesn\'t release it into the body either.</p>'
        f'<p class="stxt">Its patented surface reflects specific wavelengths of light back to your skin. That signal — according to the evidence presented by LifeWave — stimulates the body itself to raise the levels of GHK-Cu it naturally produces.</p>'
        f'<p class="stxt"><b>No drugs. No injections. No absorption through the skin.</b> Just light.</p>'
        f'<p class="stxt stxt-it">Think of it as modern acupuncture, without needles, reminding your body of a process it has always known.</p>'
        f'</div>'
        f'<div><img src="{IMG_PATCHES}" class="img-full" alt="Patches"></div>'
        f'</div></section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<section class="sec"><div style="text-align:center;max-width:800px;margin:0 auto">'
        f'<h2 class="ttl ttl-center" style="font-size:clamp(24px,3vw,38px)">Want to see how this changes real people\'s lives?</h2>'
        f'<div class="cta-btns" style="justify-content:center">'
        f'<a href="{LINK_RESULTS}" target="_self" class="btn">See real results ›</a>'
        f'<a href="{LINK_STUDIES}" target="_self" class="btn btn-outline">See studies and patents ›</a>'
        f'</div></div></section>',
        unsafe_allow_html=True,
    )


# ─── Page: Resultados (English) ──────────────────────────────────────────────
def render_resultados_en():
    cards = ""
    for vid_id, label in TESTIMONIALS_EN:
        cards += (
            f'<div class="test-card" aria-label="{label}">'
            f'<iframe src="https://player.vimeo.com/video/{vid_id}?title=0&byline=0&portrait=0&dnt=1" '
            f'title="{label}" allow="autoplay;fullscreen;picture-in-picture" allowfullscreen loading="lazy"></iframe>'
            f'</div>'
        )
    grid_html = (
        '<div class="test-scroll-wrap">'
        '<span class="test-arrow test-arrow-left" aria-hidden="true">‹</span>'
        f'<div class="test-scroll">{cards}</div>'
        '<span class="test-arrow test-arrow-right" aria-hidden="true">›</span>'
        '</div>'
    )
    st.markdown(
        '<section class="sec page-hero">'
        '<div class="kicker">Real experiences</div>'
        '<h1>Results people share</h1>'
        '<p class="lede">Every testimonial here is from someone who tried the patches and wanted to share what happened. Nothing scripted, nothing paid. Watch, listen, and draw your own conclusions.</p>'
        '</section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<section class="sec sec-alt"><div style="max-width:1200px;margin:0 auto">'
        f'<h2 class="ttl ttl-center">Video testimonials</h2>'
        f'<p class="stxt ttl-center" style="text-align:center;max-width:750px;margin:0 auto 30px">Different people, different reasons to start. What they share is that each one noticed something worth telling.</p>'
        f'{grid_html}'
        f'</div></section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<section class="sec"><div style="max-width:900px;margin:0 auto">'
        '<h2 class="ttl">THE CHANGES PEOPLE REPORT MOST OFTEN</h2>'
        '<p class="stxt">Stories are diverse, but patterns repeat among people who use the patches consistently for weeks or months:</p>'
        '<ul class="benefit-list">'
        '<li><b>Pain and stiffness:</b> long-standing discomfort starts to ease, and post-exercise recovery gets shorter.</li>'
        '<li><b>Sleep:</b> deeper, fewer interruptions, waking up with a clearer head.</li>'
        '<li><b>Energy and mood:</b> a different kind of stability — without the coffee spikes and crashes.</li>'
        '<li><b>Skin and hair:</b> more even texture, more glow, less hair fall.</li>'
        '<li><b>Digestion:</b> smoother processes and less inflammation after meals.</li>'
        '<li><b>Vision and focus:</b> some people notice better visual focus and mental clarity.</li>'
        '</ul>'
        '<p class="stxt stxt-it" style="margin-top:22px">Important: every body is different. What works for one person can show up differently in another — both in what improves and in how long it takes. These are individual experiences — not medical promises.</p>'
        '</div></section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<section class="sec sec-alt"><div style="text-align:center;max-width:800px;margin:0 auto">'
        f'<h2 class="ttl ttl-center">Want to try it?</h2>'
        f'<p class="stxt" style="text-align:center">The easiest thing is to message us — we\'ll tell you which patch fits what you\'re looking for, how to order it, and how the guarantee works.</p>'
        f'<div class="cta-btns" style="justify-content:center;margin-top:20px">'
        f'<a href="{WA}" target="_self" class="btn btn-wa">💬 Chat on WhatsApp</a>'
        f'<a href="{LINK_GHK}" target="_self" class="btn btn-outline">What is GHK-Cu? ›</a>'
        f'</div></div></section>',
        unsafe_allow_html=True,
    )


# ─── Page: Estudios (English) ────────────────────────────────────────────────
STUDIES_EN = [
    ("PSY-TEK Subtle Energy Sciences Laboratory · California, USA",
     "Biophotonic and energy-response analyses",
     "Measurements of changes in subjects' biophotonic response before and after using the patches, using imaging and biophysical field analysis techniques. They observed consistent variations in energy markers."),
    ("The Center for Biofield Sciences · India",
     "Biophysical response measurements",
     "Studies on physiological and subjective variables in patch users, with protocols applied by independent researchers, focused on perceived wellbeing and markers of energetic balance."),
    ("Dermal safety studies",
     "Hypoallergenicity and skin compatibility",
     "Testing by independent dermatological certification labs to evaluate the safety of the adhesive and the patch material on sensitive skin. The patches use medical-grade hypoallergenic 3M acrylic adhesive."),
    ("GHK-Cu measurement",
     "Pre/post evaluation of the copper peptide",
     "Pilot studies analyzing GHK-Cu levels in users before and after continued use of the X39 patch, aiming to document the peptide increase associated with exposure to specific wavelengths."),
    ("Gene regulation",
     "Changes in expression of repair-related genes",
     "Observations on the expression of thousands of genes linked to tissue repair and cellular response in subjects after short-term use of the patch, documented in company technical reports."),
    ("Sports recovery",
     "Observations in athletes and active people",
     "Reports on post-training recovery and effort tolerance in athletes who use the patches, including healing times for micro-injuries and return to activity."),
]


def render_estudios_en():
    st.markdown(
        '<section class="sec page-hero">'
        '<div class="kicker">Science and patents</div>'
        '<h1>Studies and patents</h1>'
        '<p class="lede">Over more than two decades, LifeWave has invested in independent research and in intellectual protection of its technology. Here are the most relevant points.</p>'
        '</section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<section class="sec"><div style="max-width:1100px;margin:0 auto">'
        '<h2 class="ttl ttl-center">BY THE NUMBERS</h2>'
        '<div class="fact-grid">'
        '<div class="fact-card"><span class="big">+200</span><h3>Granted patents</h3><p>Globally, with several more pending.</p></div>'
        '<div class="fact-card"><span class="big">+70</span><h3>Patents in regeneration</h3><p>Directly tied to regeneration science and technology.</p></div>'
        '<div class="fact-card"><span class="big">20+</span><h3>Years of development</h3><p>Continuous research since the company was founded in 2004.</p></div>'
        '<div class="fact-card"><span class="big">2025</span><h3>Biotech Breakthrough Award</h3><p>"Stem Cell Innovation of the Year" category.</p></div>'
        '</div></div></section>',
        unsafe_allow_html=True,
    )
    items_html = "".join(
        f'<div class="study-item"><span class="org">{org}</span><h3>{title}</h3><p>{desc}</p></div>'
        for (org, title, desc) in STUDIES_EN
    )
    st.markdown(
        '<section class="sec sec-alt"><div class="study-list">'
        '<h2 class="ttl ttl-center">INDEPENDENT RESEARCH</h2>'
        '<p class="stxt ttl-center" style="text-align:center;max-width:750px;margin:0 auto 30px">'
        'Different labs and research centers have evaluated the patch technology. Below is a selection.'
        '</p>'
        + items_html +
        '</div></section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<section class="sec"><div style="max-width:950px;margin:0 auto">'
        '<h2 class="ttl ttl-center">RECOGNITIONS</h2>'
        '<ul class="check-list" style="max-width:750px;margin:0 auto">'
        '<li><b>2025 Biotech Breakthrough Award</b> — "Stem Cell Innovation of the Year"</li>'
        '<li>Multiple awards for innovation in wellness technology in previous editions</li>'
        '<li>Presence in more than one hundred countries with a network of distributors and brand partners</li>'
        '<li>David Schmidt, founder, is author and inventor of more than 200 patents worldwide</li>'
        '</ul></div></section>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<section class="sec sec-alt"><div style="text-align:center;max-width:800px;margin:0 auto">'
        f'<h2 class="ttl ttl-center" style="font-size:clamp(24px,3vw,38px)">Want to understand how this applies to you?</h2>'
        f'<p class="stxt" style="text-align:center">Message us and we\'ll walk you through it, calmly and with data.</p>'
        f'<div class="cta-btns" style="justify-content:center;margin-top:20px">'
        f'<a href="{WA}" target="_self" class="btn btn-wa">💬 Chat on WhatsApp</a>'
        f'<a href="{LINK_GHK}" target="_self" class="btn btn-outline">More about GHK-Cu ›</a>'
        f'</div></div></section>',
        unsafe_allow_html=True,
    )


# ─── Router ──────────────────────────────────────────────────────────────────
if lang == "en":
    if page == "home":
        render_home_en()
    elif page == "ghk":
        render_ghk_en()
    elif page == "resultados":
        render_resultados_en()
    elif page == "estudios":
        render_estudios_en()
    else:
        render_home_en()
else:
    if page == "home":
        render_home_es()
    elif page == "ghk":
        render_ghk_es()
    elif page == "resultados":
        render_resultados_es()
    elif page == "estudios":
        render_estudios_es()
    else:
        render_home_es()

st.markdown(footer(), unsafe_allow_html=True)
