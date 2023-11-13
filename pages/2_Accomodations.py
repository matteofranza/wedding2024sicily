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
    <style>
    .justify-text {
        text-align: justify;
    }
    </style>
    <div class="justify-text">
    Visto l’alto numero di amici e familiari che ci raggiungerà da fuori Sicilia, e visto le diverse esigenze individuali, abbiamo deciso di non occuparci direttamente della vostra sistemazione (speriamo sappiate comprendere la situazione ;)). Come già detto, luglio sarà alta stagione, quindi vi consigliamo caldamente di cominciare a cercare e prenotare un posto per la vostra sistemazione. Al momento, ci sono ancora svariate opzioni economiche, soprattutto se vi organizzate in gruppo.<br> 
    Le piattaforme di prenotazione consigliate sono quelle classiche ([AirBnB](https://www.airbnb.com/), [Booking](https://www.booking.com/index.it.html?aid=397594&label=gog235jc-1DCAEoggI46AdIM1gDaCyIAQGYARS4ARfIAQzYAQPoAQGIAgGoAgO4AsfYtaoGwAIB0gIkMWJkYmJjMDEtNDE2ZC00ZDdmLTlmZDYtY2MxNzg2ZThjZGZj2AIE4AIB&sid=0c9cc786cb4b9dbfe28a52fd0b89a5d3&keep_landing=1&sb_price_type=total&), [campeggio](https://www.campingbaiadelsole.it/))), più i vari Hotel presenti sul posto.<br>
    Non esitate a contattarci per ogni domanda e dubbio prima di confermare le prenotazioni.
    </div>
    """, unsafe_allow_html=True)
