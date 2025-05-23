import streamlit as st

st.title("Test Bouton Ultra-Simple")
st.write("Ceci est un test minimal pour Streamlit Cloud.")

if st.button("Cliquez-moi !"):
    st.success("Le bouton minimal a été cliqué avec succès !")
    st.balloons()