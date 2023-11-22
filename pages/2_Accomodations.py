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

st.markdown("<h1 style='text-align: center'> Accomodations </h1>", unsafe_allow_html=True)

language_selection = st.sidebar.selectbox("Change language", ["ITA", "ENG"], index=0)


if language_selection == "ITA":
    st.markdown("""
                <style>
                .justify-text {
                text-align: justify;
                }
                </style>
                <div class="justify-text">
                Visto l’alto numero di amici e familiari che ci raggiungerà da fuori Sicilia, e visto le diverse esigenze individuali, abbiamo deciso di non occuparci direttamente della vostra sistemazione (speriamo sappiate comprendere la situazione ;)). Come già detto, luglio sarà alta stagione, quindi vi consigliamo caldamente di cominciare a cercare e prenotare un posto per la vostra sistemazione. Al momento, ci sono ancora svariate opzioni economiche, soprattutto se vi organizzate in gruppo.<br> 
                Le piattaforme di prenotazione consigliate sono quelle classiche <a href='https://www.airbnb.com'>AirBnB</a>, <a href='https://www.booking.com/index.en-gb.html'>Booking</a>, <a href='https://www.campingbaiadelsole.it/'>campeggio</a>, più i vari Hotel presenti sul posto.<br> 
                Non esitate a contattarci per ogni domanda e dubbio prima di confermare le prenotazioni.
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
                Given the high number of friends and family members coming from outside Sicily, and given the different personal needs, we’ve decided not to take care of your accommodations (we hope you’ll understand ;)). As we’ve already said, July is considered peak season, therefore we strongly suggest you to start looking for and booking a place for your staying. At the moment, there still are several economic options, especially if you organize into groups.<br> 
                The platforms for bookings that we suggest are the classic ones <a href='https://www.airbnb.com'>AirBnB</a>, <a href='https://www.booking.com/index.en-gb.html'>Booking</a>, <a href='https://www.campingbaiadelsole.it/'>campeggio</a>, plus the various hotels.<br>
                Please, do not hesitate to contact us for any questions or doubts before booking.
                </div>
                """, unsafe_allow_html=True)    

