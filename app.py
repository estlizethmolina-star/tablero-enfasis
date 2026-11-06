# =============================================================================
# TABLERO INTERACTIVO: EL NARCOTRÁFICO EN EL CONFLICTO COLOMBIANO
# Enfoque: Financiación, Carteles, Pablo Escobar, Geografía y Persistencia Actual
# =============================================================================

import streamlit as st
import pandas as pd

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Narcotráfico y Conflicto en Colombia - Tablero Educativo",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# SECCIÓN 1: MENÚ LATERAL DE NAVEGACIÓN (6 Módulos Especializados)
# =============================================================================
with st.sidebar:
    st.header("🗺️ Estructura del Conflicto")
    opcion_menu = st.radio(
        "Seleccione un módulo de análisis:",
        [
            "1. Narcotráfico como Gasolina del Conflicto",
            "2. El Triángulo de Galtung (Violencia y Narcotráfico)",
            "3. La Era de los Grandes Carteles (Medellín y Cali)",
            "4. Pablo Escobar y el Narcoterrorismo",
            "5. Geografía de la Droga y Corredores de Violencia",
            "6. Persistencia Actual y Políticas de Erradicación"
        ]
    )
    st.write("---")
    st.info("💡 **Enfoque Académico:** Este tablero analiza de forma rigurosa el impacto del narcotráfico como combustible financiero y degradador del conflicto armado en Colombia.")

# =============================================================================
# SECCIÓN 2: DESARROLLO DE LOS MÓDULOS
# =============================================================================

# -----------------------------------------------------------------------------
# MÓDULO 1: NARCOTRÁFICO COMO GASOLINA DEL CONFLICTO
# -----------------------------------------------------------------------------
if opcion_menu == "1. Narcotráfico como Gasolina del Conflicto":
    st.title("🔥 Módulo 1: El Narcotráfico como Gasolina de la Violencia")
    st.subheader("La transformación económica del conflicto armado")

    st.markdown("""
    El conflicto colombiano nació originalmente de tensiones políticas y agrarias. Sin embargo, en los años 80,
    el ingreso masivo de dólares del narcotráfico actuó como **combustible financiero** de todos los grupos armados.

    ### Impacto Estructural en el Conflicto:
    * **Financiamiento de Ejércitos:** Tanto guerrillas (FARC, ELN) como grupos paramilitares (AUC) multiplicaron sus combatientes y compraron armamento militar avanzado gracias a impuestos sobre la hoja de coca y al control de laboratorios.
    * **Prolongación de la Guerra:** Al contar con rentas ilícitas autónomas e ilimitadas, los actores armados ya no dependían del apoyo o legitimidad de la población civil, lo que les permitió sostener el conflicto por décadas.
    * **Degradación Ética:** Los ideales originales de cambio social o defensa agraria se desdibujaron, convirtiendo el control territorial en un fin estrictamente lucrativo.
    """)

    st.subheader("📊 Tabla de Contraste Histórico")
    datos_ejemplo = {
        "Variable de Análisis": [
            "Gasto de Defensa Nacional (% del PIB)",
            "Capacidad Militar de Grupos Armados",
            "Tasa de Homicidios (Promedio Nacional por 100k hab.)",
            "Sometimiento / Negociaciones de Paz"
        ],
        "Antes del Auge Narcotraficante (Años 70)": ["~1.5%", "Baja (Armas rudimentarias, presencia aislada)", "~25 (Normal regional)", "Búsqueda de salidas políticas comunes"],
        "Durante el Auge Narco-Conflicto (Años 90 - 2000s)": ["~4.3%", "Alta (Fusiles modernos, comunicaciones satelitales, dominio de regiones)", "~70 (Picos históricos de violencia extrema)", "Prolongación por abundancia de recursos financieros"]
    }
    df_impacto = pd.DataFrame(datos_ejemplo)
    st.table(df_impacto)

