import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.header("Demonstration")
st.markdown(
"""
This is a demonstration of our app **How to use and load our vegetation maps** in [Kalimantan Island](https://id.wikipedia.org/wiki/Kalimantan) 
"""
)

st.video('https://www.youtube.com/watch?v=fTzlyayFXBM&t=684s')
