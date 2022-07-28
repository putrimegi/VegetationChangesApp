import streamlit as st
import ee
import numpy as np
import geemap
import pandas as pd

service_account = 'keygoogleearthengine@kp-putri-megi.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'kp-putri-megi-86d984e6c787.json')
ee.Initialize(credentials)

st.set_page_config(layout="wide")

st.title("Marker Cluster")

Map = geemap.Map()
Map.setCenter(114.0, 5.0, 6)

marks = 'Database_Titik_Lokasi_Kalimantan.csv'

Map.add_points_from_xy(
    marks,
    x="Longtitude",
    y="Latitude",
    color_column='Type',
    icon_colors=['black','blue'],
    icon_names=['truck', 'tint'],
    #spin=True,
    add_legend=True,
)

Map.to_streamlit(height=700)

# with st.expander("See source code"):
#     with st.echo():

#          m = leafmap.Map(center=[40, -100], zoom=4)
# #         cities = 'https://github.com/putrimegi/kerjapraktek/blob/5cbd738e3c96e0b89fe2f8cb8357838fa24845ee/Titik%20Lokasi%20Kalimantan.csv'
# #         #regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'

# #         #m.add_geojson(regions, layer_name='US Regions')
# #         m.add_points_from_xy(
# #             cities,
# #             x="Longitude",
# #             y="Latitude",
# #             color_column='Type',
# #             icon_names=['gear', 'map'],
# #             spin=True,
# #             add_legend=True,
# #         )
        
#  m.to_streamlit(height=700)
