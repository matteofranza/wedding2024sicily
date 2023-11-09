import streamlit as st

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
st.markdown("<h1 style='text-align: center'> Sistemazioni </h1>", unsafe_allow_html=True)

st.markdown("""
Visto il numero di person che ci raggiungera' da fuori della Sicilia, e delle varie esigenze individuali, non ci siamo sentiti di prenderci la responsabilita' di organizzare una sistemazione di gruppo. 
Infatti ci aspettiamo che molti di voi possano passare piu' tempo in sicilia prima e dopo l'evento.
Considerando che sara' alta stagione, vi consigliamo di cominciare a cerca sin da ora e tentare di prenotare entro l'anno nuovo.
Detto questo le piattoforme di pernottamento consigliate sono quelle classiche 
(
            [airbnb](https://www.airbnb.com/),
            [booking](https://www.booking.com/index.it.html?aid=397594&label=gog235jc-1DCAEoggI46AdIM1gDaCyIAQGYARS4ARfIAQzYAQPoAQGIAgGoAgO4AsfYtaoGwAIB0gIkMWJkYmJjMDEtNDE2ZC00ZDdmLTlmZDYtY2MxNzg2ZThjZGZj2AIE4AIB&sid=0c9cc786cb4b9dbfe28a52fd0b89a5d3&keep_landing=1&sb_price_type=total&),
            [campeggio](https://www.campingbaiadelsole.it/)) piu' i vari Hotel presenti sul luogo.
Spulciando le varie soluzioni vi possiamo suggerire di organizzarvi in gruppi per trovare sistemazioni piu' convenienti.

Non esistate a contattarci per ogni domanda e dubbio prima di confermare le prenotazioni

""", unsafe_allow_html=False)
