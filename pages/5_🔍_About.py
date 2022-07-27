import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

col1, col2, col3= st.columns(3)

with col2:
    st.markdown(
"""
This web app is maintained by ACE,  
Remote sensing and Geographic Information Science (GIS) researchers group from Geomatics Engineering, Institute Technology of Sepuluh Nopember. 
"""
)

col1, col2, col3= st.columns(3)

with col1:
    st.header("Member 1")
    #st.image("https://static.streamlit.io/examples/cat.jpg")

with col3:
    st.header("Member 2")
    #st.image("https://static.streamlit.io/examples/dog.jpg")


st.header("batas bawah")
