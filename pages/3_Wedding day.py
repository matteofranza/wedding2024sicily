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
language_selection = st.sidebar.selectbox("Change language", ["ITA", "ENG"], index=0)

st.markdown("<h1 style='text-align: center'> Wedding day </h1>", unsafe_allow_html=True)


if language_selection == "ITA":
    st.markdown("""
                <style>
                .justify-text {
                text-align: justify;
                }
                </style>
                <div class="justify-text">
                La cerimonia si svolgerà a Villa Fegotto intorno alle ore 18:00/18.30 (Avrete conferma dell’orario quando riceverete la partecipazione). Terminata la cerimonia, mentre noi sogneremo uno spritz scattandoci di malavoglia qualche foto, voi vi potrete godere un buonissimo aperitivo in loco. Al termine della cena inizierà la festa vera e propria: open bar per tutti e discoteca sotto le stelle fino alle 02:30.<br> 
                Per raggiungere Villa Fegotto, nel caso non abbiate una macchina o non abbiate voglia di guidare (non guidate se pensate di approfittare dell’open bar!!!), vi verrà fornito un servizio navetta. Gli orari sono ancora da stabilire, così come le fermate. Sicuramente cercheremo di venire incontro a tutti, programmando fermate strategiche in base ai luoghi dove deciderete di alloggiare. Ciò non significa che vi verremo a prendere casa per casa come quando c'era LVI, ma cercheremo di organizzare almeno un punto di incontro a Marina di Ragusa ed uno a Ragusa. Lo stesso servizio navetta vi sarà messo a disposizione alla fine della festa, e vi riporterà alla stessa fermata in cui l’avete preso all’andata.<br> 
                PS: un servizio di animazione/baby sitter si prenderà cura dei vostri bambini con età dai 3 ai 9 anni circa, principalmente durante la cena (da definire la possibilità di estendere il servizio anche durante la festa) ;). 
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
                The ceremony will take place at Villa Fegotto around 18h/18h30 (Timeline will be officially confirmed in the invitation you’ll receive). After the ceremony, while we’ll dream of having a spritz and reluctantly, we’ll take a few photos, you’ll enjoy a delicious apéro on the spot. At the end of the dinner, the real party begins: open bar for everyone and disco under the stars until 02h30.<br>
                To reach Villa Fegotto, if you don’t have a car or don’t want to drive (do not drive if you want to take advantage of the open bar!!!), we’ll provide you with a bus service. A timeline needs to be established yet, same for the stops.  Surely, we’ll try to meet you halfway, scheduling the bus stops as close as possible to your place of staying. Obv, this doesn’t mean that we’ll pick you up house by house, but we’ll try to organize a stop in Marina di Ragusa and another one in Ragusa.<br> 
                The same bus service will be provided to you at the end of the party, and it will take you back to the same bus stop where you picked it up.<br>
                PS: a baby sitter will be provided to take care of your children age 3-9 yo, mainly during the dinner (let’s see if we can extend it also during the party) ;). 

                </div>
                """, unsafe_allow_html=True)    
