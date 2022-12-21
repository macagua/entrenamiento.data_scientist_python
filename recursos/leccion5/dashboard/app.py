# @Email:  leonardocaballero@gmail.com
# @Website:  https://pythonandvba.com
# @Github:  https://github.com/macagua
# @Project:  Tablero de Ventas con Streamlit


import os
import pandas as pd
import plotly.express as px
import streamlit as st

FULL_PATH = (
    os.path.dirname(os.path.abspath(__file__)) + os.sep + "ventas_supermercado.xlsx"
)

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="Tablero de Ventas", page_icon=":bar_chart:", layout="wide"
)

# ---- LEER ARCHIVO EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io=FULL_PATH,
        engine="openpyxl",
        sheet_name="Ventas",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    # Agregar columna 'hour' al dataframe
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    df.rename(columns={"hour": "Hora"}, inplace=True)
    return df


df = get_data_from_excel()

# ---- BARRA LATERAL ----
st.sidebar.header("Por favor, filtre aquí:")
ciudad = st.sidebar.multiselect(
    "Seleccione la Ciudad:",
    options=df["Ciudad"].unique(),
    default=df["Ciudad"].unique(),
)

tipo_cliente = st.sidebar.multiselect(
    "Seleccione el tipo de Cliente:",
    options=df["Tipo_Cliente"].unique(),
    default=df["Tipo_Cliente"].unique(),
)

genero = st.sidebar.multiselect(
    "Seleccione el Genero:",
    options=df["Genero"].unique(),
    default=df["Genero"].unique(),
)

df_seleccion = df.query(
    "Ciudad == @ciudad & Tipo_Cliente ==@tipo_cliente & Genero == @genero"
)
df_seleccion.rename(columns={"Linea producto": "Línea de producto"}, inplace=True)

# ---- PAGINA PRINCIPAL ----
st.title(":bar_chart: Tablero de Ventas")
st.markdown("##")

# KPI PRINCIPALES
total_ventas = int(df_seleccion["Total"].sum(numeric_only=True))
puntuacion_media = round(df_seleccion["Clasificacion"].mean(), 1)
puntuacion_star = ":star:" * int(round(puntuacion_media, 0))
ventas_promedio_por_transaccion = round(df_seleccion["Total"].mean(), 2)

columna_izquierda, columna_media, columna_derecha = st.columns(3)
with columna_izquierda:
    st.subheader("Total de Ventas:")
    st.subheader(f"Bs. {total_ventas:,}")
with columna_media:
    st.subheader("Puntuación media:")
    st.subheader(f"{puntuacion_media} {puntuacion_star}")
with columna_derecha:
    st.subheader("Ventas promedio por transacción:")
    st.subheader(f"Bs. {ventas_promedio_por_transaccion}")

st.markdown("""---""")

# VENTAS POR LÍNEA DE PRODUCTO [GRÁFICO DE BARRAS]
ventas_por_linea_producto = (
    df_seleccion.groupby(by=["Línea de producto"])
    .sum(numeric_only=True)[["Total"]]
    .sort_values(by="Total")
)
fig_ventas_producto = px.bar(
    ventas_por_linea_producto,
    x="Total",
    y=ventas_por_linea_producto.index,
    orientation="h",
    title="<b>Ventas por Línea de Producto</b>",
    color_discrete_sequence=["#0083B8"] * len(ventas_por_linea_producto),
    template="plotly_white",
)
fig_ventas_producto.update_layout(
    plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False))
)

# VENTAS POR HORA [GRÁFICO DE BARRAS]
ventas_por_horas = df_seleccion.groupby(by=["Hora"]).sum(numeric_only=True)[["Total"]]
fig_ventas_por_horas = px.bar(
    ventas_por_horas,
    x=ventas_por_horas.index,
    y="Total",
    title="<b>Ventas por hora</b>",
    color_discrete_sequence=["#0083B8"] * len(ventas_por_horas),
    template="plotly_white",
)
fig_ventas_por_horas.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


columna_izquierda, columna_derecha = st.columns(2)
columna_izquierda.plotly_chart(fig_ventas_por_horas, use_container_width=True)
columna_derecha.plotly_chart(fig_ventas_producto, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
