"""Pauli Wellness - LifeWave Landing Page"""
import streamlit as st
import csv
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="Pauli Wellness | LifeWave", page_icon="✨", layout="wide", initial_sidebar_state="collapsed")
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
def save_csv(fp, row, hdr):
    e = fp.exists()
    with open(fp, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not e: w.writerow(hdr)
        w.writerow(row)
WA = "593939890499"
WA_URL = f"https://wa.me/{WA}?text=Hola%20Pauli!%20Vi%20tu%20pagina%20y%20me%20gustaria%20saber%20mas%20sobre%20los%20parches%20LifeWave"
if "qz" not in st.session_state: st.session_state.qz = 0
if "qa" not in st.session_state: st.session_state.qa = {}
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
*{box-sizing:border-box}
.stApp{background:#FFFFFF!important;color:#373F41!important;font-family:'Inter',sans-serif!important}
.block-container{padding-top:0!important;padding-bottom:0!important;max-width:100%!important}
header[data-testid="stHeader"]{display:none!important}
#MainMenu,footer,.stDeployButton{visibility:hidden!important;display:none!important}
div[data-testid="stSidebarCollapsedControl"]{display:none!important}
.nav{position:fixed;top:0;left:0;right:0;z-index:9999;background:rgba(255,255,255,.95);backdrop-filter:blur(20px);border-bottom:1px solid rgba(25,79,144,.15);padding:12px 40px;display:flex;justify-content:space-between;align-items:center}
.nav-b{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;background:linear-gradient(135deg,#194F90,#5EB3E4);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nav-l{display:flex;gap:24px;align-items:center}
.nav-l a{color:rgba(25,79,144,.75)!important;text-decoration:none!important;font-size:.85rem;font-weight:500;letter-spacing:.5px;text-transform:uppercase;transition:color .3s}
.nav-l a:hover{color:#194F90!important}
.nav-c{background:linear-gradient(135deg,#194F90,#2B6CB0)!important;-webkit-text-fill-color:white!important;-webkit-background-clip:unset!important;padding:8px 20px;border-radius:25px;font-weight:600!important;font-size:.8rem!important}
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:120px 20px 80px;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:conic-gradient(from 0deg at 50% 50%,transparent 0deg,rgba(25,79,144,.03) 60deg,transparent 120deg,rgba(94,179,228,.02) 180deg,transparent 240deg,rgba(236,245,250,.5) 300deg,transparent 360deg);animation:hr 30s linear infinite}
@keyframes hr{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.hero-c{position:relative;z-index:2;max-width:900px}
.badge{display:inline-block;background:rgba(25,79,144,.15);border:1px solid rgba(25,79,144,.3);border-radius:50px;padding:8px 24px;font-size:.8rem;color:#194F90;font-weight:600;letter-spacing:2px;text-transform:uppercase;margin-bottom:24px}
.ht{font-family:'Playfair Display',serif;font-size:clamp(2.5rem,6vw,4.5rem);font-weight:700;line-height:1.1;margin-bottom:24px;color:#194F90}
.gr{background:linear-gradient(135deg,#194F90 0%,#5EB3E4 50%,#2B6CB0 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-size:200% auto;animation:sh 3s ease-in-out infinite}
@keyframes sh{0%,100%{background-position:0% center}50%{background-position:200% center}}
.hs{font-size:clamp(1rem,2vw,1.25rem);color:rgba(55,63,65,.7);line-height:1.7;max-width:650px;margin:0 auto 40px}
.hb{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.bp{display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,#194F90,#2B6CB0);color:white!important;text-decoration:none!important;padding:14px 32px;border-radius:50px;font-weight:600;font-size:.95rem;transition:all .3s;box-shadow:0 4px 25px rgba(25,79,144,.3)}
.bp:hover{transform:translateY(-2px);box-shadow:0 8px 35px rgba(25,79,144,.45)}
.bs{display:inline-flex;align-items:center;gap:8px;background:rgba(25,79,144,.06);border:1px solid rgba(25,79,144,.25);color:#194F90!important;text-decoration:none!important;padding:14px 32px;border-radius:50px;font-weight:600;font-size:.95rem;transition:all .3s}
.bs:hover{background:rgba(25,79,144,.08);border-color:rgba(25,79,144,.5)}
.bw{display:inline-flex;align-items:center;gap:10px;background:linear-gradient(135deg,#25D366,#128C7E);color:white!important;text-decoration:none!important;padding:16px 36px;border-radius:50px;font-weight:700;font-size:1rem;transition:all .3s;box-shadow:0 4px 25px rgba(37,211,102,.3)}
.bw:hover{transform:translateY(-3px);box-shadow:0 8px 35px rgba(37,211,102,.45)}
.sec{padding:100px 20px;position:relative}
.tg{display:inline-block;background:rgba(25,79,144,.12);border:1px solid rgba(25,79,144,.25);border-radius:50px;padding:6px 20px;font-size:.75rem;color:#194F90;font-weight:600;letter-spacing:2px;text-transform:uppercase;margin-bottom:16px}
.st{font-family:'Playfair Display',serif;font-size:clamp(2rem,4vw,3rem);font-weight:700;color:#194F90;line-height:1.2;margin-bottom:16px}
.ss{font-size:1.05rem;color:rgba(55,63,65,.65);line-height:1.7;max-width:600px}
.stats{display:flex;justify-content:center;gap:60px;flex-wrap:wrap;padding:60px 20px;background:rgba(25,79,144,.04);border-top:1px solid rgba(25,79,144,.1);border-bottom:1px solid rgba(25,79,144,.1)}
.stat{text-align:center}
.sn{font-family:'Playfair Display',serif;font-size:2.8rem;font-weight:700;background:linear-gradient(135deg,#194F90,#5EB3E4);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.sl{font-size:.8rem;color:rgba(55,63,65,.55);text-transform:uppercase;letter-spacing:2px;margin-top:4px}
.gc{background:rgba(236,245,250,.8);border:1px solid rgba(25,79,144,.06);border-radius:20px;padding:32px;backdrop-filter:blur(10px);transition:all .4s;height:100%}
.gc:hover{transform:translateY(-8px);border-color:rgba(25,79,144,.3);box-shadow:0 20px 60px rgba(25,79,144,.1)}
.ci{font-size:2.5rem;margin-bottom:16px}
.ct{font-size:1.15rem;font-weight:700;color:#194F90;margin-bottom:10px}
.cx{font-size:.9rem;color:rgba(55,63,65,.65);line-height:1.6}
.pc{background:rgba(236,245,250,.8);border:1px solid rgba(25,79,144,.06);border-radius:24px;overflow:hidden;transition:all .4s;margin-bottom:24px}
.pc:hover{transform:translateY(-8px);border-color:rgba(25,79,144,.4);box-shadow:0 20px 60px rgba(25,79,144,.15)}
.pi{width:100%;height:240px;object-fit:cover;display:block}
.pf{padding:24px}
.pk{font-size:.7rem;color:#194F90;text-transform:uppercase;letter-spacing:2px;font-weight:600;margin-bottom:8px}
.pn{font-size:1.2rem;font-weight:700;color:#194F90;margin-bottom:8px}
.pd{font-size:.85rem;color:rgba(55,63,65,.55);line-height:1.5;margin-bottom:16px}
.tc{background:rgba(236,245,250,.8);border:1px solid rgba(25,79,144,.06);border-radius:20px;padding:32px;transition:all .3s}
.tc:hover{border-color:rgba(25,79,144,.3)}
.tq{font-size:3rem;color:rgba(25,79,144,.3);font-family:'Playfair Display',serif;line-height:1;margin-bottom:8px}
.tt{font-size:.95rem;color:rgba(55,63,65,.8);line-height:1.7;font-style:italic;margin-bottom:16px}
.ta{font-size:.85rem;font-weight:600;color:#194F90}
.ts{color:#FFD700;font-size:.9rem;margin-bottom:12px}
.qc{background:linear-gradient(135deg,rgba(25,79,144,.08),rgba(94,179,228,.05));border:1px solid rgba(25,79,144,.2);border-radius:24px;padding:48px;max-width:700px;margin:0 auto}
.qp{height:4px;background:rgba(25,79,144,.08);border-radius:2px;margin-bottom:32px;overflow:hidden}
.qpb{height:100%;background:linear-gradient(90deg,#194F90,#5EB3E4);border-radius:2px;transition:width .5s}
.qq{font-size:1.3rem;font-weight:600;color:#194F90;margin-bottom:24px;text-align:center}
.snum{width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#194F90,#2B6CB0);display:flex;align-items:center;justify-content:center;font-size:1.4rem;font-weight:800;color:white;margin:0 auto 16px}
.sc{background:rgba(236,245,250,.8);border:1px solid rgba(25,79,144,.06);border-radius:20px;padding:32px 24px;text-align:center;transition:all .4s;height:100%}
.sc:hover{transform:translateY(-5px);border-color:rgba(25,79,144,.3)}
.foot{text-align:center;padding:40px 20px;border-top:1px solid rgba(25,79,144,.12);background:#27455C;color:rgba(255,255,255,.6);font-size:.75rem}
.foot a{color:rgba(94,179,228,.9)!important;text-decoration:none!important}
.waf{position:fixed;bottom:24px;right:24px;z-index:9999;width:60px;height:60px;background:#25D366;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 25px rgba(37,211,102,.4);transition:all .3s;animation:bn 2s infinite}
.waf:hover{transform:scale(1.1)}
.waf svg{width:32px;height:32px;fill:white}
@keyframes bn{0%,20%,50%,80%,100%{transform:translateY(0)}40%{transform:translateY(-8px)}60%{transform:translateY(-4px)}}
@keyframes fu{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
@keyframes fd{from{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:translateY(0)}}
.stTextInput>div>div>input,.stTextArea>div>div>textarea{background:rgba(25,79,144,.04)!important;border:1px solid rgba(25,79,144,.15)!important;border-radius:12px!important;color:#373F41!important;font-family:'Inter',sans-serif!important;padding:12px 16px!important}
.stTextInput>div>div>input:focus,.stTextArea>div>div>textarea:focus{border-color:#194F90!important;box-shadow:0 0 0 2px rgba(25,79,144,.2)!important}
.stRadio>div{background:rgba(236,245,250,1)!important;border-radius:12px!important;padding:12px!important}
div.stButton>button{background:linear-gradient(135deg,#194F90,#2B6CB0)!important;color:white!important;border:none!important;border-radius:50px!important;padding:12px 32px!important;font-weight:600!important;font-family:'Inter',sans-serif!important;transition:all .3s!important;box-shadow:0 4px 20px rgba(25,79,144,.3)!important}
div.stButton>button:hover{transform:translateY(-2px)!important;box-shadow:0 8px 30px rgba(25,79,144,.45)!important}
@media(max-width:768px){.nav{padding:10px 16px}.nav-l{display:none}.stats{gap:30px}.hero{padding:100px 16px 60px}.sec{padding:60px 16px}.qc{padding:32px 20px}}
</style>""", unsafe_allow_html=True)
# NAV
st.markdown(f"""<div class="nav"><div class="nav-b">✨ Pauli Wellness</div><div class="nav-l"><a href="#productos">Productos</a><a href="#ciencia">Ciencia</a><a href="#resultados">Resultados</a><a href="#experiencias">Testimonios</a><a href="#equipo">Unete</a><a href="{WA_URL}" target="_blank" class="nav-c">Contactame</a></div></div>""", unsafe_allow_html=True)
# WHATSAPP FLOAT
st.markdown(f"""<a href="{WA_URL}" target="_blank" class="waf" title="WhatsApp"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.8-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.3-5-3.7-10.5-6.6z"/></svg></a>""", unsafe_allow_html=True)
# HERO
st.markdown(f"""<div class="hero"><div class="hero-c"><div class="badge">Tecnologia Patentada · +200 Patentes Mundiales</div><h1 class="ht">Tu cuerpo sabe sanarse.<br/><span class="gr">Solo necesita recordar como.</span></h1><p class="hs">Descubre la fototerapia que activa tus celulas madre con luz — sin quimicos, sin inyecciones, sin efectos secundarios. Respaldado por ciencia real y mas de 80 estudios clinicos.</p><div class="hb"><a href="{WA_URL}" target="_blank" class="bp">Quiero Saber Mas</a><a href="#ciencia" class="bs">Ver la Ciencia</a></div></div></div>""", unsafe_allow_html=True)
# STATS
st.markdown("""<div class="stats"><div class="stat"><div class="sn">200+</div><div class="sl">Patentes Mundiales</div></div><div class="stat"><div class="sn">80+</div><div class="sl">Estudios Clinicos</div></div><div class="stat"><div class="sn">20+</div><div class="sl">Anos de Investigacion</div></div><div class="stat"><div class="sn">80+</div><div class="sl">Paises</div></div></div>""", unsafe_allow_html=True)
# PROBLEM
st.markdown("""<div class="sec" style="text-align:center"><div class="tg">El Problema</div><h2 class="st" style="max-width:700px;margin:0 auto 16px">A medida que envejecemos, nuestras celulas se ralentizan</h2><p class="ss" style="margin:0 auto 48px;max-width:600px">Menos celulas activas significa recuperacion mas lenta, menos energia y signos visibles de envejecimiento.</p></div>""", unsafe_allow_html=True)
pc = st.columns(4)
for i,(icon,t,d) in enumerate([("😴","Fatiga y Baja Energia","Te sientes agotado/a sin razon aparente."),("🤕","Dolor y Rigidez","Dolores articulares y musculares que limitan tu dia a dia."),("😶‍🌫️","Sueno Deficiente","No logras un descanso profundo y reparador."),("🪞","Envejecimiento Visible","Lineas de expresion, piel opaca, cabello debilitado.")]):
    with pc[i]:
        st.markdown(f'<div class="gc"><div class="ci">{icon}</div><div class="ct">{t}</div><div class="cx">{d}</div></div>', unsafe_allow_html=True)
# SOLUTION
st.markdown(f"""<div class="sec" style="text-align:center"><div style="background:linear-gradient(135deg,rgba(25,79,144,.1),rgba(94,179,228,.06));border:1px solid rgba(25,79,144,.2);border-radius:24px;padding:48px 32px;max-width:900px;margin:0 auto"><div class="tg" style="background:rgba(94,179,228,.15);border-color:rgba(94,179,228,.3);color:#2B6CB0">La Solucion</div><h2 class="st" style="margin-bottom:16px">No es una pastilla, crema ni inyeccion.<br/><span style="background:linear-gradient(135deg,#194F90,#5EB3E4);-webkit-background-clip:text;-webkit-text-fill-color:transparent">Es una categoria completamente nueva.</span></h2><p class="ss" style="margin:0 auto;max-width:650px">Un parche no transdermico que usa luz para enviar una senal a tus celulas. Nada entra en tu cuerpo. Solo activa lo que ya esta dentro de ti.</p></div></div>""", unsafe_allow_html=True)
# SCIENCE
st.markdown('<div id="ciencia"></div>', unsafe_allow_html=True)
st.markdown("""<div class="sec"><div style="text-align:center;margin-bottom:48px"><div class="tg">La Ciencia</div><h2 class="st">Por que la luz?</h2><p class="ss" style="margin:0 auto">La fototerapia tiene mas de 100 anos de historia cientifica.</p></div></div>""", unsafe_allow_html=True)
s1,s2 = st.columns(2)
with s1:
    st.markdown("""<div class="gc" style="height:auto"><div class="ci">💡</div><div class="ct" style="font-size:1.3rem">Como Funciona?</div><div class="cx" style="margin-bottom:16px">La luz es informacion, y tu cuerpo siempre esta a la escucha. Nuestro parche patentado refleja longitudes de onda especificas de luz que estimulan la piel para elevar <strong style="color:#5EB3E4">GHK-Cu</strong>, el peptido de cobre clinicamente probado para reparar y regenerar celulas.</div><div class="cx">Es como la acupuntura unida a la biologia cuantica — sin agujas ni complejidades.</div></div>""", unsafe_allow_html=True)
with s2:
    st.markdown("""<div class="gc" style="height:auto"><div class="ci">🧬</div><div class="ct" style="font-size:1.3rem">GHK-Cu: El Superpeptido</div><div class="cx" style="margin-bottom:16px">A medida que envejecemos, los niveles naturales de GHK-Cu disminuyen drasticamente. Con ellos, nuestra capacidad de reparacion y regeneracion.</div><div class="cx" style="margin-bottom:16px">Esta clinicamente probado que nuestro parche eleva GHK-Cu a <strong style="color:#194F90">niveles juveniles</strong>.</div><div style="background:rgba(25,79,144,.1);border-radius:12px;padding:16px;margin-top:8px"><div style="font-size:.8rem;color:rgba(255,255,255,.6)">✅ +4,000 genes se resetean · ✅ Aumento del 73% en GHK-Cu · ✅ Reduccion visible de arrugas</div></div></div>""", unsafe_allow_html=True)
# PRODUCTS
st.markdown('<div id="productos"></div>', unsafe_allow_html=True)
st.markdown("""<div class="sec"><div style="text-align:center;margin-bottom:48px"><div class="tg">Productos</div><h2 class="st">Conoce la Linea LifeWave</h2><p class="ss" style="margin:0 auto">Cada parche esta disenado para activar una respuesta especifica en tu cuerpo.</p></div></div>""", unsafe_allow_html=True)
prods = [("✨","ESTRELLA","X39","Activa celulas madre, eleva GHK-Cu y rejuvenece tu cuerpo desde adentro."),("⚡","RENDIMIENTO","X49","Mejora la resistencia fisica y la recuperacion muscular."),("🌙","BIENESTAR","Aeon","Reduce el estres oxidativo y promueve la calma interior."),("😴","DESCANSO","Silent Nights","Mejora la calidad del sueno sin quimicos ni melatonina."),("🔋","ENERGIA","Energy Enhancer","Aumenta la energia natural y la resistencia fisica."),("❄️","ALIVIO","IceWave","Alivia el dolor de forma natural y sin medicamentos.")]
cols = st.columns(3)
for i,(icon,cat,name,desc) in enumerate(prods):
    with cols[i%3]:
        st.markdown(f'<div class="pc"><div class="pf"><div class="pk">{cat}</div><div class="pn">{icon} {name}</div><div class="pd">{desc}</div><a href="{WA_URL}" target="_blank" class="bp" style="font-size:.8rem;padding:10px 24px;width:100%;justify-content:center">Consultar</a></div></div>', unsafe_allow_html=True)
# HOW IT WORKS
st.markdown("""<div class="sec"><div style="text-align:center;margin-bottom:48px"><div class="tg">Como Empezar</div><h2 class="st">4 Pasos Simples</h2></div></div>""", unsafe_allow_html=True)
steps = [("#194F90","1","Contactame","Escribeme por WhatsApp y cuéntame tu situacion."),("#5EB3E4","2","Evaluacion","Te ayudo a elegir el parche ideal para ti."),("#FFD700","3","Aplicacion","Coloca tu parche y deja que la luz haga el trabajo."),("#D98471","4","Resultados","Siente la diferencia en los primeros dias.")]
sc = st.columns(4)
for i,(color,num,title,desc) in enumerate(steps):
    with sc[i]:
        st.markdown(f'<div class="sc"><div class="snum" style="background:{color}">{num}</div><div class="ct">{title}</div><div class="cx">{desc}</div></div>', unsafe_allow_html=True)
# QUIZ
st.markdown('<div id="resultados"></div>', unsafe_allow_html=True)
st.markdown("""<div class="sec" style="text-align:center"><div class="tg">Descubre tu Parche</div><h2 class="st">Cual es el parche ideal para ti?</h2><p class="ss" style="margin:0 auto 40px">Responde 3 preguntas y te recomendamos el producto perfecto.</p></div>""", unsafe_allow_html=True)
qs = [("Cual es tu principal preocupacion?",["Falta de energia","Dolor cronico","Mal dormir","Envejecimiento"]),("Que edad tienes?",["25-35","36-45","46-55","56+"]),("Has probado parches antes?",["Si","No","No se que son"])]
if st.session_state.qz < len(qs):
    q,opts = qs[st.session_state.qz]
    st.markdown(f'<div class="qc"><div class="qp"><div class="qpb" style="width:{(st.session_state.qz+1)/len(qs)*100}%"></div></div><div class="qq">{q}</div></div>', unsafe_allow_html=True)
    ans = st.radio("", opts, key=f"q{st.session_state.qz}", label_visibility="collapsed")
    if st.button("Siguiente →" if st.session_state.qz < len(qs)-1 else "Ver Resultado"):
        st.session_state.qa[st.session_state.qz] = ans
        st.session_state.qz += 1
        st.rerun()
else:
    recs = {"Falta de energia":"Energy Enhancer + X39","Dolor cronico":"IceWave + X39","Mal dormir":"Silent Nights + Aeon","Envejecimiento":"X39 + Aeon"}
    rec = recs.get(st.session_state.qa.get(0,""), "X39")
    st.markdown(f"""<div class="qc" style="text-align:center"><div style="font-size:3rem;margin-bottom:16px">🎯</div><div class="st" style="font-size:1.5rem">Tu combinacion ideal:</div><div style="font-size:1.8rem;font-weight:800;background:linear-gradient(135deg,#194F90,#5EB3E4);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:16px 0">{rec}</div><a href="{WA_URL}" target="_blank" class="bw" style="margin-top:16px">📲 Consultar por WhatsApp</a></div>""", unsafe_allow_html=True)
    if st.button("Repetir Quiz"):
        st.session_state.qz = 0
        st.session_state.qa = {}
        st.rerun()
# BENEFITS
st.markdown("""<div class="sec"><div style="text-align:center;margin-bottom:48px"><div class="tg">Beneficios</div><h2 class="st">Por que elegir LifeWave?</h2></div></div>""", unsafe_allow_html=True)
bens = [("🧬","Celulas Madre","Activa la regeneracion celular natural."),("💊","Sin Quimicos","Nada entra en tu cuerpo. 100% no invasivo."),("📊","Clinicamente Probado","Mas de 80 estudios respaldan la tecnologia."),("⚡","Resultados Rapidos","Muchos usuarios sienten cambios en horas."),("🌍","Global","Disponible en mas de 80 paises."),("🏆","Patentado","Mas de 200 patentes mundiales protegen esta tecnologia.")]
bc = st.columns(3)
for i,(icon,t,d) in enumerate(bens):
    with bc[i%3]:
        st.markdown(f'<div class="gc" style="text-align:center;margin-bottom:24px"><div class="ci">{icon}</div><div class="ct">{t}</div><div class="cx">{d}</div></div>', unsafe_allow_html=True)
# TESTIMONIALS
st.markdown('<div id="experiencias"></div>', unsafe_allow_html=True)
st.markdown("""<div class="sec"><div style="text-align:center;margin-bottom:48px"><div class="tg">Experiencias</div><h2 class="st">Lo que dicen nuestros usuarios</h2></div></div>""", unsafe_allow_html=True)
tests = [("⭐⭐⭐⭐⭐","Despues de 2 semanas con X39, mi energia cambio completamente. Ya no necesito 3 cafes al dia.","Maria G., 45 anos"),("⭐⭐⭐⭐⭐","Llevaba anos con dolor de rodillas. Con IceWave senti alivio desde el primer dia.","Carlos R., 58 anos"),("⭐⭐⭐⭐⭐","Mis amigas me preguntan que me hice en la cara. Solo uso X39 y Aeon.","Laura M., 52 anos")]
tc = st.columns(3)
for i,(stars,quote,author) in enumerate(tests):
    with tc[i]:
        st.markdown(f'<div class="tc"><div class="ts">{stars}</div><div class="tq">"</div><div class="tt">{quote}</div><div class="ta">— {author}</div></div>', unsafe_allow_html=True)
# ABOUT
st.markdown(f"""<div class="sec" style="text-align:center"><div style="background:linear-gradient(135deg,rgba(25,79,144,.08),rgba(94,179,228,.05));border:1px solid rgba(25,79,144,.2);border-radius:24px;padding:48px;max-width:800px;margin:0 auto"><div style="font-size:4rem;margin-bottom:16px">👩‍⚕️</div><div class="tg">Tu Guia</div><h2 class="st">Soy Pauli</h2><p class="ss" style="margin:0 auto 24px;max-width:550px">Brand Partner oficial de LifeWave. Mi mision es ayudarte a descubrir el poder de la fototerapia y acompanarte en tu camino hacia el bienestar.</p><a href="{WA_URL}" target="_blank" class="bw">📲 Habla Conmigo</a></div></div>""", unsafe_allow_html=True)
# JOIN TEAM
st.markdown('<div id="equipo"></div>', unsafe_allow_html=True)
st.markdown("""<div class="sec" style="text-align:center"><div class="tg">Oportunidad</div><h2 class="st">Unete al Equipo</h2><p class="ss" style="margin:0 auto 32px">Emprende tu propio negocio con LifeWave. Te acompano paso a paso.</p></div>""", unsafe_allow_html=True)
with st.form("join"):
    c1,c2 = st.columns(2)
    jn = c1.text_input("Nombre completo")
    je = c2.text_input("Email")
    jt = c1.text_input("Telefono / WhatsApp")
    jc = c2.text_input("Ciudad / Pais")
    jm = st.text_area("Por que te interesa LifeWave?", height=100)
    if st.form_submit_button("Quiero Unirme al Equipo"):
        if jn and je:
            save_csv(DATA_DIR/"team.csv", [datetime.now().isoformat(),jn,je,jt,jc,jm], ["fecha","nombre","email","telefono","ciudad","motivacion"])
            st.success("Gracias! Pauli te contactara pronto.")
        else:
            st.warning("Por favor completa nombre y email.")
# CONTACT
st.markdown("""<div class="sec" style="text-align:center"><div class="tg">Contacto</div><h2 class="st">Tienes preguntas?</h2><p class="ss" style="margin:0 auto 32px">Escribeme y te respondo personalmente.</p></div>""", unsafe_allow_html=True)
with st.form("contact"):
    cc1,cc2 = st.columns(2)
    cn = cc1.text_input("Tu nombre")
    ce = cc2.text_input("Tu email")
    cm = st.text_area("Tu mensaje", height=100)
    if st.form_submit_button("Enviar Mensaje"):
        if cn and ce and cm:
            save_csv(DATA_DIR/"contacts.csv", [datetime.now().isoformat(),cn,ce,cm], ["fecha","nombre","email","mensaje"])
            st.success("Mensaje enviado! Te respondere pronto.")
        else:
            st.warning("Por favor completa todos los campos.")
# CTA
st.markdown(f"""<div class="sec" style="text-align:center;padding:80px 20px"><h2 class="st" style="font-size:clamp(2rem,5vw,3.5rem)">Listo para <span class="gr">transformar tu bienestar</span>?</h2><p class="ss" style="margin:0 auto 32px;max-width:550px">Miles de personas ya estan experimentando los beneficios de LifeWave. Tu siguiente paso esta a un mensaje de distancia.</p><a href="{WA_URL}" target="_blank" class="bw" style="font-size:1.1rem;padding:18px 40px">📲 Contactar a Pauli por WhatsApp</a></div>""", unsafe_allow_html=True)
# FAQ
st.markdown("""<div class="sec"><div style="text-align:center;margin-bottom:48px"><div class="tg">FAQ</div><h2 class="st">Preguntas Frecuentes</h2></div></div>""", unsafe_allow_html=True)
faqs = [("Es seguro?","Si. Los parches LifeWave son 100% no invasivos. Nada entra en tu cuerpo. Estan respaldados por mas de 80 estudios clinicos y tienen certificaciones internacionales."),("Como funciona la fototerapia?","Tu cuerpo emite calor (luz infrarroja). Nuestros parches reflejan longitudes de onda especificas que estimulan la piel y activan respuestas biologicas como la produccion de peptidos regenerativos."),("Cuanto tiempo tarda en hacer efecto?","Muchos usuarios reportan cambios en las primeras horas. Los resultados optimos se ven entre 1-3 meses de uso continuo."),("Puedo usar varios parches a la vez?","Si. De hecho, las combinaciones de parches potencian los resultados. Te ayudo a encontrar la combinacion perfecta para ti."),("Tiene efectos secundarios?","No se han reportado efectos secundarios significativos. Al ser no transdermico, no introduce sustancias en tu cuerpo."),("Como puedo comprar?","Contactame directamente por WhatsApp. Te guio en todo el proceso y te ayudo a elegir los productos ideales para ti.")]
for q,a in faqs:
    with st.expander(q):
        st.write(a)
# FOOTER
st.markdown(f"""<div class="foot"><p>© 2024 Pauli Wellness · Brand Partner Independiente de <a href="https://www.lifewave.com" target="_blank">LifeWave</a></p><p style="margin-top:8px">📱 <a href="{WA_URL}" target="_blank">WhatsApp</a> · Ecuador 🇪🇨</p><p style="margin-top:16px;font-size:.65rem;color:rgba(255,255,255,.35)">Los parches LifeWave no son dispositivos medicos y no estan destinados a diagnosticar, tratar, curar o prevenir ninguna enfermedad.</p></div>""", unsafe_allow_html=True)
# SIDEBAR LEAD CAPTURE
with st.sidebar:
    st.markdown("### 🎁 Guia Gratis")
    st.markdown("Descarga nuestra guia sobre fototerapia y celulas madre.")
    with st.form("lead"):
        ln = st.text_input("Tu nombre")
        le = st.text_input("Tu email")
        if st.form_submit_button("Descargar Guia"):
            if ln and le:
                save_csv(DATA_DIR/"leads.csv", [datetime.now().isoformat(),ln,le], ["fecha","nombre","email"])
                st.success("Revisa tu WhatsApp! Te enviare la guia.")
            else:
                st.warning("Completa nombre y email.")
