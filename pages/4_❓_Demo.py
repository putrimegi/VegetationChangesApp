import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title('Demo')
st.markdown(
"""
This is a demonstration of our web apps created using [streamlit](https://streamlit.io/) and [leafmapapp](https://leafmap.org/) 

write(How to use and load our vegetation maps) in [Kalimantan Island](https://id.wikipedia.org/wiki/Kalimantan) 
"""
)

st.subheader("Instructions")
st.markdown(
"""
See this video bellow
"""
)

st.video('https://www.youtube.com/watch?v=fTzlyayFXBM&t=684s')
