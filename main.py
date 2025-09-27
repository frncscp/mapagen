import streamlit as st 
from render.maps import loadMap

st.set_page_config(
    page_title = "mapagen",
    page_icon = "🗺️"

)

st.title("mapagen")

mapa = st.file_uploader(label = "Sube el mapa a renderizar", type = ["geo.json", "geojson"])
st.divider()
loadMap(mapa)