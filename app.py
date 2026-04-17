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

# ─── Routing & language from query params ────────────────────────────────────
qp = st.query_params
page = qp.get("page", "home")
if page not in ("home", "ghk", "resultados", "estudios"):
    page = "home"
lang = qp.get("lang", "es")
if lang not in ("es", "en"):
    lang = "es"

# ─── Config ──────────────────────────────────────────────────────────────────
WA_NUM = "593939890499"
WA_TXT = "Hola%20Pauli!%20Vi%20tu%20pagina%20y%20me%20gustaria%20saber%20mas%20sobre%20los%20parches%20LifeWave"
WA = f"https://wa.me/{WA_NUM}?text={WA_TXT}"

# Internal page routes (replaces prior whythelight.com links)
LINK_HOME = f"?page=home&lang={lang}"
LINK_GHK = f"?page=ghk&lang={lang}"
LINK_RESULTS = f"?page=resultados&lang={lang}"
LINK_STUDIES = f"?page=estudios&lang={lang}"

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
html[data-light]{
  --bg:#fafafa;--bg-2:#f0f0f0;--text:#1a1a1a;--muted:#555;
  --accent:#b8923c;--accent-hover:#8f6e2b;
  --card-bg:#ffffff;--card-text:#111;--card-sub:#555;
  --nav-bg:rgba(255,255,255,.96);--nav-border:#e2e2e2;
  --footer-text:#555;--footer-border:#e2e2e2;
  --tl-title:#1B2A4A;
}

*{box-sizing:border-box;margin:0;padding:0}
html,body,.stApp{background:var(--bg)!important;font-family:'Inter',sans-serif!important;color:var(--text)!important;transition:background .25s,color .25s}
.block-container{padding:0!important;max-width:100%!important}
header[data-testid="stHeader"],#MainMenu,footer,.stDeployButton{display:none!important}
div[data-testid="stSidebarCollapsedControl"],section[data-testid="stSidebar"]{display:none!important}
.stApp > div:first-child > div:first-child > div:first-child > div:first-child{gap:0!important}
a{color:inherit;text-decoration:none}

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
.nav-tools{display:flex;gap:14px;align-items:center}
.theme-tgl{background:transparent;border:1px solid var(--nav-border);width:38px;height:38px;border-radius:50%;font-size:17px;cursor:pointer;color:var(--text);display:flex;align-items:center;justify-content:center;transition:all .2s;padding:0}
.theme-tgl:hover{border-color:var(--accent);color:var(--accent)}
.lang-switch{display:flex;gap:6px;font-size:13px;font-weight:700;align-items:center}
.lang-switch a{color:var(--muted);padding:4px 6px;border-radius:4px;transition:all .2s}
.lang-switch a.active{color:var(--accent)}
.lang-switch a:hover{color:var(--accent)}
.lang-switch .sep{color:var(--muted);opacity:.5}

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

.test-scroll{display:flex;gap:18px;overflow-x:auto;padding:20px 0 28px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch}
.test-scroll::-webkit-scrollbar{height:8px}
.test-scroll::-webkit-scrollbar-thumb{background:var(--accent);border-radius:4px}
.test-card{flex:0 0 300px;scroll-snap-align:start;background:var(--bg-2);border-radius:12px;overflow:hidden;box-shadow:0 6px 24px rgba(0,0,0,.35)}
.test-card .video-wrap{border-radius:0;box-shadow:none}
.test-label{padding:12px;text-align:center;font-weight:600;font-size:14px;background:var(--bg-2);color:var(--text)}
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

.test-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px;margin-top:10px}
.test-grid .test-card{flex:none;background:var(--bg-2)}

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
  .test-card{flex-basis:260px}
}
</style>"""

# ─── Nav HTML + theme toggle JS ──────────────────────────────────────────────
def active(p): return " active" if page == p else ""

NAV = f"""
<nav class="topnav">
  <div class="nav-inner">
    <a href="{LINK_HOME}" target="_top" class="nav-logo">Pauli <span>Wellness</span></a>
    <div class="nav-links">
      <a href="{LINK_HOME}" target="_top" class="{active('home').strip()}">{t['nav_home']}</a>
      <a href="{LINK_GHK}" target="_top" class="{active('ghk').strip()}">{t['nav_ghk']}</a>
      <a href="{LINK_RESULTS}" target="_top" class="{active('resultados').strip()}">{t['nav_results']}</a>
      <a href="{LINK_STUDIES}" target="_top" class="{active('estudios').strip()}">{t['nav_studies']}</a>
      <a href="{WA}" target="_blank" class="nav-contact">{t['nav_contact']}</a>
    </div>
    <div class="nav-tools">
      <button class="theme-tgl" onclick="__pauliTheme()" aria-label="Toggle theme" id="themeTgl">🌙</button>
      <div class="lang-switch">
        <a href="?page={page}&lang=es" target="_top" class="{'active' if lang == 'es' else ''}">ES</a>
        <span class="sep">·</span>
        <a href="?page={page}&lang=en" target="_top" class="{'active' if lang == 'en' else ''}">EN</a>
      </div>
    </div>
  </div>
