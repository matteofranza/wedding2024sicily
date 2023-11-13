import streamlit as st
import os
from streamlit_folium import folium_static
import folium
from folium.features import CustomIcon
######################################################################
## layout
######################################################################
st.set_page_config(layout="wide")
#Hide "made with streamlit" at the bottom of the page
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
######################################################################
######################################################################
st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    <h1 class="centered-text">Travel and locations</h1>
    """, unsafe_allow_html=True)

st.markdown("""
Tra le domande che vi saranno sorte ci saranno: diavolo bisogna andare? come ci arrivo? Bene, qui sotto cercheremo di spiegarvi tutto sulla cartina.
""", unsafe_allow_html=False)





sicily_bounds = [
    [36.635, 12.376],  # Southwest corner
    [38.796, 15.654]   # Northeast corner
]

# Create a map object with these bounds as maxBounds
m = folium.Map(
    location=[37.599994, 14.015356],  # Center of the bounds
    zoom_start=7,
    min_zoom=7,
    max_zoom=16,
    maxBounds=sicily_bounds,
    maxBoundsViscosity=1.0,  # Makes the bounds sticky (i.e., the map will bounce back when dragging outside)
)
map_width, map_height = 500, 300


def add_custom_icon_marker(location, icon_path, popup_text):
    # Check if the file exists
    if not os.path.isfile(icon_path):
        raise FileNotFoundError(f"The icon at path {icon_path} was not found.")

    custom_icon = CustomIcon(
        icon_image=icon_path,
        icon_size=(30, 30),  # Size of the icon image (width, height)
    )
    folium.Marker(
        location=location,
        icon=custom_icon,
        popup=popup_text,
    ).add_to(m)

# List of locations, icon paths, and popups

icons_directory = os.path.join(os.getcwd(), 'icons')
icons_info = [
    {'location': [37.46678, 15.0664], 'icon_path': os.path.join(icons_directory, 'airport.png'), 'popup_text': 'Catania-Fontanarossa Airport'},
    {'location': [37.070339538444806, 14.649711615950432], 'icon_path': os.path.join(icons_directory, 'wedding.png'), 'popup_text': 'Villa Fegotto'},
    {'location': [36.919911618944, 14.70805545783845], 'icon_path': os.path.join(icons_directory, 'city.png'), 'popup_text': 'Ragusa'},
    {'location': [36.78651754572091, 14.556379583430562], 'icon_path': os.path.join(icons_directory, 'city.png'), 'popup_text': 'Marina di Ragusa'}
]

for icon_info in icons_info:
    add_custom_icon_marker(icon_info['location'], icon_info['icon_path'], icon_info['popup_text'])



col1, col2, col3 = st.columns([1,2,1])
with col2:
    folium_static(m, width=map_width, height=map_height)

st.markdown("""
    <style>
    .justify-text {
        text-align: justify;
    }
    </style>
    <div class="justify-text">
    <strong>Aeroporto di Catania - Fontanarossa:</strong> questo è l'aeroporto dove, molto probabilmente, la maggior parte di voi atterrerà. È possibile che ci siano periodi dell'anno in cui, in base al vostro punto di partenza, potrebbero esserci dei voli con destinazione Aeroporto di Comiso, che è un piccolo aeroporto vicinissimo a Ragusa. Quindi, prima di prenotare, assicuratevi quale collegamento esiste con il vostro aeroporto di partenza.<br>
    Per chi atterrerà a Catania, se non avete intenzioni di affittare un'automobile, potrete optare per il servizio di bus Etnatraporti che, con un viaggio pittoresco tra fico pala, muretti a secco e munnizza, vi porterà a Ragusa e Marina di Ragusa. I biglietti sono acquistabili sul sito oppure direttamente alla biglietteria all'uscita dell'aeroporto (Chiosco Etnatrasporti).<br>
    C’è un bus con destinazione Ragusa ad ogni ora (Durata: 1h45). Tuttavia, dall’aeroporto i bus per Marina di Ragusa sono molto più saltuari (4 corse al giorno, durata: 2h20), quindi controllate gli orari sul sito oppure chiedete in biglietteria se e quando passa il bus per Marina di Ragusa. In ogni caso, dalla stazione di Ragusa partono dei bus per Marina di Ragusa ad ogni ora.
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
    <style>
    .justify-text {
        text-align: justify;
    }
    </style>
    <div class="justify-text">
    <strong>Marina di Ragusa e Ragusa:</strong> queste sono le due destinazioni che vi suggeriamo per la vostra villeggiatura. Se preferite il mare (le spiagge sono tutte libere con qualche chalet sparso qua e la), Marina di Ragusa è il vostro posto (sarà alta stagione, quindi affrettatevi a prenotare l’alloggio prima che vada tutto a ruba!). Se preferite la città, allora cercate a Ragusa, tenendo in considerazione che dista 15 min di macchina da Marina di Ragusa e dal quale partono ad ogni ora bus per il mare. 
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
    <style>
    .justify-text {
        text-align: justify;
    }
    </style>
    <div class="justify-text">
    <strong>Villa Fegotto:</strong> sarà la sede del nostro sposalizio. Qui potete cominciare a farvi un'idea del posto. Se siete interessati alla storia della villa, potete farvela raccontare direttamente da quel figo di Alberto Angela qui. Come avrete capito, Villa Fegotto non è vicinissima a Ragusa ma dista circa 30 minuti. Non preoccupatevi, data la distanza e l’open bar, vi metteremo a disposizione un servizio di bus gratuito per l'evento (vedi sezione <strong>Wedding day</strong>).
    </div>
    """, unsafe_allow_html=True)