# -----------------------------------------------------------------------------
# MÓDULO 2: EL TRIÁNGULO DE GALTUNG
# -----------------------------------------------------------------------------
elif opcion_menu == "2. El Triángulo de Galtung (Violencia y Narcotráfico)":
    st.title("🔺 Módulo 2: El Triángulo de la Violencia de Johan Galtung")
    st.subheader("Marco conceptual para entender las raíces y síntomas de la violencia")

    st.write("Selecciona una dimensión para evaluar cómo se vincula con la economía de la droga:")

    dimension = st.radio(
        "Dimensión:",
        ["💥 Violencia Directa", "🏗️ Violencia Estructural", "🧠 Violencia Cultural"],
        horizontal=True,
        index=None
    )

    st.write("---")

    if dimension == "💥 Violencia Directa":
        st.error("### Violencia Directa (El Síntoma Visible)\nMasacres de campesinos, secuestros sistemáticos, ataques con carros bomba en ciudades, el asesinato de líderes sociales y los combates de control territorial. Es la manifestación física y armada más evidente financiada por la coca.")
    elif dimension == "🏗️ Violencia Estructural":
        st.warning("### Violencia Estructural (La Raíz de la Siembra)\nLa pobreza extrema del campesino rural, la ausencia de vías para transportar productos lícitos y el abandono de la justicia estatal. Esta exclusión histórica empuja a las comunidades a sembrar cocaína como su única opción para no morir de hambre.")
    elif dimension == "🧠 Violencia Cultural":
        st.info("### Violencia Cultural (La Legitimación de la Droga)\nLa narco-cultura imperante que rinde culto al dinero rápido, al lujo y al poder de las armas. Esta mentalidad desvaloriza el trabajo honesto y legitima la delincuencia como método rápido de ascenso social.")
    else:
        st.caption("👆 Elige uno de los tres componentes de arriba para analizar la violencia bajo la teoría de paz de Galtung.")

