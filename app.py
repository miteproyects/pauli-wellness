"""Pauli Wellness - LifeWave Landing Page (ES) - Exact replica of whythelight.com"""
import streamlit as st
st.set_page_config(page_title="Pauli Wellness | LifeWave", page_icon="✨", layout="wide", initial_sidebar_state="collapsed")
WA = "593939890499"
WA_URL = f"https://wa.me/{WA}?text=Hola%20Pauli!%20Vi%20tu%20pagina%20y%20me%20gustaria%20saber%20mas%20sobre%20los%20parches%20LifeWave"
# Image URLs from whythelight.com
IMG = {
    "hero": "https://whythelight.com/wp-content/uploads/2025/09/Woman-patchOnBack-600x400-1.png",
    "aging": "https://whythelight.com/wp-content/uploads/2025/11/womanAging-battery-1-1024x981.png",
    "video_thumb": "https://whythelight.com/wp-content/uploads/2025/11/3-MinuteVideo-thumbnail-2-1.png",
    "patch_place": "https://whythelight.com/wp-content/uploads/2025/09/SN-Patch-placement-scaled-1-690x1024.jpg",
    "couple": "https://whythelight.com/wp-content/uploads/2025/09/490141872_10162757194347458_245241563246855534_n-1024x1024.jpg",
    "mountain": "https://whythelight.com/wp-content/uploads/2025/11/Man-frontOfMtn-819x1024.png",
    "patches": "https://whythelight.com/wp-content/uploads/2025/09/Phototherapy-LifeWave-patches-clean-1024x1024.jpg",
    "tl_days": "https://whythelight.com/wp-content/uploads/2025/09/timeline-firstFewDays-2.png",
    "tl_6w": "https://whythelight.com/wp-content/uploads/2025/09/timeline-6weeks-2.png",
    "tl_3m": "https://whythelight.com/wp-content/uploads/2025/09/timeline-3months-2.png",
    "tl_women": "https://whythelight.com/wp-content/uploads/2025/09/timeline-3women.png",
    "tl_med": "https://whythelight.com/wp-content/uploads/2025/09/timeline-meditation.png",
    "holding": "https://whythelight.com/wp-content/uploads/2025/11/HoldingPatch-clean-cropped-1024x1024.png",
    "badge": "https://whythelight.com/wp-content/uploads/2025/09/MoneyBack-badge-1.png",
}
VIMEO_MAIN = "1107969285"
VIMEO_DS = "1022736477"
# Testimonial Vimeo video IDs
TEST_VIDS = [
    ("1049988653","Tendinitis en Codo"),
    ("1049981959","Ojos, Digestión, Piel"),
    ("1049987570","Rodilla"),
    ("1049987675","Dolor de Espalda"),
    ("1049989437","Energía y Sueño"),
    ("1049983588","Piel y Recuperación"),
    ("1049985898","Claridad Mental"),
    ("1072261891","Artritis"),
    ("1049982670","Inflamación"),
]
CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
.stApp{background:#fff!important;font-family:'Inter',sans-serif!important}
.block-container{padding:0!important;max-width:100%!important}
header[data-testid="stHeader"]{display:none!important}
#MainMenu,footer,.stDeployButton{display:none!important}
div[data-testid="stSidebarCollapsedControl"]{display:none!important}
section[data-testid="stSidebar"]{display:none!important}
.wa-float{position:fixed;bottom:25px;right:25px;z-index:9999;width:60px;height:60px;border-radius:50%;background:#25D366;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 15px rgba(37,211,102,.4);transition:transform .3s;text-decoration:none}
.wa-float:hover{transform:scale(1.1)}
.wa-float svg{width:35px;height:35px;fill:#fff}
.hero-section{position:relative;width:100%;min-height:90vh;background:linear-gradient(135deg,rgba(59,71,119,.85),rgba(27,42,74,.7)),url('HERO_BG') center/cover;display:flex;flex-direction:column;justify-content:center;padding:60px 8%}
.hero-top{font-size:clamp(28px,4.5vw,58px);font-weight:800;color:#fff;text-transform:uppercase;line-height:1.15;max-width:900px;margin-bottom:40px}
.hero-sub{font-size:clamp(18px,2.5vw,32px);color:#fff;text-align:right;max-width:700px;margin-left:auto;line-height:1.5}
.hero-sub2{font-size:clamp(16px,2vw,26px);color:#fff;text-align:right;max-width:700px;margin-left:auto;font-style:italic;margin-top:15px;line-height:1.5}
.sec{padding:60px 8%;width:100%}
.sec-dark{background:#1B2A4A;color:#fff}
.sec-light{background:#f5f5f5;color:#1a1a1a}
.sec-white{background:#fff;color:#1a1a1a}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.ttl{font-size:clamp(28px,4vw,52px);font-weight:800;text-transform:uppercase;line-height:1.15;margin-bottom:20px}
.ttl-center{text-align:center}
.stxt{font-size:clamp(16px,1.5vw,22px);line-height:1.7}
.stxt-it{font-style:italic}
.img-full{width:100%;height:auto;border-radius:8px;display:block}
.check-list{list-style:none;padding:0;margin:20px 0}
.check-list li{font-size:clamp(16px,1.4vw,20px);padding:8px 0;display:flex;align-items:center;gap:12px}
.check-list li::before{content:"›";font-size:24px;color:#1B2A4A;font-weight:bold;min-width:20px}
.check-dark li::before{color:#7eb8ff}
.benefit-list{list-style:none;padding:0;margin:20px 0}
.benefit-list li{font-size:clamp(16px,1.4vw,20px);padding:10px 0;display:flex;align-items:center;gap:12px}
.benefit-list li::before{content:"✔";color:#4CAF50;font-size:20px;min-width:24px}
.btn{display:inline-block;padding:16px 36px;background:#1B2A4A;color:#fff;text-decoration:none;border-radius:50px;font-weight:700;font-size:16px;text-transform:uppercase;letter-spacing:1px;transition:all .3s;border:none;cursor:pointer}
.btn:hover{background:#2d4470;transform:translateY(-2px)}
.btn-wa{background:#25D366}.btn-wa:hover{background:#1da851}
.video-wrap{position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,.2)}
.video-wrap iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}
.step-num{width:50px;height:50px;border-radius:50%;background:#f0f0f0;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:20px;color:#1B2A4A;flex-shrink:0}
.step-row{display:flex;align-items:center;gap:20px;margin:25px 0}
.step-txt{font-size:clamp(16px,1.5vw,22px);color:#fff}
.tl-card{background:rgba(255,255,255,.06);backdrop-filter:blur(10px);border-radius:16px;padding:30px;text-align:center;border:1px solid rgba(255,255,255,.1)}
.tl-card h3{font-size:clamp(18px,1.8vw,24px);color:#7eb8ff;margin-bottom:5px}
.tl-card h4{font-size:clamp(16px,1.5vw,20px);font-weight:700;margin-bottom:5px}
.tl-card p{font-size:14px;opacity:.8}
.tl-card img{width:100%;border-radius:12px;margin-bottom:15px}
.tl-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:25px;margin-top:30px}
.test-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:30px}
.test-card{border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.1)}
.test-card .video-wrap{border-radius:0;box-shadow:none}
.test-label{padding:10px;text-align:center;font-weight:600;font-size:14px;background:#f8f8f8}
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:start}
.about-txt{font-size:clamp(15px,1.3vw,18px);line-height:1.8;color:rgba(255,255,255,.9)}
.about-txt b{color:#fff}
.footer{background:#0a0f1a;color:rgba(255,255,255,.7);padding:40px 8%;text-align:center;font-size:13px;line-height:1.8}
@media(max-width:768px){
.grid2,.about-grid{grid-template-columns:1fr;gap:25px}
.hero-section{min-height:auto;padding:40px 5%}
.hero-sub,.hero-sub2{text-align:left;margin-left:0}
.sec{padding:40px 5%}
.tl-grid{grid-template-columns:1fr 1fr}
.test-grid{grid-template-columns:1fr}
}
</style>"""
# WhatsApp floating button
WA_BTN = f'''<a href="{WA_URL}" target="_blank" class="wa-float" aria-label="WhatsApp">
<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>'''
# Build page
st.markdown(CSS, unsafe_allow_html=True)
st.markdown(WA_BTN, unsafe_allow_html=True)
# HERO
st.markdown(f'''<div class="hero-section" style="background:linear-gradient(135deg,rgba(59,71,119,.85),rgba(27,42,74,.7)),url('{IMG["hero"]}') center/cover">
<div class="hero-top">DESPUÉS DE 10 AÑOS DE INVESTIGACIÓN EN CÉLULAS MADRE Y MÁS DE 200 PATENTES GLOBALES . . .</div>
<div class="hero-sub">descubrimos una forma de usar luz, no químicos, para estimular la producción celular de tu propio cuerpo.</div>
<div class="hero-sub2">Es como activar el interruptor de reparación de tu cuerpo — de forma segura, sin esfuerzo y desde adentro.</div>
</div>''', unsafe_allow_html=True)
# WHY ALL THE RESEARCH
st.markdown(f'''<div class="sec sec-light">
<div class="grid2">
<div><img src="{IMG["aging"]}" class="img-full" alt="Envejecimiento celular"></div>
<div>
<h2 class="ttl">¿POR QUÉ TANTA INVESTIGACIÓN?</h2>
<p class="stxt">A medida que envejeces, las células de reparación natural de tu cuerpo se ralentizan.</p>
<p class="stxt" style="margin-top:15px">Menos células activas significan que tu cuerpo sana más lentamente y muestra signos de envejecimiento más rápido.</p>
<p class="stxt stxt-it" style="margin-top:15px">Y... comienzas a sentirlo —</p>
<ul class="check-list">
<li>Dolores y rigidez</li>
<li>Mal sueño y recuperación lenta</li>
<li>Baja energía y concentración</li>
<li>Líneas finas, cabello debilitado e inflamación</li>
</ul>
<p class="stxt" style="margin-top:15px">Si pudieras reparar y regenerar de forma segura y asequible desde adentro hacia afuera — <b><i>¿no querrías hacerlo?</i></b></p>
</div>
</div>
</div>''', unsafe_allow_html=True)
# THIS ISN'T A BETTER PILL
st.markdown(f'''<div class="sec sec-white">
<div class="grid2">
<div>
<h2 class="ttl">ESTO NO ES UNA MEJOR PASTILLA, CREMA, INYECTABLE O TENDENCIA.</h2>
<p class="stxt" style="margin-top:15px">Esta es una categoría completamente nueva.</p>
<p class="stxt" style="margin-top:15px">Un parche portátil, no transdérmico, con resultados reales respaldados por ciencia, estudios clínicos y patentes globales.</p>
<p class="stxt" style="margin-top:20px"><b>Sin medicamentos. Sin inyecciones. Sin adivinanzas. Sin efectos secundarios.</b></p>
<p class="stxt stxt-it" style="margin-top:10px">Solo luz — enviando una señal que tu cuerpo olvidó . . . hasta ahora.</p>
</div>
<div class="video-wrap">
<iframe src="https://player.vimeo.com/video/{VIMEO_MAIN}?autoplay=0&title=0&byline=0&portrait=0" allow="autoplay;fullscreen" allowfullscreen></iframe>
</div>
</div>
</div>''', unsafe_allow_html=True)
# WATCH VIDEO CTA
st.markdown(f'''<div class="sec sec-dark" style="text-align:center;padding:50px 8%">
<div style="max-width:800px;margin:0 auto">
<div class="video-wrap" style="margin-bottom:20px">
<iframe src="https://player.vimeo.com/video/{VIMEO_MAIN}?autoplay=0&title=0&byline=0&portrait=0" allow="autoplay;fullscreen" allowfullscreen></iframe>
</div>
<p style="font-size:clamp(20px,2.5vw,32px);font-weight:700;color:#fff;margin-top:20px">← Mira Cómo Funciona el Parche<br>Video de 3 minutos</p>
</div>
</div>''', unsafe_allow_html=True)
# WHY LIGHT
st.markdown(f'''<div class="sec sec-white">
<div class="grid2">
<div>
<h2 class="ttl">¿POR QUÉ LA LUZ?</h2>
<p class="stxt" style="font-size:clamp(18px,2vw,26px)">La luz es información — y tu cuerpo siempre está escuchando.</p>
<p class="stxt" style="margin-top:15px">Es acupuntura combinada con biología cuántica — sin agujas ni complejidad.</p>
<p class="stxt" style="margin-top:15px">Nuestro parche patentado refleja longitudes de onda específicas de luz que estimulan tu piel para elevar el <b>GHK-Cu</b>, el péptido de cobre clínicamente comprobado para reparar y regenerar células dañadas.</p>
<p class="stxt" style="margin-top:15px">Nada entra en tu cuerpo. Solo una señal limpia que despierta lo que ya está dentro de ti.</p>
<p class="stxt stxt-it" style="margin-top:15px"><b>Tu cuerpo sabe qué hacer. El parche simplemente se lo recuerda.</b></p>
</div>
<div><img src="{IMG["patches"]}" class="img-full" alt="Parches LifeWave"></div>
</div>
</div>''', unsafe_allow_html=True)
# NOT ABOUT QUICK FIXES
st.markdown(f'''<div class="sec sec-dark">
<div class="grid2">
<div><img src="https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=600" class="img-full" alt="Persona activa" style="border-radius:12px"></div>
<div>
<h2 class="ttl">ESTO NO SE TRATA DE SOLUCIONES RÁPIDAS NI DE ENMASCARAR SÍNTOMAS</h2>
<p class="stxt" style="margin-top:15px">Imagina despertar con energía que no proviene de la cafeína. Piel que refleja tu vitalidad. Un cuerpo que responde como si recordara para qué fue creado.</p>
<ul class="benefit-list" style="margin-top:20px">
<li>Energía renovada que te acompaña todo el día</li>
<li>Sueño profundo y reparador con mayor claridad mental</li>
<li>Piel más suave y joven con soporte natural de colágeno</li>
<li>Recuperación más rápida — del ejercicio o de la vida</li>
<li>Regeneración que comienza desde adentro hacia afuera</li>
<li>y lo más importante… <b><i>¡sentirte tú mismo/a de nuevo!</i></b></li>
</ul>
</div>
</div>
</div>''', unsafe_allow_html=True)
# GHK-Cu
st.markdown(f'''<div class="sec sec-light">
<div class="grid2">
<div>
<h2 class="ttl" style="color:#1B2A4A">GHK-Cu Péptido de Cobre</h2>
<p class="stxt" style="font-size:clamp(18px,2vw,24px);color:#1B2A4A;font-weight:600;margin-bottom:15px">¡El súper péptido de tu propio cuerpo!</p>
<p class="stxt">El interruptor maestro que reactiva la capacidad de curación de tu cuerpo.</p>
<p class="stxt" style="margin-top:15px">A medida que envejecemos, los niveles naturales de <b>GHK-Cu</b> en nuestro cuerpo disminuyen — y con ellos, nuestra capacidad de reparar, renovar y regenerar.</p>
<p class="stxt" style="margin-top:15px">Nuestro parche está clínicamente comprobado para elevar el GHK-Cu, restaurando este péptido de cobre vital a niveles juveniles.</p>
<p class="stxt" style="margin-top:15px">Incluso si no sientes algo de inmediato, tus células ya están trabajando arduamente — reparando lo más importante primero, luego avanzando hacia los cambios que puedes ver y sentir.</p>
<a href="https://whythelight.com/ghk-cu/" target="_blank" class="btn" style="margin-top:20px">APRENDE MÁS SOBRE GHK ➜</a>
</div>
<div><img src="{IMG["mountain"]}" class="img-full" alt="Hombre en la montaña"></div>
</div>
</div>''', unsafe_allow_html=True)
# SKEPTICAL
st.markdown('''<div class="sec sec-white" style="text-align:center">
<h2 class="ttl ttl-center">SI ERES ESCÉPTICO/A, BIEN . . .</h2>
<p class="stxt" style="text-align:center">Muchos de nuestros clientes también lo fueron.</p>
</div>''', unsafe_allow_html=True)
# Testimonials
test_html = '<div class="sec sec-light"><div class="test-grid">'
for vid_id, label in TEST_VIDS[:6]:
    test_html += f'''<div class="test-card">
<div class="video-wrap"><iframe src="https://player.vimeo.com/video/{vid_id}?title=0&byline=0&portrait=0" allow="fullscreen" allowfullscreen loading="lazy"></iframe></div>
<div class="test-label">{label}</div></div>'''
test_html += '</div></div>'
st.markdown(test_html, unsafe_allow_html=True)
# HOW TO WEAR
st.markdown(f'''<div class="sec sec-dark">
<div class="grid2">
<div>
<h2 class="ttl">CÓMO USAR EL PARCHE</h2>
<p class="stxt" style="font-size:clamp(18px,2vw,26px);font-weight:600;margin-bottom:20px">¡Simplemente despega y pega!</p>
<div class="step-row"><div class="step-num">1</div><div class="step-txt">Aplica sobre piel limpia y seca.</div></div>
<div class="step-row"><div class="step-num">2</div><div class="step-txt">Úsalo hasta 12 horas puesto, luego 12 horas sin él.</div></div>
<div class="step-row"><div class="step-num">3</div><div class="step-txt">Desecha el parche o colócalo en tu mascota.</div></div>
<div class="step-row"><div class="step-num">4</div><div class="step-txt">Pon un parche nuevo y repite diariamente.</div></div>
<p class="stxt" style="margin-top:20px">Para mejores resultados, asegúrate de tomar <b>mucha agua</b>.</p>
</div>
<div><img src="{IMG["patch_place"]}" class="img-full" alt="Colocación del parche"></div>
</div>
</div>''', unsafe_allow_html=True)
# TIMELINE
st.markdown(f'''<div class="sec sec-white" style="text-align:center">
<h2 class="ttl ttl-center" style="color:#1B2A4A">QUÉ ESPERAR</h2>
<div class="tl-grid">
<div class="tl-card" style="background:#f0f4ff;border-color:#d0d8f0">
<img src="{IMG["tl_days"]}" alt="Primeros días">
<h3 style="color:#1B2A4A">En los Primeros Días</h3>
<h4>4,000 Genes Comienzan a Reiniciarse</h4>
</div>
<div class="tl-card" style="background:#f0f4ff;border-color:#d0d8f0">
<img src="{IMG["tl_6w"]}" alt="6 semanas">
<h3 style="color:#1B2A4A">Dentro de 4 Semanas</h3>
<h4>La Reparación Celular se Activa</h4>
<p style="color:#555">Trabajando silenciosamente en lo que tu cuerpo más necesita</p>
</div>
<div class="tl-card" style="background:#f0f4ff;border-color:#d0d8f0">
<img src="{IMG["tl_women"]}" alt="6 semanas balance">
<h3 style="color:#1B2A4A">Dentro de 6 Semanas</h3>
<h4>Tu Cerebro y Energía Entran en Balance</h4>
<p style="color:#555">*Respaldado por estudios de PSY-TEK Labs y The Center for Biofield Sciences</p>
</div>
<div class="tl-card" style="background:#f0f4ff;border-color:#d0d8f0">
<img src="{IMG["tl_3m"]}" alt="3-6 meses">
<h3 style="color:#1B2A4A">En 3-6 Meses</h3>
<h4>El Colágeno Aumenta</h4>
<p style="color:#555">La piel se suaviza, la recuperación se acelera</p>
</div>
<div class="tl-card" style="background:#f0f4ff;border-color:#d0d8f0">
<img src="{IMG["tl_med"]}" alt="12 meses">
<h3 style="color:#1B2A4A">A los 12 Meses</h3>
<h4>No solo te sientes mejor—</h4>
<p style="color:#555">te ves y vives como tal</p>
</div>
</div>
</div>''', unsafe_allow_html=True)
# ABOUT THE COMPANY
st.markdown(f'''<div class="sec sec-dark">
<div class="about-grid">
<div class="video-wrap">
<iframe src="https://player.vimeo.com/video/{VIMEO_DS}?title=0&byline=0&portrait=0" allow="autoplay;fullscreen" allowfullscreen></iframe>
</div>
<div>
<h2 class="ttl">ACERCA DE LA EMPRESA</h2>
<h3 style="font-size:clamp(18px,2vw,26px);margin-bottom:20px;color:#fff">David Schmidt<br>Fundador, Inventor + CEO</h3>
<p class="about-txt">Desde 2004, hemos ayudado a personas en todo el mundo a sentirse mejor, verse más jóvenes y llevar vidas más plenas. Lo hacemos a través de productos de bienestar que aprovechan la energía natural y la resiliencia del cuerpo, y a través de oportunidades de negocio que inspiran la realización personal y profesional.</p>
<p class="about-txt" style="margin-top:15px">A nivel global, David es titular de más de <b>200 patentes otorgadas</b> con muchas más en proceso. Más de setenta de esas patentes están en el campo de la ciencia y tecnología regenerativa.</p>
<p class="about-txt" style="margin-top:15px">A lo largo de los años, LifeWave ha recibido múltiples premios, incluyendo el reciente <b>Premio Biotech Breakthrough 2025 por "Innovación en Células Madre del Año"</b></p>
</div>
</div>
</div>''', unsafe_allow_html=True)
# PATENTS & RISK FREE
st.markdown(f'''<div class="sec sec-white" style="text-align:center">
<div class="grid2">
<div><img src="{IMG["holding"]}" class="img-full" alt="Sosteniendo parche"></div>
<div style="text-align:left">
<img src="{IMG["badge"]}" style="width:120px;margin-bottom:15px" alt="Garantía">
<h2 class="ttl">PATENTES Y ESTUDIOS</h2>
<p class="stxt" style="font-size:clamp(20px,2.5vw,32px);font-weight:700">¡Experimenta los beneficios con confianza!</p>
<p class="stxt" style="font-size:clamp(18px,2vw,26px);margin-top:10px">Prueba nuestro parche <b>Sin Riesgo por 30/90 días*</b></p>
</div>
</div>
</div>''', unsafe_allow_html=True)
# CTA SECTION
st.markdown(f'''<div class="sec sec-light">
<div class="grid2">
<div>
<h2 class="ttl">¿CURIOSO/A SOBRE CÓMO ESTO ENCAJA EN TU PROPIO CAMINO DE SALUD?</h2>
<p class="stxt" style="font-size:clamp(18px,2vw,24px);margin-top:15px">No estás solo/a.</p>
<p class="stxt" style="font-size:clamp(18px,2vw,24px)">Comunícate con la persona que compartió este sitio web contigo.</p>
<div style="margin-top:25px;display:flex;gap:15px;flex-wrap:wrap">
<a href="{WA_URL}" target="_blank" class="btn btn-wa">💬 ESCRÍBEME POR WHATSAPP</a>
</div>
</div>
<div><img src="{IMG["couple"]}" class="img-full" alt="Pareja feliz"></div>
</div>
</div>''', unsafe_allow_html=True)
# FOOTER
st.markdown(f'''<div class="footer">
<p>Aviso legal: Nuestros parches se basan en la teoría de la fototerapia.<br>
Los parches no están comprobados según los estándares de la medicina convencional y no deben usarse en lugar de la atención médica.</p>
<p style="margin-top:12px">*Garantía de devolución de dinero de 90 días para Clientes Minoristas y Preferidos. Garantía de devolución de 30 días para Socios de Marca Mayoristas.</p>
<p style="margin-top:12px;font-size:11px">Nuestros productos no están destinados a diagnosticar, tratar, curar o prevenir ninguna enfermedad o condición médica. El contenido presentado es de naturaleza general y se proporciona solo con fines informativos. No asumimos responsabilidad por daños o lesiones a personas o propiedades que surjan de cualquier uso de cualquier producto, información, ideas o instrucciones contenidas en los materiales proporcionados.</p>
<p style="margin-top:20px;font-size:14px;color:rgba(255,255,255,.5)">©2026 Pauli Wellness | Todos los derechos reservados.</p>
</div>''', unsafe_allow_html=True)
