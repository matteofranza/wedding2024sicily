import streamlit as st
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
    <style>
    .justify-text {
        text-align: justify;
    }
    </style>
    <div class="justify-text">
    Vi starete chiedendo: ma dove diavolo bisogna andare? Come ci arrivo? Non preoccupatevi, qui sotto cercheremo di spiegarvi tutto, anche con l’aiuto di una cartina.
    </div>
    """, unsafe_allow_html=True)



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
    custom_icon = CustomIcon(
        icon_path,
        icon_size=(30, 30),  # Size of the icon image (width, height)
    )
    folium.Marker(
        location=location,
        icon=custom_icon,
        popup=popup_text,
    ).add_to(m)

# List of locations, icon paths, and popups
icons_info = [
    {'location': [37.46678, 15.0664], 'icon_path': 'icons//airport.png', 'popup_text': 'Catania-Fontanarossa Airport'},
    {'location': [37.070339538444806, 14.649711615950432], 'icon_path': 'icons/wedding.png', 'popup_text': 'Villa Fegotto'},
    {'location': [36.919911618944, 14.70805545783845], 'icon_path': 'icons/city.png', 'popup_text': 'Ragusa'},
    {'location': [36.78651754572091, 14.556379583430562], 'icon_path': 'icons/city.png', 'popup_text': 'Marina di Ragusa'}
]

for icon_info in icons_info:
    add_custom_icon_marker(icon_info['location'], icon_info['icon_path'], icon_info['popup_text'])


col1, col2, col3 = st.columns([1,2,1])
with col2:
    folium_static(m, width=map_width, height=map_height)


language_selection = st.sidebar.selectbox("Change language", ["ITA", "ENG"], index=0)


st.markdown("""
    <style>
    .justify-text {
        text-align: justify;
    }
    </style>
    <div class="justify-text">
    <b>Aeroporto di Catania - Fontanarossa:</b> questo è l'aeroporto dove, molto probabilmente, la maggior parte di voi atterrerà. È possibile che ci siano periodi dell'anno in cui, in base al vostro punto di partenza, potrebbero esserci dei voli con destinazione Aeroporto di Comiso, che è un piccolo aeroporto vicinissimo a Ragusa. Quindi, prima di prenotare, assicuratevi quale collegamento esiste con il vostro aeroporto di partenza.<br>
    Per chi atterrerà a Catania, se non avete intenzioni di affittare un'automobile, potrete optare per il servizio di bus Etnatraporti che, con un viaggio pittoresco tra fico pala, muretti a secco e munnizza, vi porterà a Ragusa e Marina di Ragusa. I biglietti sono acquistabili sul sito oppure direttamente alla biglietteria all'uscita dell'aeroporto (Chiosco Etnatrasporti).<br>
    C’è un bus con destinazione Ragusa ad ogni ora (Durata: 1h45). Tuttavia, dall’aeroporto i bus per Marina di Ragusa sono molto più saltuari (4 corse al giorno, durata: 2h20), quindi controllate gli orari sul sito oppure chiedete in biglietteria se e quando passa il bus per Marina di Ragusa. In ogni caso, dalla stazione di Ragusa partono dei bus per Marina di Ragusa ad ogni ora.
    </div>
    """, unsafe_allow_html=True)

if language_selection == "ITA":
    st.markdown("""
    <style>
    .justify-text {
        text-align: justify;
    }
    </style>
    <div class="justify-text">
    Vi starete chiedendo: ma dove diavolo bisogna andare? Come ci arrivo? Non preoccupatevi, qui sotto cercheremo di spiegarvi tutto, anche con l’aiuto di una cartina.<br>
                
    <b>Aeroporto di Catania - Fontanarossa:</b> questo è l'aeroporto dove, molto probabilmente, la maggior parte di voi atterrerà. È possibile che ci siano periodi dell'anno in cui, in base al vostro punto di partenza, potrebbero esserci dei voli con destinazione Aeroporto di Comiso, che è un piccolo aeroporto vicinissimo a Ragusa. Quindi, prima di prenotare, assicuratevi quale collegamento esiste con il vostro aeroporto di partenza **. 
    Per chi atterrerà a Catania, se non avete intenzioni di affittare un'automobile, potrete optare per il servizio di bus Etnatraporti che, con un viaggio pittoresco tra fico pala, muretti a secco e munnizza, vi porterà a Ragusa e Marina di Ragusa. I biglietti sono acquistabili sul sito oppure direttamente alla biglietteria all'uscita dell'aeroporto (Chiosco Etnatrasporti).
    C’è un bus con destinazione Ragusa ad ogni ora (Durata: 1h45). Tuttavia, dall’aeroporto i bus per Marina di Ragusa sono molto più saltuari (4 corse al giorno, durata: 2h20), quindi controllate gli orari sul sito oppure chiedete in biglietteria se e quando passa il bus per Marina di Ragusa. In ogni caso, dalla stazione di Ragusa partono dei bus per Marina di Ragusa ad ogni ora. <br>
                
    <b>Marina di Ragusa e Ragusa:</b> queste sono le due destinazioni che vi suggeriamo per la vostra villeggiatura. Se preferite il mare (le spiagge sono tutte libere con qualche chalet sparso qua e la), Marina di Ragusa è il vostro posto (sarà alta stagione, quindi affrettatevi a prenotare l’alloggio prima che vada tutto a ruba!). Se preferite la città, allora cercate a Ragusa, tenendo in considerazione che dista 15 min di macchina da Marina di Ragusa e dal quale partono ad ogni ora bus per il mare.<br> 
                
    <b>Villa Fegotto:<b> sarà la sede del nostro sposalizio. Qui potete cominciare a farvi un'idea del posto. Se siete interessati alla storia della villa, potete farvela raccontare direttamente da quel figo di Alberto Angela qui. Come avrete capito, Villa Fegotto non è vicinissima a Ragusa ma dista circa 30 minuti. Non preoccupatevi, data la distanza e l’open bar, vi metteremo a disposizione un servizio di bus gratuito per l'evento (vedi sezione Wedding day).<br>
                
    **Per chi viaggia dal Piemonte: abbiamo scoperto che da Marzo 2024 inizieranno dei voli bisettimanali con tratta a/r Torino-Comiso con Volotea! Al momento sul sito compaiono voli programmati fino a giugno, ma molto probabilmente verranno aggiornati nel tempo, aggiungendo voli anche a luglio ;) Quindi, tenetelo in considerazione!
    </div>
    """, unsafe_allow_html=True)


if language_selection == "ENG":
    st.markdown("""
    <style>
    .justify-text {
        text-align: justify;
    }
    </style>
    <div class="justify-text">
    You might wonder: where in hell should I go? How do I reach the place? Don’t worry, here we’ll explain everything, with a little help from the map.<br>
    
    <b>Catania- Fontanarossa Airport:</b> this is the airport where probably most of you will land in. There might be periods during the year in which, based on the airport you’ll fly from, there might be flights to Comiso Airport, which is a very small airport very close to Ragusa. So, before booking, check which connections are available with your departure airport.
    For those who will land in Catania, if you don’t want to rent a car, you can use the bus service Etnatrasporti that, with a picturesque journey among prickly pear, dry stone walls and trash, will take you to Ragusa and Marina di Ragusa. Tickets are purchasable online or at the ticket kiosk right outside the airport (Kiosk Etnatrasporti).
    There are buses to Ragusa at every hour of the day (Travel time: 1h45). Nonetheless, buses from the airport to Marina di Ragusa are more infrequent (4 rides/day, travel time: 2h20), so check in advance online or at the ticket kiosk if and which buses are directed to Marina di Ragusa. In any case, there is a bus departing Ragusa bus station to Marina di Ragusa at every hour. <br>
    
    <b>Marina di Ragusa e Ragusa:</b> these are the two destinations we suggest you for your holidays. If you prefer the seaside (all the beaches are free with a few choices for chalets), then Marina di Ragusa is your choice (it will be peak season, so hurry up with booking the accommodation before there won’t be any available for you!). If you prefer the city, then Ragusa is what you’re looking for, keeping in mind that it’s only 15 min by car from Marina di Ragusa and from which a bus at every hour departs with destination Marina di Ragusa.<br> 
                
    <b>Villa Fegotto:</b> it’s the place where the ceremony and the party will take place. Here you can find some information about the place. If you’re interested about the history of the Villa, here you have that handsome man Alberto Angela telling you the story. As you might have noticed, Villa Fegotto isn’t very close to Ragusa, but it’s 30 min far away. Don’t worry, given the distance and the open bar, there will be a bus service available for you for the day (see Wedding day section).<br>
    </div>
    """, unsafe_allow_html=True)

