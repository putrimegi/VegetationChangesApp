import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title('Demo')
st.markdown(
"""
See this video demonstration of our web apps created using [streamlit](https://streamlit.io/) and [leafmapapp](https://leafmap.org/) below to learn *How to use and load our Vegetation Maps* on [Kalimantan Island](https://id.wikipedia.org/wiki/Kalimantan).
"""
)
st.subheader('Demonstration of Vegetation changes web application')
st.video('https://www.youtube.com/watch?v=pkQDFjMkAZw&t=14s')
st.markdown(
"""
"""
)
st.subheader('Developing a Streamlit Web App for Geospasial Application')
st.video('https://www.youtube.com/watch?v=fTzlyayFXBM&t=684s')