# -----------------------------------------------------------------------------
# MÓDULO 3: LA ERA DE LOS GRANDES CARTELES (MEDELLÍN Y CALI)
# -----------------------------------------------------------------------------
elif opcion_menu == "3. La Era de los Grandes Carteles (Medellín y Cali)":
    st.title("🏢 Módulo 3: Los Grandes Carteles y la Historia de Violencia")
    st.subheader("El surgimiento de imperios transnacionales del crimen")

    st.markdown("""
    Durante los años 80 y principios de los 90, los **Carteles de Medellín y Cali** industrializaron el tráfico de cocaína a escala global,
    lo que desató repercusiones devastadoras para la historia de Colombia.

    ### Las dos caras de la industrialización criminal:
    * **El Cartel de Medellín:** Se caracterizó por un choque violento, directo y frontal contra el Estado. Construyeron redes de sicariato compuestas por jóvenes de comunas vulnerables, convirtiendo a las grandes ciudades en campos de batalla.
    * **El Cartel de Cali:** Optó por una estrategia más silenciosa de infiltración a través de la corrupción económica. Compraron sectores de la policía, de la justicia, del sector empresarial e incluso campañas presidenciales (como el Proceso 8.000), debilitando gravemente la moralidad del Estado.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.info("**Consecuencia Social:** Los carteles crearon milicias y financiaron autodefensas para proteger sus laboratorios de las guerrillas, originando el surgimiento del paramilitarismo moderno.")
    with col2:
        st.warning("**Consecuencia Económica:** El lavado de activos a gran escala en el sector inmobiliario y el campo provocó un aumento masivo de tierras improductivas y una desigual contrarreforma agraria.")

# -----------------------------------------------------------------------------
# MÓDULO 4: PABLO ESCOBAR Y EL NARCOTERRORISMO
# -----------------------------------------------------------------------------
elif opcion_menu == "4. Pablo Escobar y el Narcoterrorismo":
    st.title("💵 Módulo 4: Pablo Escobar y su Aporte Directo a la Violencia")
    st.subheader("La guerra armada de un solo individuo contra una nación")

    st.markdown("""
    La figura de **Pablo Escobar** representa el punto máximo en el que el narcotráfico desafió abiertamente el monopolio de la fuerza del Estado.
    Su lema de *'plata o plomo'* doblegó voluntades e impuso el terror como doctrina política.

    ### Hitos de la violencia liderada por Escobar:
    * **La Lucha contra la Extradición:** Para evitar ser juzgado en Estados Unidos, Escobar creó el grupo *'Los Extraditables'* bajo la consigna: *'Preferimos una tumba en Colombia a un calabozo en Estados Unidos'*.
    * **El Narcoterrorismo Urbano:** Introdujo el uso masivo de carros bomba en Bogotá y Medellín, atacando centros comerciales, sedes del DAS (inteligencia del Estado) e incluso haciendo estallar en pleno vuelo el avión de Avianca 203.
    * **Magnicidios de Líderes:** Ordenó el asesinato del ministro de Justicia Rodrigo Lara Bonilla, el director del diario El Espectador Guillermo Cano, y el candidato presidencial favorito Luis Carlos Galán, asestando golpes letales a la democracia.
    """)

    st.error("⚠️ **El legado del Sicariato:** Escobar institucionalizó el sicariato juvenil pagando recompensas por cada policía asesinado, sembrando una cultura de desprecio por la vida que hoy en día aún resuena en las periferias urbanas.")

# -----------------------------------------------------------------------------
# MÓDULO 5: GEOGRAFÍA DE LA DROGA Y CORREDORES DE VIOLENCIA
# -----------------------------------------------------------------------------
elif opcion_menu == "5. Geografía de la Droga y Corredores de Violencia":
    st.title("🗺️ Módulo 5: Geografía del Conflicto, Cultivos y Fronteras")
    st.subheader("¿Por qué la violencia ocurre en lugares específicos del mapa?")

    st.markdown("""
    La violencia ligada al narcotráfico no se distribuye de manera uniforme. Se concentra estratégicamente en corredores logísticos fluviales,
    salidas al mar y fronteras terrestres, donde los grupos ilegales disputan el territorio.
    """)

    # Coordenadas estratégicas de alta disputa en Colombia
    datos_geograficos = {
        'lat': [8.58, 1.61, 7.30, 1.83],
        'lon': [-72.93, -75.60, -76.18, -78.75],
        'Zona Crítica': [
            'Catatumbo (Salida estratégica y frontera porosa)',
            'Caquetá (Núcleo histórico de retaguardia armada)',
            'Urabá (Punto clave de exportación marítima hacia el Caribe)',
            'Tumaco (Puerto natural de salida en el Pacífico)'
        ],
        'Razón del Conflicto': [
            'Disputas territoriales para el paso fronterizo de insumos y droga.',
            'Grandes extensiones de tierra propicias para plantación y laboratorios.',
            'Control absoluto de rutas marítimas y exportación para carteles internacionales.',
            'Ubicación clave para despacho rápido en lanchas rápidas y semisumergibles.'
        ]
    }
    df_mapa = pd.DataFrame(datos_geograficos)
    st.map(df_mapa)

    st.write("**💡 Conclusión Geográfica:** El verdadero motor de la violencia armada no radica en cultivar la hoja de coca, sino en controlar los canales de exportación para maximizar el valor de la droga procesada.")

# -----------------------------------------------------------------------------
# MÓDULO 6: PERSISTENCIA ACTUAL Y POLÍTICAS DE ERRADICACIÓN
# -----------------------------------------------------------------------------
elif opcion_menu == "6. Persistencia Actual y Políticas de Erradicación":
    st.title("✈️ Módulo 6: ¿Por qué sigue afectándonos la violencia y la cocaína hoy?")
    st.subheader("El círculo vicioso del narcotráfico y la búsqueda de paz")

    st.markdown("""
    A pesar de la caída de Escobar, el desmantelamiento de los carteles y la firma del Acuerdo de Paz de 2016 con las FARC, el narcotráfico sigue activo.
    Los antiguos frentes armados se fragmentaron en disidencias de guerrillas, grupos paramilitares (Clan del Golfo) y pandillas urbanas, manteniendo viva la violencia.
    """)

    mecanismo = st.radio("Selecciona una problemática para analizar en clase:", [
        "El 'Efecto Globo' en la siembra de Coca",
        "Fumigación con Glifosato vs. Sustitución Voluntaria"
    ])

    st.write("---")

    if mecanismo == "El 'Efecto Globo' en la siembra de Coca":
        st.info("### El Efecto Globo\nEste concepto explica que erradicar forzadamente los cultivos de coca en un municipio no elimina la demanda del mercado; simplemente desplaza la siembra (se infla en otra parte) hacia parques nacionales protegidos, reservas indígenas o zonas fronterizas donde el control del Estado es ausente.")
    else:
        st.warning("### El Debate de las Políticas de Erradicación\n* **Glifosato (Aspersión Aérea):** Rápida y abarca grandes áreas de difícil acceso, pero genera daños colaterales a la salud, destruye los cultivos de comida de los campesinos y siembra rencor en las comunidades rurales hacia el gobierno.\n* **Sustitución Voluntaria de Cultivos:** Propone transitar hacia cacao, café o caucho de forma legal, pero sufre de demoras en infraestructura y el asedio violento de los nuevos grupos armados que asesinan a líderes sociales y campesinos para que no dejen de sembrar coca.")
