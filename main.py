import streamlit as st
import random
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Aprendiendo Telecomunicaciones", page_icon="📡")
# --- COLOCA IMAGEN DE FONDO ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.postimg.cc/52mKJrvV/Chat-GPT-Image-2-mar-2026-11-43-11-p-m.png");
        background-color: #0f172a;
        font-family: "Times New Roman", Times, serif;
        
            /* FORZAR TODO EL TEXTO A BLANCO */
    h1, h2, h3, h4, h5, h6,
    p, div, span, label {
        color: white !important;
        font-family: "Courier New", Courier, monospace !important;
    }

    /* FORZAR TODO EL TEXTO A BLANCO */
    h1, h2, h3, h4, h5, h6,
    p, div, span, label {
        color: white !important;
        font-family: "Courier New", Courier, monospace !important;
    }

    /* BOTONES */
    .stButton>button {
        background-color: #1e293b;
        color: white !important;
        border: 1px solid #00c3ff;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #00c3ff;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# --- 1. BASE DE DATOS DE PRUEBA (El "Pool" de 10 preguntas) ---
#  "Aquí es donde se añaden las preguntas"
if 'pool_preguntas' not in st.session_state:
    st.session_state.pool_preguntas = [
    {"p": "¿Qué significa la sigla RF en telecomunicaciones?",
     "o": ["Radio Frecuencia", "Red Física", "Rango Final", "Registro de Fibra"],
     "c": "Radio Frecuencia"},

    {"p": "¿Qué dispositivo amplifica una señal en telecomunicaciones?",
     "o": ["Router", "Amplificador", "Switch", "Modem"],
     "c": "Amplificador"},

    {"p": "¿Qué medio de transmisión usa luz visible para enviar datos?",
     "o": ["Cable coaxial", "Par trenzado", "Fibra óptica", "Microondas"],
     "c": "Fibra óptica"},

    {"p": "¿Qué unidad se usa para medir frecuencia?",
     "o": ["Voltios", "Hertz", "Ohmios", "Watts"],
     "c": "Hertz"},

    {"p": "¿Qué dispositivo convierte señales digitales a analógicas?",
     "o": ["Switch", "Router", "Módem", "Antena"],
     "c": "Módem"},

    {"p": "¿Qué significa la sigla ISP?",
     "o": ["Internet Service Provider", "Internal Signal Protocol", "Integrated System Port", "Internet Signal Process"],
     "c": "Internet Service Provider"},

    {"p": "¿Qué fenómeno puede afectar la calidad de una señal inalámbrica?",
     "o": ["La Distancia", "El viento", "Gravedad", "Interferencia"],
     "c": "Interferencia"},

    {"p": "¿Qué red cubre un área personal como Bluetooth?",
     "o": ["LAN", "WAN", "PAN", "MAN"],
     "c": "PAN"},

    {"p": "¿Qué protocolo se usa para navegar en páginas web?",
     "o": ["FTP", "HTTP", "SMTP", "SSH"],
     "c": "HTTP"},

    {"p": "¿Qué unidad de medida representa la potencia de una señal?",
     "o": ["dBm", "Segundos", "Bits", "Metros"],
     "c": "dBm"}
]
    # Mezclamos el pool para que no siempre salgan igual
    random.shuffle(st.session_state.pool_preguntas)

TOTAL_PREGUNTAS = len(st.session_state.pool_preguntas)

# --- 2. GESTIÓN DEL ESTADO DEL JUEGO ---
# Usamos session_state para que la App "recuerde" en qué pregunta vamos
if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.juego_terminado = False

# --- 3. FUNCIONES DE AUDIO ---
# Nota : Streamlit puede reproducir audio desde una URL
def reproducir_sonido(url):
    st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

# --- 4. INTERFAZ VISUAL ---
st.markdown(
    """
    <h1 style='text-align: center; 
               font-family: "Courier New", Courier, monospace;
               font-size: 48px;'>         
        Aprendiendo Telecomunicaciones📡
    </h1>
    """,
    unsafe_allow_html=True
)
st.divider()

if not st.session_state.juego_terminado:
    # Barra de progreso (5 preguntas por ronda)
    progreso = (st.session_state.indice) / TOTAL_PREGUNTAS
    st.progress(progreso)
    # Obtenemos la pregunta actual del pool
    pregunta_actual = st.session_state.pool_preguntas[st.session_state.indice]
    
    st.write(f"### {pregunta_actual['p']}")
    
    # Creamos los botones para las opciones
    # El alumno puede cambiar el diseño de estos botones
    opciones = pregunta_actual['o']
    
    # Usamos columnas para que parezca el tablero del programa de TV
    col1, col2 = st.columns(2)
    
    with col1:
        btn_a = st.button(f"A) {opciones[0]}", use_container_width=True)
        btn_b = st.button(f"B) {opciones[1]}", use_container_width=True)
    with col2:
        btn_c = st.button(f"C) {opciones[2]}", use_container_width=True)
        btn_d = st.button(f"D) {opciones[3]}", use_container_width=True)

    # Lógica de respuesta
    seleccion = None
    if btn_a: seleccion = opciones[0]
    if btn_b: seleccion = opciones[1]
    if btn_c: seleccion = opciones[2]
    if btn_d: seleccion = opciones[3]

    if seleccion:
        if seleccion == pregunta_actual['c']:
            st.success("¡CORRECTO! 🌟")
            # AQUÍ PODRÍAS PONER UN SONIDO DE VICTORIA
            # reproducir_sonido("URL_DE_SONIDO_CORRECTO")
            st.session_state.puntos += 2
            time.sleep(1) # Pausa dramática
        else:
            st.error(f"INCORRECTO. La respuesta era: {pregunta_actual['c']} ❌")
            # reproducir_sonido("URL_DE_SONIDO_ERROR")
            time.sleep(1)

        # Avanzamos a la siguiente pregunta
        if st.session_state.indice < TOTAL_PREGUNTAS - 1: # Jugamos todas  las preguntas por ronda
            st.session_state.indice += 1
            st.rerun()
        else:
            st.session_state.juego_terminado = True
            st.rerun()

else:
    # PANTALLA FINAL
    st.header("🏁 ¡El juego ha terminado!")
    max_puntos = TOTAL_PREGUNTAS * 2
    st.metric("PUNTUACIÓN FINAL", f"{st.session_state.puntos} / {max_puntos}")
    
    porcentaje = (st.session_state.puntos / max_puntos) * 100
    st.metric("PORCENTAJE OBTENIDO", f"{porcentaje}%")
    
    if porcentaje >= 80:
        st.balloons()
        st.success("¡Excelente desempeño! 🌟 Nivel suficiente para ser ingeniero en Telecomunicaciones :) ")

    elif porcentaje >= 50:
        st.snow()
        st.info("Buen intento 📚 Sigue reforzando conceptos y llegarás más alto.")

    else:
        st.error("Necesitas estudiar más ☹️ ¡Las telecomunicaciones te esperan!")
    
    if st.button("Reintentar"):
        # Limpiamos todo para empezar de nuevo
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.session_state.juego_terminado = False
        random.shuffle(st.session_state.pool_preguntas)
        st.rerun()
