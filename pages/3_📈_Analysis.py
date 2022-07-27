import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title('Analysis Changes in Vegetation Area')
st.markdown(
"""
"""
)
st.header("📌 Graph of changes in the area of vegetation")
st.markdown(
"""
"""
)
st.markdown(
"""
![](https://i.postimg.cc/CLc2jBVD/Area-of-Vegetation.jpg)
"""
)
expander = st.expander("See explanation")
expander.write("""
The graph above shows the total area of four vegetation classes on the island of Kalimantan from 2000 to 2021. The no vegetation and slightly density classes rarely experience small changes, the moderately density class is decreasing, and the high density class is increasing.
"""
)
st.markdown(
"""
"""
)
st.header("📌 Vegetation Changes in a Coal Area")
st.markdown(
"""
"""
)
st.markdown(
"""
📍 PT. Kaltim Prima Coal (KCP)
"""
)
st.markdown(
"""
![](https://i.postimg.cc/mDwcNbc5/7.jpg)
"""
)
st.markdown(
"""
📍 PT. Adaro Indonesia (AI) (left) & PT.Kideco Jaya Agung (right)
"""
)
st.markdown(
"""
![](https://i.postimg.cc/hGnPCkqW/8.jpg)
"""
)
st.markdown(
"""
📍 PT. Berau Coal
"""
)
st.markdown(
"""
![](https://i.postimg.cc/K8mxyn4C/9.jpg)
"""
)
expander = st.expander("See explanation")
expander.write("""
  The island of Kalimantan is famous for it's mineral wealth and many mining industries operate. Through the picture above, the increase in a mining areas from 2000 to 2021 can be seen.
"""
)

st.subheader("📌 Distribution of Oil and Palm Plantations  in Kalimantan")
st.markdown(
"""
![](https://i.postimg.cc/3R3FRhx1/pnas-1704728114fig01.jpg) 
"""
)
expander = st.expander("See explanation")
expander.write("""
  Changes in vegetation every year are increasing. This change is presumably due to land clearing for plantations, timber industries, and other industries that utilize natural resources in Kalimantan. The image above is a map of the oil palm plantation area in 2017. The plantation areas are spread across the island of Kalimantan. 
"""
)
st.markdown(
"""
Image sourced from [Kimberly M. Carlson,2017](https://www.pnas.org/doi/10.1073/pnas.1704728114#fig01)
"""
)
