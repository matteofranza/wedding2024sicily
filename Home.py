import streamlit as st
import streamlit.components.v1 as components
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
## Title
######################################################################
st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    <h1 class="centered-text">Home</h1>
    """, unsafe_allow_html=True)

st.markdown("""
Eccoci qui! Ne avrete sentito parlare ma l'estate prossima visiterete la Sicilia per partecipare al nostro matrimonio.
Questa app ha il solo scopo di fornivi una panoramica dell'organizzazione dell'evento per aiutarvi a pianificare il vostro viaggio. Il vero sito web vi verra' svelato con la consegna delle
partecipazioni (febbraio/marzo 2024).
Per cominciare potete selezionare l'area di interesse sulla sinistra. Ovviamente sentitve liberi di contattarci privatamente per ogni esigenza.  
""", unsafe_allow_html=False)
