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
    La cerimonia si svolgerà a Villa Fegotto intorno alle ore 18:00/18.30 (Avrete conferma dell’orario quando riceverete la partecipazione). Terminata la cerimonia, mentre noi sogneremo uno spritz scattandoci di malavoglia qualche foto, voi vi potrete godere un buonissimo aperitivo in loco. Al termine della cena inizierà la festa vera e propria: open bar per tutti e discoteca sotto le stelle fino alle 02:30.<br> 
    Per raggiungere Villa Fegotto, nel caso non abbiate una macchina o non abbiate voglia di guidare (non guidate se pensate di approfittare dell’open bar!!!), vi verrà fornito un servizio navetta. Gli orari sono ancora da stabilire, così come le fermate. Sicuramente cercheremo di venire incontro a tutti, programmando fermate strategiche in base ai luoghi dove deciderete di alloggiare. Ciò non significa che vi verremo a prendere casa per casa come quando c'era LVI, ma cercheremo di organizzare almeno un punto di incontro a Marina di Ragusa ed uno a Ragusa. Lo stesso servizio navetta vi sarà messo a disposizione alla fine della festa, e vi riporterà alla stessa fermata in cui l’avete preso all’andata. <br>
    PS: un servizio di animazione/baby sitter si prenderà cura dei vostri bambini con età dai 3 ai 9 anni circa, principalmente durante la cena (da definire la possibilità di estendere il servizio anche durante la festa) ;). 

    </div>
    """, unsafe_allow_html=True)
