"""Pauli Wellness – Replica fiel de whythelight.com/es/"""
import streamlit as st

st.set_page_config(
    page_title="¿Por qué la luz?",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

WA = "593939890499"
WA_URL = f"https://wa.me/{WA}?text=Hola%20Pauli!%20Vi%20tu%20pagina%20y%20me%20gustaria%20saber%20mas%20sobre%20los%20parches%20LifeWave"

# ── Image URLs (from whythelight.com) ──────────────────────────────
IMG = {
    "aging":       "https://whythelight.com/wp-content/uploads/2025/11/womanAging-battery-1-1024x981.png",
    "video_thumb": "https://whythelight.com/wp-content/uploads/2025/11/3-MinuteVideo-thumbnail-2-1.png",
    "patch_place": "https://whythelight.com/wp-content/uploads/2025/09/SN-Patch-placement-scaled-1-690x1024.jpg",
    "couple":      "https://whythelight.com/wp-content/uploads/2025/09/490141872_10162757194347458_245241563246855534_n-1024x1024.jpg",
    "mountain":    "https://whythelight.com/wp-content/uploads/2025/11/Man-frontOfMtn-819x1024.png",
    "patches":     "https://whythelight.com/wp-content/uploads/2025/09/Phototherapy-LifeWave-patches-clean-1024x1024.jpg",
    "tl_days":     "https://whythelight.com/wp-content/uploads/2025/09/timeline-firstFewDays-2.png",
    "tl_6w":       "https://whythelight.com/wp-content/uploads/2025/09/timeline-6weeks-2.png",
    "tl_3m":       "https://whythelight.com/wp-content/uploads/2025/09/timeline-3months-2.png",
    "tl_women":    "https://whythelight.com/wp-content/uploads/2025/09/timeline-3women.png",
    "tl_med":      "https://whythelight.com/wp-content/uploads/2025/09/timeline-meditation.png",
    "holding":     "https://whythelight.com/wp-content/uploads/2025/11/HoldingPatch-clean-cropped-1024x759.png",
    "badge":       "https://whythelight.com/wp-content/uploads/2025/09/90-dayGuarantee.png",
    "kitchen":     "https://whythelight.com/wp-content/uploads/2025/09/ManWoman-Kitchen-swirl-1024x645.png",
}

# Testimonial video thumbnail IDs (from Vimeo CDN)
TEST_VIDS = [
    "2058613616", "2058621890", "2108344089", "2058623296",
    "2058629372", "2058612341", "2058625996", "2058626286", "2058631142",
]

# ── CSS ────────────────────────────────────────────────────────────
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
.stApp{background:#0a0a0f!important;font-family:'Inter',sans-serif!important;color:#e8e8ed!important}
.block-container{padding-top:0!important;padding-bottom:0!important;max-width:100%!important}
header[data-testid="stHeader"]{display:none!important}
#MainMenu,footer,.stDeployButton{visibility:hidden!important;display:none!important}
div[data-testid="stSidebarCollapsedControl"]{display:none!important}

/* ── Sections ── */
.sec{max-width:1100px;margin:0 auto;padding:80px 24px}
.sec-full{padding:80px 24px}
.sec-center{text-align:center}

/* ── Typography ── */
.heading{font-family:'Playfair Display',serif;font-size:clamp(2rem,4.5vw,3.2rem);font-weight:700;color:#fff;line-height:1.15;margin-bottom:20px}
.heading-lg{font-family:'Playfair Display',serif;font-size:clamp(2.4rem,5.5vw,4rem);font-weight:700;color:#fff;line-height:1.1;margin-bottom:24px}
.subtext{font-size:clamp(.95rem,1.8vw,1.15rem);color:rgba(255,255,255,.6);line-height:1.75;max-width:700px}
.subtext-center{margin-left:auto;margin-right:auto}
.accent{color:#c9a84c}
.accent2{color:#7ecfc0}

/* ── Hero ── */
.hero-wrap{background:linear-gradient(180deg,#0a0a0f 0%,#111118 100%);padding:60px 24px 80px;text-align:center}
.hero-inner{max-width:900px;margin:0 auto}
.hero-lead{font-size:clamp(1rem,2vw,1.2rem);color:rgba(255,255,255,.55);line-height:1.8;margin-bottom:32px}
.hero-lead strong{color:#c9a84c}

/* ── Buttons ── */
.btn-wa{display:inline-flex;align-items:center;gap:10px;background:#25D366;color:#fff!important;text-decoration:none!important;padding:16px 36px;border-radius:50px;font-weight:700;font-size:1rem;transition:all .3s;box-shadow:0 4px 20px rgba(37,211,102,.3)}
.btn-wa:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(37,211,102,.45)}
.btn-outline{display:inline-flex;align-items:center;gap:8px;border:1.5px solid rgba(255,255,255,.25);color:#fff!important;text-decoration:none!important;padding:14px 32px;border-radius:50px;font-weight:600;font-size:.95rem;transition:all .3s;background:transparent}
.btn-outline:hover{border-color:#c9a84c;color:#c9a84c!important}

/* ── Divider line ── */
.divider{width:60px;height:2px;background:#c9a84c;margin:24px auto}

/* ── Two-col layout ── */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}

/* ── Image helpers ── */
.img-rounded{border-radius:16px;width:100%;height:auto;display:block}
.img-circle{border-radius:50%;width:100%;max-width:280px;height:auto;display:block;margin:0 auto}

/* ── Symptom pills ── */
.symptoms{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.symptom{background:rgba(201,168,76,.08);border:1px solid rgba(201,168,76,.2);border-radius:50px;padding:10px 22px;font-size:.9rem;color:rgba(255,255,255,.7)}

/* ── Video thumbnail ── */
.vid-thumb{position:relative;border-radius:16px;overflow:hidden;cursor:pointer;max-width:600px;margin:0 auto;display:block}
.vid-thumb img{width:100%;display:block;border-radius:16px}
.vid-play{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:72px;height:72px;background:rgba(0,0,0,.55);border-radius:50%;display:flex;align-items:center;justify-content:center;border:2px solid rgba(255,255,255,.7)}
.vid-play::after{content:'';border-style:solid;border-width:14px 0 14px 24px;border-color:transparent transparent transparent #fff;margin-left:4px}
.vid-label{text-align:center;margin-top:12px;font-size:.9rem;color:rgba(255,255,255,.5)}

/* ── Benefits grid ── */
.ben-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:40px}
.ben-card{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:32px;transition:border-color .3s}
.ben-card:hover{border-color:rgba(201,168,76,.3)}
.ben-icon{font-size:1.8rem;margin-bottom:12px}
.ben-title{font-size:1.05rem;font-weight:700;color:#fff;margin-bottom:8px}
.ben-desc{font-size:.9rem;color:rgba(255,255,255,.5);line-height:1.6}

/* ── GHK section ── */
.ghk-box{background:linear-gradient(135deg,rgba(126,207,192,.06),rgba(201,168,76,.04));border:1px solid rgba(126,207,192,.15);border-radius:20px;padding:48px 36px}

/* ── Testimonial carousel ── */
.test-scroll{display:flex;gap:20px;overflow-x:auto;padding:20px 0;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch}
.test-scroll::-webkit-scrollbar{height:6px}
.test-scroll::-webkit-scrollbar-thumb{background:rgba(255,255,255,.15);border-radius:3px}
.test-card{flex:0 0 280px;scroll-snap-align:start;border-radius:14px;overflow:hidden;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);transition:border-color .3s;cursor:pointer}
.test-card:hover{border-color:rgba(201,168,76,.3)}
.test-card img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.test-card .play-sm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:48px;height:48px;background:rgba(0,0,0,.5);border-radius:50%;display:flex;align-items:center;justify-content:center}
.test-card-inner{position:relative}

/* ── How to use steps ── */
.steps-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:28px;margin-top:40px}
.step-card{text-align:center;padding:28px 20px}
.step-num{width:48px;height:48px;border-radius:50%;background:rgba(201,168,76,.15);border:1.5px solid rgba(201,168,76,.3);display:flex;align-items:center;justify-content:center;font-size:1.2rem;font-weight:800;color:#c9a84c;margin:0 auto 16px}
.step-title{font-size:1rem;font-weight:700;color:#fff;margin-bottom:8px}
.step-desc{font-size:.88rem;color:rgba(255,255,255,.5);line-height:1.6}

/* ── Timeline ── */
.tl-grid{display:grid;grid-template-columns:1fr 1fr;gap:36px;margin-top:48px}
.tl-item{display:grid;grid-template-columns:100px 1fr;gap:20px;align-items:start}
.tl-item img{width:100px;height:100px;border-radius:12px;object-fit:cover}
.tl-period{font-size:.8rem;font-weight:700;color:#c9a84c;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px}
.tl-desc{font-size:.92rem;color:rgba(255,255,255,.6);line-height:1.6}

/* ── About / David ── */
.about-card{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:48px;text-align:center;max-width:800px;margin:0 auto}

/* ── Guarantee ── */
.guarantee{display:flex;align-items:center;gap:32px;justify-content:center;flex-wrap:wrap;padding:48px 24px}
.guarantee img{width:120px}

/* ── CTA ── */
.cta-box{background:linear-gradient(135deg,rgba(201,168,76,.08),rgba(126,207,192,.05));border:1px solid rgba(201,168,76,.15);border-radius:24px;padding:60px 40px;text-align:center;max-width:800px;margin:0 auto}

/* ── Footer ── */
.foot{text-align:center;padding:48px 24px;border-top:1px solid rgba(255,255,255,.06)}
.foot p{color:rgba(255,255,255,.3);font-size:.78rem;line-height:1.7;max-width:800px;margin:0 auto}

/* ── WhatsApp FAB ── */
.waf{position:fixed;bottom:24px;right:24px;z-index:9999;width:60px;height:60px;background:#25D366;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 25px rgba(37,211,102,.4);transition:all .3s;animation:bounce 2s infinite}
.waf:hover{transform:scale(1.1)}
.waf svg{width:32px;height:32px;fill:white}
@keyframes bounce{0%,20%,50%,80%,100%{transform:translateY(0)}40%{transform:translateY(-8px)}60%{transform:translateY(-4px)}}

/* ── Responsive ── */
@media(max-width:768px){
  .two-col{grid-template-columns:1fr;gap:32px}
  .tl-grid{grid-template-columns:1fr}
  .sec{padding:60px 16px}
  .hero-wrap{padding:40px 16px 60px}
  .guarantee{flex-direction:column;text-align:center}
  .test-card{flex:0 0 240px}
  .cta-box{padding:40px 20px}
}
</style>""", unsafe_allow_html=True)

# ── WhatsApp FAB ──────────────────────────────────────────────────
st.markdown(f'''<a href="{WA_URL}" target="_blank" class="waf" title="WhatsApp">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.8-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.3-5-3.7-10.5-6.6z"/></svg></a>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HERO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="hero-wrap"><div class="hero-inner">
<p class="hero-lead">
Tras <strong>10 años de investigación con células madre</strong> y más de <strong>200 patentes mundiales</strong>…
descubrimos una manera de utilizar la luz, no productos químicos, para señalar la propia
producción celular de su cuerpo.<br><br>
Es como activar el interruptor de reparación de tu propio cuerpo… <em>con seguridad, sin esfuerzo y desde dentro.</em>
</p>
</div></div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ¿POR QUÉ TANTA INVESTIGACIÓN?
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec">
<div class="two-col">
  <div>
    <h2 class="heading">¿Por qué tanta investigación?</h2>
    <p class="subtext">
      A medida que envejecemos, las células reparadoras naturales de nuestro organismo se ralentizan.
      Un menor número de células activas significa que su cuerpo se cura más lentamente y muestra
      signos de envejecimiento más rápidamente.
    </p>
    <p class="subtext" style="margin-top:20px">Y… empiezas a sentirlo…</p>
    <div class="symptoms">
      <span class="symptom">Dolores y rigidez</span>
      <span class="symptom">Sueño insuficiente</span>
      <span class="symptom">Recuperación lenta</span>
      <span class="symptom">Baja energía y concentración</span>
      <span class="symptom">Líneas de expresión</span>
      <span class="symptom">Adelgazamiento del cabello</span>
      <span class="symptom">Inflamación</span>
    </div>
    <p class="subtext" style="margin-top:28px">
      Si pudieras reparar y regenerar de dentro a fuera de forma segura y asequible…
      <strong style="color:#c9a84c">¿no te gustaría?</strong>
    </p>
  </div>
  <div style="text-align:center">
    <img src="{IMG['aging']}" alt="Envejecimiento celular" class="img-rounded">
  </div>
</div>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# NO ES UNA PASTILLA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec sec-center" style="background:rgba(255,255,255,.02)">
<h2 class="heading">No se trata de una pastilla, crema, inyección o tendencia mejor.</h2>
<p class="subtext subtext-center" style="margin-bottom:20px">
  Se trata de una <strong style="color:#c9a84c">categoría completamente nueva.</strong>
</p>
<p class="subtext subtext-center">
  Un parche no transdérmico para llevar puesto con resultados reales respaldados por la ciencia,
  estudios clínicos y patentes mundiales.
</p>
<div class="symptoms" style="justify-content:center;margin-top:28px">
  <span class="symptom">Sin medicamentos</span>
  <span class="symptom">Sin inyecciones</span>
  <span class="symptom">Sin conjeturas</span>
  <span class="symptom">Sin efectos secundarios</span>
</div>
<p class="subtext subtext-center" style="margin-top:28px;font-style:italic">
  Sólo luz — enviando una señal que tu cuerpo olvidó… hasta ahora.
</p>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# VIDEO CTA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec sec-center">
<h2 class="heading" style="font-size:clamp(1.4rem,3vw,2rem)">Vea cómo funciona el parche</h2>
<p class="subtext subtext-center" style="margin-bottom:32px">Vídeo de 3 minutos</p>
<a href="https://whythelight.com/es/" target="_blank" class="vid-thumb">
  <img src="{IMG['video_thumb']}" alt="Ver video">
  <div class="vid-play"></div>
</a>
<p class="vid-label">Haz clic para ver el video en whythelight.com</p>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ¿POR QUÉ LA LUZ?
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec">
<div class="two-col">
  <div>
    <h2 class="heading">¿Por qué la luz?</h2>
    <p class="subtext" style="margin-bottom:20px">
      La luz es información, y tu cuerpo siempre está a la escucha.
    </p>
    <p class="subtext" style="margin-bottom:20px">
      Es la acupuntura unida a la biología cuántica, sin agujas ni complejidades.
    </p>
    <p class="subtext">
      Nuestro parche patentado refleja longitudes de onda específicas de luz que estimulan
      la piel para elevar <strong class="accent2">GHK-Cu</strong>, el péptido de cobre clínicamente
      probado para reparar y regenerar las células dañadas.
    </p>
    <p class="subtext" style="margin-top:20px">
      Nada entra en tu cuerpo. Solo una señal clara que despierta lo que ya hay dentro de ti.
    </p>
    <p class="subtext" style="margin-top:20px;font-style:italic;color:rgba(255,255,255,.7)">
      Tu cuerpo sabe qué hacer. El parche simplemente lo recuerda.
    </p>
  </div>
  <div style="text-align:center">
    <img src="{IMG['mountain']}" alt="Bienestar" class="img-rounded">
  </div>
</div>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BENEFITS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown('''<div class="sec sec-center" style="background:rgba(255,255,255,.02)">
<p class="subtext subtext-center" style="margin-bottom:12px">No se trata de soluciones rápidas ni de enmascarar los síntomas. Imagine…</p>
<div class="ben-grid">
  <div class="ben-card"><div class="ben-icon">⚡</div><div class="ben-title">Energía renovada</div>
    <div class="ben-desc">Que te lleva a lo largo del día</div></div>
  <div class="ben-card"><div class="ben-icon">🧠</div><div class="ben-title">Sueño profundo y reparador</div>
    <div class="ben-desc">Y mayor claridad cerebral</div></div>
  <div class="ben-card"><div class="ben-icon">✨</div><div class="ben-title">Piel más tersa y juvenil</div>
    <div class="ben-desc">Con soporte de colágeno natural</div></div>
  <div class="ben-card"><div class="ben-icon">💪</div><div class="ben-title">Recuperación más rápida</div>
    <div class="ben-desc">Del ejercicio o de la vida</div></div>
  <div class="ben-card"><div class="ben-icon">🔄</div><div class="ben-title">Regeneración desde adentro</div>
    <div class="ben-desc">De adentro hacia afuera</div></div>
  <div class="ben-card"><div class="ben-icon">🙌</div><div class="ben-title">Sintiéte tú mismo/a de nuevo</div>
    <div class="ben-desc">¡Lo más importante!</div></div>
</div>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# GHK-Cu
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec">
<div class="two-col">
  <div class="ghk-box">
    <p style="font-size:.8rem;font-weight:600;color:#7ecfc0;text-transform:uppercase;letter-spacing:2px;margin-bottom:12px">GHK-Cu · Péptido de cobre</p>
    <h2 class="heading" style="font-size:clamp(1.6rem,3vw,2.2rem)">El superpéptido de tu propio cuerpo.</h2>
    <p class="subtext" style="margin-bottom:16px">
      El interruptor maestro que vuelve a activar la capacidad curativa de tu cuerpo.
    </p>
    <p class="subtext" style="margin-bottom:16px">
      A medida que envejecemos, los niveles naturales de GHK-Cu de nuestro cuerpo disminuyen
      y, con ellas, nuestra capacidad de reparación, renovación y regeneración.
    </p>
    <p class="subtext" style="margin-bottom:16px">
      Está clínicamente probado que nuestro parche eleva GHK-Cu, restaurando este péptido
      de cobre vital a niveles juveniles.
    </p>
    <p class="subtext" style="font-style:italic">
      Aunque no sientas nada de inmediato, tus células ya están trabajando duro: primero
      reparan lo más importante y luego pasan a los cambios que puedes ver y sentir.
    </p>
    <a href="https://whythelight.com/es/ghk-cu/" target="_blank" class="btn-outline" style="margin-top:24px">Más información sobre GHK →</a>
  </div>
  <div style="text-align:center">
    <img src="{IMG['couple']}" alt="Pareja saludable" class="img-rounded">
  </div>
</div>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TESTIMONIALS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
test_cards = ""
for vid in TEST_VIDS:
    thumb_url = f"https://i.vimeocdn.com/video/{vid}-d_840"
    test_cards += f'''<div class="test-card">
      <div class="test-card-inner">
        <img src="{thumb_url}" alt="Testimonio" loading="lazy">
      </div>
    </div>'''

st.markdown(f'''<div class="sec sec-center">
<h2 class="heading">Si eres escéptico, bien…</h2>
<p class="subtext subtext-center" style="margin-bottom:32px">
  Muchos de nuestros clientes también lo estaban.
</p>
<div class="test-scroll">{test_cards}</div>
<p style="font-size:.8rem;color:rgba(255,255,255,.35);margin-top:12px">(Desplácese para ver más testimonios)</p>
<a href="https://whythelight.com/es/resultados-reales/" target="_blank" class="btn-outline" style="margin-top:24px">Ver más experiencias personales →</a>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CÓMO USAR EL PARCHE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec" style="background:rgba(255,255,255,.02)">
<div class="two-col">
  <div>
    <h2 class="heading">Cómo llevar el parche</h2>
    <p class="subtext" style="margin-bottom:32px">Basta con despegar y pegar.</p>
    <div class="steps-grid" style="grid-template-columns:1fr 1fr">
      <div class="step-card"><div class="step-num">1</div><div class="step-title">Aplicar</div>
        <div class="step-desc">Sobre la piel limpia y seca.</div></div>
      <div class="step-card"><div class="step-num">2</div><div class="step-title">Llevar</div>
        <div class="step-desc">Hasta 12 horas encendido, luego 12 horas apagado.</div></div>
      <div class="step-card"><div class="step-num">3</div><div class="step-title">Reutilizar</div>
        <div class="step-desc">Tire el parche o póngaselo a su mascota.</div></div>
      <div class="step-card"><div class="step-num">4</div><div class="step-title">Repetir</div>
        <div class="step-desc">Póngase un nuevo parche y repita la operación a diario.</div></div>
    </div>
    <p class="subtext" style="margin-top:24px;font-style:italic;font-size:.85rem">
      Para obtener los mejores resultados, asegúrese de beber mucha agua.
    </p>
  </div>
  <div style="text-align:center">
    <img src="{IMG['patch_place']}" alt="Colocación del parche" class="img-rounded" style="max-width:400px;margin:0 auto">
  </div>
</div>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# QUÉ ESPERAR – TIMELINE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec sec-center">
<h2 class="heading">Esto es lo que puede esperar</h2>
<div class="divider"></div>
<div class="tl-grid">

  <div class="tl-item">
    <img src="{IMG['tl_days']}" alt="Primeros días">
    <div>
      <div class="tl-period">En los primeros días</div>
      <div class="tl-desc">4.000 genes comienzan a reiniciarse</div>
    </div>
  </div>

  <div class="tl-item">
    <img src="{IMG['tl_med']}" alt="4 semanas">
    <div>
      <div class="tl-period">En 4 semanas</div>
      <div class="tl-desc">Se activa la reparación celular. Trabaja en silencio lo que tu cuerpo más necesita.</div>
    </div>
  </div>

  <div class="tl-item">
    <img src="{IMG['tl_6w']}" alt="6 semanas">
    <div>
      <div class="tl-period">En 6 semanas</div>
      <div class="tl-desc">Tu cerebro y tu energía entran en balance.*
      <br><span style="font-size:.75rem;color:rgba(255,255,255,.35)">*Apoyado por estudios de PSY-TEK Labs y The Center for Biofield Sciences</span></div>
    </div>
  </div>

  <div class="tl-item">
    <img src="{IMG['tl_3m']}" alt="3 meses">
    <div>
      <div class="tl-period">En 3-6 meses</div>
      <div class="tl-desc">Aumenta el colágeno. La piel suaviza, la recuperación se acelera.</div>
    </div>
  </div>

  <div class="tl-item" style="grid-column:1/-1;text-align:center;display:block">
    <img src="{IMG['tl_women']}" alt="12 meses" style="width:200px;margin:0 auto 12px;border-radius:12px">
    <div class="tl-period">Antes de 12 meses</div>
    <div class="tl-desc">No sólo te sientes mejor — te ves y vives como tal.</div>
  </div>

</div>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ACERCA DE LA EMPRESA — DAVID SCHMIDT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec">
<div class="about-card">
  <p style="font-size:.8rem;font-weight:600;color:#c9a84c;text-transform:uppercase;letter-spacing:2px;margin-bottom:16px">Acerca de la empresa</p>
  <h2 class="heading" style="font-size:clamp(1.4rem,3vw,2rem)">David Schmidt</h2>
  <p style="font-size:.9rem;color:rgba(255,255,255,.45);margin-bottom:20px">Fundador, Inventor + CEO</p>
  <p class="subtext subtext-center" style="margin-bottom:16px">
    Desde 2004, hemos ayudado a personas de todo el mundo a sentirse mejor, tener un aspecto
    más joven y llevar una vida más alegre.
  </p>
  <p class="subtext subtext-center" style="margin-bottom:16px">
    A nivel mundial, David es titular de más de 200 patentes concedidas y se están escribiendo
    muchas más. Más de setenta de las patentes concedidas pertenecen al campo de la ciencia
    y la tecnología regenerativas.
  </p>
  <p class="subtext subtext-center" style="font-style:italic">
    LifeWave ha recibido múltiples premios, entre ellos el reciente
    Premio Biotech Breakthrough 2025.
  </p>
</div>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PATENTES + GARANTÍA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec sec-center" style="background:rgba(255,255,255,.02)">
<a href="https://whythelight.com/es/estudios/" target="_blank" class="btn-outline" style="margin-bottom:40px">Patentes y estudios →</a>

<div class="guarantee">
  <img src="{IMG['badge']}" alt="Garantía 90 días">
  <div style="text-align:left">
    <h3 style="font-size:1.3rem;font-weight:700;color:#fff;margin-bottom:8px">¡Disfrute de los beneficios con confianza!</h3>
    <p class="subtext">Prueba nuestro parche sin riesgos durante 30/90 días*.</p>
  </div>
</div>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CTA FINAL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="sec">
<div class="cta-box">
  <img src="{IMG['holding']}" alt="Parche en mano" style="width:200px;border-radius:12px;margin-bottom:24px">
  <h2 class="heading" style="font-size:clamp(1.4rem,3vw,2rem)">
    ¿Siente curiosidad por saber cómo encaja esto en su propio camino hacia la salud?
  </h2>
  <p class="subtext subtext-center" style="margin-bottom:28px">
    No estás solo. Ponte en contacto con la persona que compartió este sitio web contigo.
  </p>
  <a href="{WA_URL}" target="_blank" class="btn-wa" style="font-size:1.05rem;padding:18px 40px">
    📲 Información sobre paquetes y precios
  </a>
</div>
</div>''', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FOOTER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(f'''<div class="foot">
<p style="margin-bottom:12px">
  Descargo de responsabilidad: Nuestros parches se basan en la teoría de la fototerapia.
  Los parches no están probados según los estándares de la medicina convencional y no deben
  utilizarse en lugar de la atención médica.
</p>
<p style="margin-bottom:12px">
  *Garantía de devolución del dinero de 90 días para clientes minoristas y preferentes.
  Garantía de devolución del dinero de 30 días para socios de marca mayoristas.
</p>
<p>
  Nuestros productos no están destinados a diagnosticar, tratar, curar o prevenir ninguna
  enfermedad o afección médica. El contenido presentado es en forma de resumen, es de carácter
  general y se proporciona únicamente con fines informativos.
</p>
<p style="margin-top:20px;font-size:.7rem">
  ©2026 Pauli Wellness · Brand Partner de <a href="https://www.lifewave.com" target="_blank"
  style="color:rgba(201,168,76,.6);text-decoration:none">LifeWave</a>
  · <a href="{WA_URL}" target="_blank" style="color:rgba(201,168,76,.6);text-decoration:none">WhatsApp</a>
  · Ecuador 🇪🇨
</p>
</div>''', unsafe_allow_html=True)
