"""Pauli Wellness - LifeWave Landing Page (ES)
1:1 parallel of whythelight.com/es/ — same photos, videos, sections, link targets.
Spanish copy is Pauli Wellness's own adaptation.
"""
import streamlit as st

st.set_page_config(
    page_title="¿Por qué la luz? | Pauli Wellness",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Config ──────────────────────────────────────────────────────────────────
WA_NUM = "593939890499"
WA_TXT = "Hola%20Pauli!%20Vi%20tu%20pagina%20y%20me%20gustaria%20saber%20mas%20sobre%20los%20parches%20LifeWave"
WA = f"https://wa.me/{WA_NUM}?text={WA_TXT}"

# External pages on whythelight.com (Pauli doesn't yet host these locally)
LINK_GHK = "https://whythelight.com/es/ghk-cu/"
LINK_RESULTS = "https://whythelight.com/es/resultados-reales/"
LINK_STUDIES = "https://whythelight.com/es/estudios/"
LINK_PRICING = WA  # Pauli routes pricing inquiries to WhatsApp

# Image URLs — same assets used by whythelight.com
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

# Vimeo IDs (from whythelight.com/es/)
VIMEO_MAIN = "1133694650"       # 3-minute "how it works"
VIMEO_DAVID = "1131910398"      # David Schmidt / About the company
# 8 testimonial videos, ordered as they appear in the reference carousel
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

# ─── CSS ─────────────────────────────────────────────────────────────────────
CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
html,body,.stApp{background:#000!important;font-family:'Inter',sans-serif!important;color:#fff!important}
.block-container{padding:0!important;max-width:100%!important}
header[data-testid="stHeader"],#MainMenu,footer,.stDeployButton{display:none!important}
div[data-testid="stSidebarCollapsedControl"],section[data-testid="stSidebar"]{display:none!important}
.stApp > div:first-child > div:first-child > div:first-child > div:first-child{gap:0!important}
a{color:inherit;text-decoration:none}
.wa-float{position:fixed;bottom:25px;right:25px;z-index:9999;width:60px;height:60px;border-radius:50%;
  background:#25D366;display:flex;align-items:center;justify-content:center;
  box-shadow:0 4px 15px rgba(37,211,102,.4);transition:transform .3s}
.wa-float:hover{transform:scale(1.1)}
.wa-float svg{width:35px;height:35px;fill:#fff}

.sec{padding:70px 8%;width:100%}
.sec-black{background:#000;color:#fff}
.sec-white{background:#fff;color:#111}
.sec-light{background:#f5f5f5;color:#111}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center}
.grid2-rev{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center}

.hero-wrap{padding:120px 8% 100px;text-align:center}
.hero-top{font-size:clamp(26px,4vw,52px);font-weight:800;line-height:1.2;max-width:1100px;margin:0 auto 35px;letter-spacing:.5px}
.hero-highlight{color:#d4a94a}
.hero-sub{font-size:clamp(18px,2.2vw,28px);max-width:950px;margin:0 auto;line-height:1.55;color:#e8e8e8}
.hero-tag{font-size:clamp(16px,1.8vw,22px);color:#bdbdbd;font-style:italic;max-width:800px;margin:25px auto 0;line-height:1.55}

.ttl{font-size:clamp(28px,3.6vw,48px);font-weight:800;text-transform:uppercase;line-height:1.15;margin-bottom:20px;letter-spacing:.4px}
.ttl-center{text-align:center}
.stxt{font-size:clamp(16px,1.4vw,20px);line-height:1.7;color:inherit}
.stxt + .stxt{margin-top:14px}
.stxt-it{font-style:italic}
.stxt-lg{font-size:clamp(18px,1.8vw,24px);line-height:1.6}

.check-list{list-style:none;padding:0;margin:22px 0}
.check-list li{font-size:clamp(16px,1.3vw,19px);padding:6px 0;display:flex;align-items:flex-start;gap:12px;line-height:1.5}
.check-list li::before{content:"›";font-size:26px;color:#d4a94a;font-weight:bold;line-height:1;min-width:18px}

.benefit-list{list-style:none;padding:0;margin:22px 0}
.benefit-list li{font-size:clamp(16px,1.35vw,19px);padding:8px 0;display:flex;align-items:flex-start;gap:12px;line-height:1.5}
.benefit-list li::before{content:"✓";color:#4CAF50;font-weight:800;font-size:20px;min-width:20px}

.img-full{width:100%;height:auto;display:block;border-radius:12px}

.btn{display:inline-block;padding:15px 34px;background:#d4a94a;color:#111;border-radius:50px;
  font-weight:800;font-size:14px;text-transform:uppercase;letter-spacing:1.2px;
  transition:all .3s;cursor:pointer;border:none}
.btn:hover{background:#b8923c;transform:translateY(-2px);color:#111}
.btn-outline{background:transparent;color:#d4a94a;border:2px solid #d4a94a}
.btn-outline:hover{background:#d4a94a;color:#111}
.btn-wa{background:#25D366;color:#fff}.btn-wa:hover{background:#1da851;color:#fff}

.video-wrap{position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:12px;
  box-shadow:0 12px 40px rgba(0,0,0,.25)}
.video-wrap iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}

.step-row{display:flex;align-items:center;gap:20px;margin:22px 0}
.step-num{width:48px;height:48px;border-radius:50%;background:#d4a94a;color:#111;
  display:flex;align-items:center;justify-content:center;font-weight:800;font-size:20px;flex-shrink:0}
.step-txt{font-size:clamp(16px,1.4vw,20px);color:#fff}

.tl-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:22px;margin-top:35px}
.tl-card{background:#fff;border-radius:14px;padding:22px 18px;text-align:center;color:#111;
  box-shadow:0 6px 24px rgba(0,0,0,.08)}
.tl-card img{width:100%;height:auto;border-radius:10px;margin-bottom:14px}
.tl-card h3{font-size:clamp(15px,1.3vw,18px);color:#d4a94a;margin-bottom:6px;font-weight:700}
.tl-card h4{font-size:clamp(15px,1.35vw,19px);font-weight:700;margin-bottom:8px;color:#1B2A4A;line-height:1.3}
.tl-card p{font-size:13px;color:#666;line-height:1.5}

.test-scroll{display:flex;gap:18px;overflow-x:auto;padding:20px 0 28px;scroll-snap-type:x mandatory;
  -webkit-overflow-scrolling:touch}
.test-scroll::-webkit-scrollbar{height:8px}
.test-scroll::-webkit-scrollbar-thumb{background:#d4a94a;border-radius:4px}
.test-card{flex:0 0 300px;scroll-snap-align:start;background:#111;border-radius:12px;overflow:hidden;
  box-shadow:0 6px 24px rgba(0,0,0,.35)}
.test-card .video-wrap{border-radius:0;box-shadow:none}
.test-label{padding:12px;text-align:center;font-weight:600;font-size:14px;background:#111;color:#fff}
.scroll-hint{text-align:center;color:#bbb;font-size:14px;font-style:italic;margin-top:8px}

.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:45px;align-items:start}
.about-txt{font-size:clamp(15px,1.3vw,17px);line-height:1.75;color:#e8e8e8}
.about-txt b{color:#fff}

.risk-box{text-align:center;max-width:1100px;margin:0 auto}
.risk-img-row{display:flex;gap:25px;align-items:center;justify-content:center;margin-bottom:30px;flex-wrap:wrap}
.risk-img-row img{max-width:340px;width:100%}
.badge-img{max-width:160px;width:100%}

.cta-grid{display:grid;grid-template-columns:1.1fr 1fr;gap:45px;align-items:center}
.cta-btns{display:flex;gap:14px;flex-wrap:wrap;margin-top:25px}

.footer{background:#000;color:#8a8a8a;padding:45px 8%;text-align:center;font-size:13px;line-height:1.75;
  border-top:1px solid #1a1a1a}
.footer .lang{margin-top:22px;display:flex;gap:18px;justify-content:center;flex-wrap:wrap;font-size:13px}
.footer .lang a{color:#8a8a8a}.footer .lang a:hover{color:#d4a94a}

@media(max-width:900px){
  .grid2,.grid2-rev,.about-grid,.cta-grid{grid-template-columns:1fr;gap:30px}
  .grid2-rev > div:first-child{order:2}
  .sec{padding:50px 6%}
  .hero-wrap{padding:80px 6% 70px}
  .tl-grid{grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}
  .test-card{flex-basis:260px}
}
</style>"""

WA_BTN = f'''<a href="{WA}" target="_blank" class="wa-float" aria-label="WhatsApp Pauli">
<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>'''

# ─── Render ──────────────────────────────────────────────────────────────────
st.markdown(CSS, unsafe_allow_html=True)
st.markdown(WA_BTN, unsafe_allow_html=True)

# 1. HERO
st.markdown(f'''
<section class="sec sec-black hero-wrap">
  <h1 class="hero-top">Tras <span class="hero-highlight">10 años de investigación con células madre</span> y más de <span class="hero-highlight">200 patentes mundiales</span>… descubrimos una manera de usar la luz, no químicos, para activar la propia producción celular de tu cuerpo.</h1>
  <p class="hero-sub">Es como encender el interruptor de reparación de tu propio cuerpo — <i>con seguridad, sin esfuerzo y desde dentro.</i></p>
</section>
''', unsafe_allow_html=True)

# 2. WHY ALL THE RESEARCH
st.markdown(f'''
<section class="sec sec-black">
  <div class="grid2">
    <div>
      <h2 class="ttl">¿POR QUÉ TANTA INVESTIGACIÓN?</h2>
      <p class="stxt">A medida que envejecemos, las células reparadoras naturales de nuestro organismo se ralentizan.</p>
      <p class="stxt">Menos células activas significa que tu cuerpo se cura más lentamente y muestra signos de envejecimiento más rápido.</p>
      <p class="stxt stxt-it">Y… empiezas a sentirlo —</p>
      <ul class="check-list">
        <li>Dolores y rigidez</li>
        <li>Sueño insuficiente y recuperación lenta</li>
        <li>Baja energía y concentración</li>
        <li>Líneas de expresión, pérdida de cabello e inflamación</li>
      </ul>
      <p class="stxt">Si pudieras reparar y regenerar de dentro hacia fuera, de forma segura y asequible… <b><i>¿no te gustaría?</i></b></p>
    </div>
    <div><img src="{IMG_AGING}" class="img-full" alt="Envejecimiento celular"></div>
  </div>
</section>
''', unsafe_allow_html=True)

# 3. NOT A BETTER PILL  (video on the right)
st.markdown(f'''
<section class="sec sec-black">
  <div class="grid2">
    <div>
      <h2 class="ttl">ESTO NO ES UNA MEJOR PASTILLA, CREMA, INYECCIÓN O TENDENCIA.</h2>
      <p class="stxt stxt-lg">Es una categoría completamente nueva.</p>
      <p class="stxt">Un parche portátil, no transdérmico, con resultados reales respaldados por ciencia, estudios clínicos y patentes mundiales.</p>
      <p class="stxt"><b>Sin medicamentos. Sin inyecciones. Sin conjeturas. Sin efectos secundarios.</b></p>
      <p class="stxt stxt-it">Solo luz — enviando una señal que tu cuerpo olvidó… hasta ahora.</p>
    </div>
    <div class="video-wrap">
      <iframe src="https://player.vimeo.com/video/{VIMEO_MAIN}?title=0&byline=0&portrait=0" allow="autoplay;fullscreen" allowfullscreen></iframe>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)

# 4. 3-MINUTE VIDEO CTA
st.markdown(f'''
<section class="sec sec-black" style="padding-top:20px">
  <div style="max-width:850px;margin:0 auto;text-align:center">
    <img src="{IMG_VIDEO_THUMB}" alt="Video de 3 minutos" style="max-width:420px;width:100%;margin-bottom:10px">
    <p style="font-size:clamp(20px,2.4vw,30px);font-weight:800;color:#fff;margin-top:15px">Mira cómo funciona el parche</p>
    <p style="font-size:clamp(16px,1.6vw,20px);color:#d4a94a;font-weight:600;margin-top:6px">Video de 3 minutos</p>
  </div>
</section>
''', unsafe_allow_html=True)

# 5. WHY LIGHT
st.markdown(f'''
<section class="sec sec-black">
  <div class="grid2">
    <div>
      <h2 class="ttl">¿POR QUÉ LA LUZ?</h2>
      <p class="stxt stxt-lg">La luz es información — y tu cuerpo siempre está escuchando.</p>
      <p class="stxt">Es acupuntura unida a la biología cuántica — sin agujas ni complejidad.</p>
      <p class="stxt">Nuestro parche patentado refleja longitudes de onda específicas de luz que estimulan tu piel para elevar el <b>GHK-Cu</b>, el péptido de cobre clínicamente comprobado para reparar y regenerar células dañadas.</p>
      <p class="stxt">Nada entra en tu cuerpo. Solo una señal limpia que despierta lo que ya está dentro de ti.</p>
      <p class="stxt stxt-it"><b>Tu cuerpo sabe qué hacer. El parche simplemente se lo recuerda.</b></p>
    </div>
    <div><img src="{IMG_PATCHES}" class="img-full" alt="Parches LifeWave"></div>
  </div>
</section>
''', unsafe_allow_html=True)

# 6. NOT ABOUT QUICK FIXES  (fixed — now uses couple photo from whythelight, not unsplash)
st.markdown(f'''
<section class="sec sec-black">
  <div class="grid2-rev">
    <div><img src="{IMG_COUPLE}" class="img-full" alt="Pareja viviendo con vitalidad"></div>
    <div>
      <h2 class="ttl">NO SE TRATA DE SOLUCIONES RÁPIDAS NI DE ENMASCARAR SÍNTOMAS</h2>
      <p class="stxt">Imagina despertar con energía que no viene de la cafeína. Piel que refleja tu vitalidad. Un cuerpo que responde como si recordara para qué fue creado.</p>
      <ul class="benefit-list">
        <li>Energía renovada que te acompaña todo el día</li>
        <li>Sueño profundo y reparador con mayor claridad mental</li>
        <li>Piel más tersa y joven con soporte natural de colágeno</li>
        <li>Recuperación más rápida — del ejercicio o de la vida</li>
        <li>Regeneración que comienza de adentro hacia afuera</li>
        <li>y lo más importante… <b><i>¡sentirte tú mismo/a de nuevo!</i></b></li>
      </ul>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)

# 7. GHK-Cu
st.markdown(f'''
<section class="sec sec-black">
  <div class="grid2">
    <div>
      <h2 class="ttl">GHK-Cu PÉPTIDO DE COBRE</h2>
      <p class="stxt stxt-lg" style="color:#d4a94a;font-weight:700">¡El súper péptido de tu propio cuerpo!</p>
      <p class="stxt">El interruptor maestro que reactiva la capacidad curativa de tu cuerpo.</p>
      <p class="stxt">A medida que envejecemos, los niveles naturales de <b>GHK-Cu</b> disminuyen — y con ellos, nuestra capacidad de reparar, renovar y regenerar.</p>
      <p class="stxt">Nuestro parche está clínicamente comprobado para elevar el GHK-Cu, restaurando este péptido vital a niveles juveniles.</p>
      <p class="stxt">Aunque no sientas algo de inmediato, tus células ya están trabajando — reparando primero lo más importante, y luego avanzando hacia los cambios que puedes ver y sentir.</p>
      <a href="{LINK_GHK}" target="_blank" rel="noopener" class="btn" style="margin-top:22px">Más información sobre GHK ›</a>
    </div>
    <div><img src="{IMG_MOUNTAIN}" class="img-full" alt="Hombre frente a la montaña"></div>
  </div>
</section>
''', unsafe_allow_html=True)

# 8. SKEPTICAL + TESTIMONIALS CAROUSEL
test_html = '<div class="test-scroll">'
for vid_id, label in TESTIMONIALS:
    test_html += f'''<div class="test-card">
<div class="video-wrap"><iframe src="https://player.vimeo.com/video/{vid_id}?title=0&byline=0&portrait=0" allow="fullscreen" allowfullscreen loading="lazy"></iframe></div>
<div class="test-label">{label}</div></div>'''
test_html += '</div>'

st.markdown(f'''
<section class="sec sec-black" style="text-align:center">
  <h2 class="ttl ttl-center">SI ERES ESCÉPTICO/A, BIEN…</h2>
  <p class="stxt stxt-lg" style="text-align:center">Muchos de nuestros clientes también lo fueron.</p>
  {test_html}
  <p class="scroll-hint">(Desliza para ver más testimonios)</p>
  <div style="margin-top:28px">
    <a href="{LINK_RESULTS}" target="_blank" rel="noopener" class="btn btn-outline">Ver más experiencias personales ›</a>
  </div>
</section>
''', unsafe_allow_html=True)

# 9. HOW TO WEAR
st.markdown(f'''
<section class="sec sec-black">
  <div class="grid2">
    <div>
      <h2 class="ttl">CÓMO USAR EL PARCHE</h2>
      <p class="stxt stxt-lg" style="color:#d4a94a;font-weight:700;margin-bottom:18px">¡Simplemente despega y pega!</p>
      <div class="step-row"><div class="step-num">1</div><div class="step-txt">Aplica sobre piel limpia y seca.</div></div>
      <div class="step-row"><div class="step-num">2</div><div class="step-txt">Úsalo hasta 12 horas puesto, luego 12 horas sin él.</div></div>
      <div class="step-row"><div class="step-num">3</div><div class="step-txt">Desecha el parche o colócalo en tu mascota.</div></div>
      <div class="step-row"><div class="step-num">4</div><div class="step-txt">Coloca un parche nuevo y repite diariamente.</div></div>
      <p class="stxt" style="margin-top:18px">Para mejores resultados, asegúrate de tomar <b>mucha agua</b>.</p>
    </div>
    <div><img src="{IMG_PATCH_PLACEMENT}" class="img-full" alt="Colocación del parche"></div>
  </div>
</section>
''', unsafe_allow_html=True)

# 10. TIMELINE
st.markdown(f'''
<section class="sec sec-black" style="text-align:center">
  <h2 class="ttl ttl-center">ESTO ES LO QUE PUEDES ESPERAR</h2>
  <div class="tl-grid">
    <div class="tl-card">
      <img src="{IMG_TL_DAYS}" alt="Primeros días">
      <h3>En los primeros días</h3>
      <h4>4.000 genes comienzan a reiniciarse</h4>
    </div>
    <div class="tl-card">
      <img src="{IMG_TL_4W}" alt="4 semanas">
      <h3>En 4 semanas</h3>
      <h4>Se activa la reparación celular</h4>
      <p>Trabajando silenciosamente en lo que tu cuerpo más necesita</p>
    </div>
    <div class="tl-card">
      <img src="{IMG_TL_6W}" alt="6 semanas">
      <h3>En 6 semanas</h3>
      <h4>Tu cerebro y energía entran en balance</h4>
      <p>*Respaldado por estudios de PSY-TEK Labs y The Center for Biofield Sciences</p>
    </div>
    <div class="tl-card">
      <img src="{IMG_TL_3M}" alt="3-6 meses">
      <h3>En 3-6 meses</h3>
      <h4>El colágeno aumenta</h4>
      <p>La piel se suaviza, la recuperación se acelera</p>
    </div>
    <div class="tl-card">
      <img src="{IMG_TL_12M}" alt="12 meses">
      <h3>En 12 meses</h3>
      <h4>No solo te sientes mejor…</h4>
      <p>te ves y vives como tal</p>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)

# 11. ABOUT THE COMPANY
st.markdown(f'''
<section class="sec sec-black">
  <div class="about-grid">
    <div class="video-wrap">
      <iframe src="https://player.vimeo.com/video/{VIMEO_DAVID}?title=0&byline=0&portrait=0" allow="autoplay;fullscreen" allowfullscreen></iframe>
    </div>
    <div>
      <h2 class="ttl">ACERCA DE LA EMPRESA</h2>
      <h3 style="font-size:clamp(18px,2vw,24px);margin-bottom:18px;color:#fff">David Schmidt<br>Fundador, inventor y CEO</h3>
      <p class="about-txt">Desde 2004, hemos ayudado a personas en todo el mundo a sentirse mejor, verse más jóvenes y llevar vidas más plenas. Lo hacemos a través de productos de bienestar que aprovechan la energía natural y la resiliencia del cuerpo, y a través de oportunidades de negocio que inspiran realización personal y profesional.</p>
      <p class="about-txt" style="margin-top:14px">A nivel global, David es titular de más de <b>200 patentes otorgadas</b> — con muchas más en proceso. Más de setenta de esas patentes están en el campo de la ciencia y tecnología regenerativa.</p>
      <p class="about-txt" style="margin-top:14px">A lo largo de los años, LifeWave ha recibido múltiples premios, incluyendo el reciente <b>Premio Biotech Breakthrough 2025</b> a la «Innovación en células madre del año».</p>
      <div style="margin-top:22px"><a href="{LINK_STUDIES}" target="_blank" rel="noopener" class="btn btn-outline">Patentes y estudios ›</a></div>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)

# 12. PATENTS & RISK-FREE
st.markdown(f'''
<section class="sec sec-black">
  <div class="risk-box">
    <div class="risk-img-row">
      <img src="{IMG_HOLDING}" alt="Sosteniendo el parche" style="border-radius:14px">
      <img src="{IMG_BADGE}" class="badge-img" alt="Garantía 30/90 días">
    </div>
    <h2 class="ttl ttl-center" style="font-size:clamp(24px,3vw,38px)">¡Disfruta de los beneficios con confianza!</h2>
    <p class="stxt stxt-lg" style="margin-top:8px">Prueba nuestro parche <b>sin riesgos durante 30/90 días*</b></p>
  </div>
</section>
''', unsafe_allow_html=True)

# 13. CURIOUS / WHATSAPP CTA
st.markdown(f'''
<section class="sec sec-black">
  <div class="cta-grid">
    <div>
      <h2 class="ttl">¿SIENTES CURIOSIDAD POR SABER CÓMO ENCAJA ESTO EN TU CAMINO DE SALUD?</h2>
      <p class="stxt stxt-lg">No estás solo/a.</p>
      <p class="stxt stxt-lg">Ponte en contacto con la persona que compartió este sitio contigo.</p>
      <div class="cta-btns">
        <a href="{WA}" target="_blank" rel="noopener" class="btn btn-wa">💬 Escríbeme por WhatsApp</a>
        <a href="{LINK_PRICING}" target="_blank" rel="noopener" class="btn">Información sobre paquetes y precios ›</a>
      </div>
    </div>
    <div><img src="{IMG_KITCHEN}" class="img-full" alt="Pareja feliz en la cocina"></div>
  </div>
</section>
''', unsafe_allow_html=True)

# FOOTER
st.markdown(f'''
<div class="footer">
  <p><b>Descargo de responsabilidad:</b> Nuestros parches se basan en la teoría de la fototerapia.<br>
  Los parches no están comprobados según los estándares de la medicina convencional y no deben usarse en lugar de la atención médica.</p>
  <p style="margin-top:12px">*Garantía de devolución de dinero de 90 días para Clientes Minoristas y Preferidos. Garantía de devolución de 30 días para Socios de Marca Mayoristas.</p>
  <p style="margin-top:12px;font-size:11px;max-width:1000px;margin-left:auto;margin-right:auto">Nuestros productos no están destinados a diagnosticar, tratar, curar o prevenir ninguna enfermedad o condición médica. El contenido presentado es de naturaleza general y se proporciona solo con fines informativos. No asumimos responsabilidad por daños o lesiones a personas o propiedades que surjan del uso de cualquier producto, información, idea o instrucción contenida en los materiales proporcionados.</p>
  <p style="margin-top:22px;font-size:14px;color:#6a6a6a">©2026 Pauli Wellness · Todos los derechos reservados.</p>
</div>
''', unsafe_allow_html=True)
