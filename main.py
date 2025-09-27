import streamlit as st 
from render.maps import loadMap

st.set_page_config(
    page_title = "mapagen",
    page_icon = "🗺️"

)

st.title("mapagen")

supported_types = [
    "geojson",   # GeoJSON
    "json",      # GeoJSON / TopoJSON
    "gpkg",      # GeoPackage
    "kml",       # KML
    "kmz",       # KMZ
    "gml",       # GML
    "parquet",   # Parquet
    "feather",   # Feather
    "fgb",       # FlatGeobuf (if GDAL ≥ 3.1)
    "mvt"        # Mapbox Vector Tiles (if GDAL supports it)
]

mapa = st.file_uploader(label = "Sube el mapa a renderizar", type = supported_types)
st.divider()

try: 
    loadMap(mapa)
except Exception as e:
    st.error("Archivo no soportado: " + str(e))