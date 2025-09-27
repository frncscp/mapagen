import geopandas as gp 
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

colorlist = [
    "black", "dimgray", "dimgrey", "gray", "grey", "darkgray", "darkgrey", "silver",
    "lightgray", "lightgrey", "gainsboro", "whitesmoke", "white", "snow", "rosybrown",
    "lightcoral", "indianred", "brown", "firebrick", "maroon", "darkred", "red",
    "mistyrose", "salmon", "tomato", "darksalmon", "coral", "orangered", "lightsalmon",
    "sienna", "seashell", "chocolate", "saddlebrown", "sandybrown", "peachpuff", "peru",
    "linen", "bisque", "darkorange", "burlywood", "antiquewhite", "tan", "navajowhite",
    "blanchedalmond", "papayawhip", "moccasin", "orange", "wheat", "oldlace", "floralwhite",
    "darkgoldenrod", "goldenrod", "cornsilk", "gold", "lemonchiffon", "khaki",
    "palegoldenrod", "darkkhaki", "ivory", "beige", "lightyellow", "lightgoldenrodyellow",
    "olive", "olivedrab", "yellowgreen", "darkolivegreen", "greenyellow", "chartreuse",
    "lawngreen", "honeydew", "darkseagreen", "palegreen", "lightgreen", "forestgreen",
    "limegreen", "darkgreen", "green", "lime", "seagreen", "mediumseagreen", "springgreen",
    "mintcream", "mediumspringgreen", "mediumaquamarine", "aquamarine", "turquoise",
    "lightseagreen", "mediumturquoise", "azure", "lightcyan", "paleturquoise",
    "darkslategray", "darkslategrey", "teal", "darkcyan", "aqua", "cyan", "darkturquoise",
    "cadetblue", "powderblue", "lightblue", "deepskyblue", "skyblue", "lightskyblue",
    "steelblue", "aliceblue", "dodgerblue", "lightslategrey", "lightslategray", "slategrey",
    "lightsteelblue", "cornflowerblue", "royalblue", "ghostwhite", "lavender",
    "midnightblue", "navy", "darkblue", "blue", "slateblue", "darkslateblue",
    "mediumslateblue", "mediumpurple", "rebeccapurple", "indigo", "darkorchid",
    "darkviolet", "mediumorchid", "thistle", "plum", "violet", "darkmagenta", "fuchsia",
    "magenta", "orchid", "mediumvioletred", "purple", "deeppink", "hotpink",
    "lavenderblush", "palevioletred", "crimson", "pink", "lightpink"
]


def loadMap(data):
    if data is not None:
        mapa = gp.read_file(data, use_arrow = True)
        openMenu(mapa)

def openMenu(gdf):
    col = st.selectbox(label="Elige la columna con las regiones", options = list(gdf))
    regions = st.multiselect(label = "Elige las divisiones a resaltar", options= gdf[col])
    appears = gdf[col].isin(regions) 
    gdf["selected"] = appears
    renderMap(gdf)

def renderMap(mapa):
    delineado = st.selectbox("Elige el color de delinado(elige 'white' si quieres que desaparezca el delineado)", options = colorlist, index= 12)
    relleno = st.selectbox("Elige el color de relleno", options = colorlist, index = 76)
    vacio = st.selectbox("Elige el color de no-relleno (elige 'white' si quieres que desaparezcan los no elegidos)", options= colorlist, index = 8)
    colors = mapa["selected"].map({True: relleno, False: vacio})

    showTable = st.toggle("Mostrar tabla")
    if showTable: 
        st.write(mapa.head())
    ax = mapa.plot(figsize=(15, 15), column = "selected", edgecolor=delineado, color=colors)
    ax.set_axis_off()
    st.pyplot(ax.figure, dpi = 300)