</nav>
<script>
(function(){{
  try {{
    const saved = localStorage.getItem('pauli-theme') || 'dark';
    if (saved === 'light') document.documentElement.setAttribute('data-light', '');
  }} catch(e) {{}}
  function applyIcon() {{
    const isLight = document.documentElement.hasAttribute('data-light');
    document.querySelectorAll('.theme-tgl').forEach(b => {{ b.textContent = isLight ? '☀️' : '🌙'; }});
  }}
  window.__pauliTheme = function() {{
    const isLight = document.documentElement.hasAttribute('data-light');
    if (isLight) {{
      document.documentElement.removeAttribute('data-light');
      try {{ localStorage.setItem('pauli-theme', 'dark'); }} catch(e) {{}}
    }} else {{
      document.documentElement.setAttribute('data-light', '');
      try {{ localStorage.setItem('pauli-theme', 'light'); }} catch(e) {{}}
    }}
    applyIcon();
  }};
  applyIcon();
  document.addEventListener('DOMContentLoaded', applyIcon);
}})();
</script>
"""

WA_BTN = f'''<a href="{WA}" target="_blank" class="wa-float" aria-label="WhatsApp Pauli">
<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>'''


def footer():
    return f'''
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
st.markdown(NAV, unsafe_allow_html=True)
st.markdown(WA_BTN, unsafe_allow_html=True)


# ─── Page: EN placeholder ────────────────────────────────────────────────────
def render_en_placeholder():
    st.markdown(f'''
<section class="sec coming-soon">
  <h1>{t["en_soon_title"]}</h1>
  <p>{t["en_soon_body"]}</p>
  <a href="{WA}" target="_blank" class="btn btn-wa">💬 {t["en_soon_cta"]}</a>
  <p style="margin-top:32px"><a href="?page={page}&lang=es" target="_top" style="color:var(--accent);font-weight:700">← Ver versión en español</a></p>
</section>
''', unsafe_allow_html=True)


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
      <a href="{LINK_GHK}" target="_top" class="btn" style="margin-top:22px">Más sobre el GHK ›</a>
    </div>
    <div><img src="{IMG_MOUNTAIN}" class="img-full" alt="Hombre frente a la montaña"></div>
  </div>
</section>
''', unsafe_allow_html=True)

    # 8. SKEPTICAL + TESTIMONIALS
    test_html = '<div class="test-scroll">'
    for vid_id, label in TESTIMONIALS:
        test_html += f'''<div class="test-card">
<div class="video-wrap"><iframe src="https://player.vimeo.com/video/{vid_id}?title=0&byline=0&portrait=0" allow="fullscreen" allowfullscreen loading="lazy"></iframe></div>
<div class="test-label">{label}</div></div>'''
    test_html += '</div>'

    st.markdown(f'''
<section class="sec" style="text-align:center">
  <h2 class="ttl ttl-center">¿ESCÉPTICO/A? BIEN. NOSOTROS TAMBIÉN LO FUIMOS.</h2>
  <p class="stxt stxt-lg" style="text-align:center">La mayoría de quienes hoy están aquí, empezaron igual. Estas son sus historias.</p>
  {test_html}
  <p class="scroll-hint">(Deslizá para ver más experiencias)</p>
  <div style="margin-top:28px">
    <a href="{LINK_RESULTS}" target="_top" class="btn btn-outline">Ver más experiencias reales ›</a>
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
      <div style="margin-top:22px"><a href="{LINK_STUDIES}" target="_top" class="btn btn-outline">Patentes y estudios ›</a></div>
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
        <a href="{WA}" target="_blank" class="btn btn-wa">💬 Hablar por WhatsApp</a>
        <a href="{WA}" target="_blank" class="btn">Paquetes y precios ›</a>
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
      <a href="{LINK_RESULTS}" target="_top" class="btn">Ver resultados reales ›</a>
      <a href="{LINK_STUDIES}" target="_top" class="btn btn-outline">Ver estudios y patentes ›</a>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)


# ─── Page: Resultados (Spanish) ──────────────────────────────────────────────
def render_resultados_es():
    grid_html = '<div class="test-grid">'
    for vid_id, label in TESTIMONIALS:
        grid_html += f'''<div class="test-card">
<div class="video-wrap"><iframe src="https://player.vimeo.com/video/{vid_id}?title=0&byline=0&portrait=0" allow="fullscreen" allowfullscreen loading="lazy"></iframe></div>
<div class="test-label">{label}</div></div>'''
    grid_html += '</div>'

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
      <a href="{WA}" target="_blank" class="btn btn-wa">💬 Hablar por WhatsApp</a>
      <a href="{LINK_GHK}" target="_top" class="btn btn-outline">¿Qué es el GHK-Cu? ›</a>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)


# ─── Page: Estudios (Spanish) ────────────────────────────────────────────────
def render_estudios_es():
    st.markdown(f'''
<section class="sec page-hero">
  <div class="kicker">Ciencia y patentes</div>
  <h1>Estudios y patentes</h1>
  <p class="lede">A lo largo de más de dos décadas, LifeWave ha invertido en investigación independiente y en protección intelectual de su tecnología. Estos son los puntos más relevantes.</p>
</section>

<section class="sec">
  <div style="max-width:1100px;margin:0 auto">
    <h2 class="ttl ttl-center">EN NÚMEROS</h2>
    <div class="fact-grid">
      <div class="fact-card">
        <span class="big">+200</span>
        <h3>Patentes otorgadas</h3>
        <p>A nivel global, con varias adicionales en trámite.</p>
      </div>
      <div class="fact-card">
        <span class="big">+70</span>
        <h3>Patentes en regeneración</h3>
        <p>Directamente ligadas a ciencia y tecnología de regeneración celular.</p>
      </div>
      <div class="fact-card">
        <span class="big">20+</span>
        <h3>Años de desarrollo</h3>
        <p>Investigación continua desde la fundación de la empresa en 2004.</p>
      </div>
      <div class="fact-card">
        <span class="big">2025</span>
        <h3>Biotech Breakthrough Award</h3>
        <p>Categoría «Innovación en células madre del año».</p>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="study-list">
    <h2 class="ttl ttl-center">INVESTIGACIÓN INDEPENDIENTE</h2>
    <p class="stxt ttl-center" style="text-align:center;max-width:750px;margin:0 auto 30px">Distintos laboratorios y centros de investigación han evaluado la tecnología de los parches. A continuación, una selección.</p>

    <div class="study-item">
      <span class="org">PSY-TEK Subtle Energy Sciences Laboratory · California, EE.UU.</span>
      <h3>Análisis biofotónicos y de respuesta energética</h3>
      <p>Mediciones de cambios en la respuesta biofotónica de sujetos antes y después del uso de los parches, utilizando técnicas de imagen y análisis del campo biofísico. Observaron variaciones consistentes en marcadores energéticos.</p>
    </div>

    <div class="study-item">
      <span class="org">The Center for Biofield Sciences · India</span>
      <h3>Mediciones de respuesta biofísica</h3>
      <p>Estudios sobre variables fisiológicas y subjetivas en usuarios de los parches, con protocolos aplicados por investigadores independientes, centrados en bienestar percibido y marcadores de equilibrio energético.</p>
    </div>

    <div class="study-item">
      <span class="org">Estudios de seguridad dérmica</span>
      <h3>Hipoalergenicidad y compatibilidad con la piel</h3>
      <p>Pruebas realizadas por laboratorios independientes de certificación dermatológica para evaluar la seguridad del adhesivo y del material del parche en pieles sensibles. Los parches utilizan adhesivo acrílico hipoalergénico de grado médico de 3M.</p>
    </div>

    <div class="study-item">
      <span class="org">Medición del GHK-Cu</span>
      <h3>Evaluación pre/post del péptido de cobre</h3>
      <p>Estudios piloto que analizaron los niveles de GHK-Cu en usuarios antes y después del uso continuado del parche X39, con el objetivo de documentar la elevación del péptido asociada a la exposición a longitudes de onda específicas.</p>
    </div>

    <div class="study-item">
      <span class="org">Regulación génica</span>
      <h3>Cambios en la expresión de genes asociados a reparación</h3>
      <p>Observaciones sobre la expresión de miles de genes relacionados con reparación tisular y respuesta celular en sujetos tras el uso del parche durante períodos cortos, documentados en informes técnicos de la empresa.</p>
    </div>

    <div class="study-item">
      <span class="org">Recuperación en deporte</span>
      <h3>Observaciones en atletas y personas activas</h3>
      <p>Reportes sobre recuperación después del entrenamiento y tolerancia al esfuerzo en deportistas que usan los parches, incluyendo tiempos de cicatrización de micro-lesiones y retorno a la actividad.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div style="max-width:950px;margin:0 auto">
    <h2 class="ttl ttl-center">RECONOCIMIENTOS</h2>
    <ul class="check-list" style="max-width:750px;margin:0 auto">
      <li><b>Premio Biotech Breakthrough 2025</b> — «Innovación en células madre del año»</li>
      <li>Múltiples premios a la innovación en tecnología de bienestar en ediciones previas</li>
      <li>Presencia en más de cien países con red de distribuidores y socios de marca</li>
      <li>David Schmidt, fundador, es autor e inventor titular de más de 200 patentes a nivel global</li>
    </ul>
  </div>
</section>

<section class="sec sec-alt">
  <div style="text-align:center;max-width:800px;margin:0 auto">
    <h2 class="ttl ttl-center" style="font-size:clamp(24px,3vw,38px)">¿Querés entender cómo esto te aplica a ti?</h2>
    <p class="stxt" style="text-align:center">Escribinos y te contamos qué hay detrás, con calma y con datos.</p>
    <div class="cta-btns" style="justify-content:center;margin-top:20px">
      <a href="{WA}" target="_blank" class="btn btn-wa">💬 Hablar por WhatsApp</a>
      <a href="{LINK_GHK}" target="_top" class="btn btn-outline">Más sobre el GHK-Cu ›</a>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)


# ─── Router ──────────────────────────────────────────────────────────────────
if lang == "en":
    render_en_placeholder()
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
