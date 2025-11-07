import streamlit as st
import pandas as pd

# --------------------------------------------
# CONFIGURACIÓN BÁSICA DE LA APP
# --------------------------------------------
st.set_page_config(
    page_title="Dashboard Turismo Caldas",
    page_icon="",
    layout="wide"
)

# --------------------------------------------
# TÍTULO Y DESCRIPCIÓN
# --------------------------------------------
st.title(" Turismo en Caldas")
st.markdown("""
Caldas te abre las puertas con el corazón.<br>
Entre montañas, café y sonrisas, los viajeros del mundo descubren un rincón donde la naturaleza y la cultura se unen para ofrecer una experiencia inolvidable.
""", unsafe_allow_html=True)

# --------------------------------------------
# SECCIÓN DE REPORTE DE POWER BI
# --------------------------------------------
st.subheader("🔹 Reporte Interactivo de Power BI")

# URL de tu reporte publicado en Power BI
powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiM2RlYzVhOTItZTZjYy00YzMxLThiZmItMzQwZmU4NDQwMjYzIiwidCI6IjRmMWUwNDRkLTNkNzAtNDk5MC1iMjZhLWI5NWYwYzY0MmUxYSIsImMiOjR9"

# Incrustar el reporte dentro de Streamlit
st.markdown(
    f"""
    <iframe width="100%" height="750"
    src="{powerbi_url}"
    frameborder="0" allowFullScreen="true"></iframe>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------
# SECCIÓN DE DATOS Y ANÁLISIS
# --------------------------------------------
st.subheader("Análisis complementario de datos turísticos")

# Ejemplo de DataFrame con datos turísticos
data = {
    "Año": [2021, 2022, 2023, 2024],
    "Visitantes": [12000, 15500, 18900, 21000],
    "Ciudad": ["Manizales", "Salamina", "Aguadas", "Riosucio"]
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

# Gráfico de visitantes por año
st.line_chart(df.set_index("Año")["Visitantes"])

# --------------------------------------------
# BOTÓN DE DESCARGA DE DATOS
# --------------------------------------------
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Descargar datos en CSV",
    data=csv,
    file_name="turismo_caldas.csv",
    mime="text/csv"
)

# --------------------------------------------
# SECCIÓN: TEXTO Y RESPUESTA EN BINARIO
# --------------------------------------------
st.subheader("Resultados del análisis")

# Textos
texto1 = "Probabilidad de aumento"
texto2 = "Tendencia general"

# Función para convertir texto a binario
def a_binario(texto):
    return ' '.join(format(ord(c), '08b') for c in texto)

# Convertir a binario
binario1 = a_binario(texto1)
binario2 = a_binario(texto2)

# Mostrar resultados
st.write(f"**{texto1}:**")
st.code(binario1, language="text")

st.write(f"**{texto2}:**")
st.code(binario2, language="text")

# --------------------------------------------
# PIE DE PÁGINA
# --------------------------------------------
st.markdown("---")
st.caption("Desarrollado por **Lorena Andrea Ríos Olaya y Vanessa Herrera Giraldo**  | Proyecto Turismo Caldas 2025")
