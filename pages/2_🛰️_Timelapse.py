import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.header("Timelapse")
#st.subheader("This timelapse showed vegetation changes from 2000-2021 on Kalimantan Island")

st.markdown (
"""
This timelapse showed vegetation changes from 2000-2021 on Kalimantan Island
"""
)
st.markdown (
"""
![Timelapse Vegetasi Pulau Kalimantan](https://media.giphy.com/media/Ey56FW3ui2TZ2vIe6y/giphy.gif)
"""
)
expander = st.expander("See explanation")
expander.write("""
   This series of shots for the time-lapse .gif was taken by Terra and Aqua [MODIS Nadir BRDF-Adjusted Reflectance Daily 500m](https://lpdaac.usgs.gov/products/mcd43a4v006/) from *January 1, 2001,* to *December 31, 2021,* while on the International Space Station. The dataset produces daily using 16 days of MODIS satellite data at a resolution of 500 meters (m). 
"""
  )

