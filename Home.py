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
    <style>
    .justify-text {
        text-align: justify;
    }
    </style>
    <div class="justify-text">
        Eccoci qui! È arrivato QUEL giorno: il 21 Luglio 2024 ci sposiamo e voi tutti siete invitati a raggiungerci in Sicilia per fare <strong>FESTA!!!</strong><br>
        Quest’ app ha il solo scopo di fornirvi una panoramica dell'organizzazione dell'evento così da permettervi, per chi lo volesse, di pianificare con anticipo il vostro viaggio. Il sito web ufficiale vi verrà svelato con la consegna delle partecipazioni (Febbraio/Marzo 2024). 
        Nella tendina in alto a sinistra troverete le varie sezioni con le informazioni su: viaggio, alloggio e giorno del matrimonio.<br>
        Per qualunque dubbio, sentitevi liberi di contattarci su Whatsapp o via email.
    </div>
    """, unsafe_allow_html=True)
