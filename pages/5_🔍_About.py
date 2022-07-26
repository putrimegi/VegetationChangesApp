import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.markdown(
"""
Web App URL: <https://template.streamlitapp.com>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""
)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Nama Anggota 1")
    #st.image("https://static.streamlit.io/examples/cat.jpg")

with col3:
    st.header("Nama Angota 2")
    #st.image("https://static.streamlit.io/examples/dog.jpg")
