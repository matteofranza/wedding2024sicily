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
Aeroporto Catania - Fontanarossa : questo è l'aeroporto relativamente piu' vicino a Ragusa. Potrebbero esserci periodi dell'anno che, in base al vostro punto di partenza, potrebbero esserci dei voli per Comiso che è effettivamente piu' vicino a Ragusa. 
Tuttavia la maggior parte di voi approdera' in terra sicula tramite Catania. Una volta giunti a Catania, se non avete intenzioni di affittare un'automobile, 
troverete potrete optare per il servizio di bus is [Etnatraporti](https://www.etnatrasporti.it/). I Biglietti sono acquistabili dal sito oppure direttamente sul posto al chioso all'uscita dell'aerporto. Il tragitto fino a Ragusa dura circa 2h (eh, lo so... non ditelo a me), 2h20 per Marina di Ragusa.
Se la vostra destinazione è Marina di Ragusa assicuratevi che il bus includa la fermata, potrebbe essere necessario un cambio a Ragusa
""", unsafe_allow_html=False)

st.markdown("""
Ragusa e Marina di Ragusa : queste sono le 2 destinazioni suggerite per la vostra villeggiatura. Ovviamente potete scegliere in base alle vostre tenendo in considerazione che la posizione dei mezzi di trasporto. 
""", unsafe_allow_html=False)

st.markdown("""
Villa Fegotto : sara' la sede del "grande giorno". [Qui ](https://www.etnatrasporti.it/) potete cominciare a farvi un'idea. 
Se siete interessati alla storia del luogo potete favela raccontare da Alberto Angela [qui ](https://www.facebook.com/SquiseatingVillaFegotto/videos/villa-fegotto-a-ulisse-il-piacere-della-scoperta/770288190120868/).
Come avrete capito, Villa Fegotto non è vicinissima a Ragusa ma dista circa 30 minuti da Ragusa. Un servizio di bus vi verra' messo a disposizione personalmente da noi per l'evento (vedi sezione Wedding day)
""", unsafe_allow_html=False)
