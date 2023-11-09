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
st.markdown("<h1 style='text-align: center'> Wedding day </h1>", unsafe_allow_html=True)

st.markdown("""
Il rito verra' pronunciato a Villa Fegotto alle ore 18:00 mentre tutto il resto della giornata si prolunghera' fino alle 03:00.
Per raggiungere il luogo vi verra' fornito un servizio di bus. Gli orari sono ancora da stabilire, come le fermate. Sicuramente cercheremo di venire in contro a tutti programmando fermate strategiche in base ai luoghi dove la gente ha deciso di alloggiare.
Cio' non significa che vi verremo a prendere casa per casa come quando c'era LVI, ma vi cercheremo di organizzare almeno un punto di incontro a Marina di Ragusa ed una a Ragusa. 
Putroppo cercate di capire che sara' un giorno complicato per noi, quindi non possiamo accontentare tutti. Se gia' sapete di poter avere delle esigenze diverse diverse dalla soluzione fornita vi prego di comunicarcelo al piu' presto per trovare una soluzione.
Visto il programma, vi invitiamo a programmare la giornata per essere pronti per le ore 16.00.  
""", unsafe_allow_html=False)
