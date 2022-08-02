#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import ee
import numpy as np
import geemap
import pandas as pd
#import pygal
#import ipygee as ui

service_account = 'keygoogleearthengine@kp-putri-megi.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'kp-putri-megi-86d984e6c787.json')
ee.Initialize(credentials)
# In[2]:

st.header("Map of Vegetation Change on Kalimantan Island")

st.markdown(
  """
  This application was created to display vegetation changes on Kalimantan Island, Indonesia, using the MNDVI algorithm from 2000-2022 years
based on the [W.J.D.van Leeuwen,1996](https://www.sciencedirect.com/science/article/abs/pii/0034425795001980) with Satellite Imagery *MODIS/006/MCD43A4*.
  """
)

#Menginisiasi map
Map = geemap.Map()
Map.setCenter(114.0, 0.0, 5)
#Map.addLayerControl()

#MEMILIH TAHUN
start_year = 2000
end_year = 2022
study_area = ee.Geometry.Polygon([
          [108.47918130370147, 0.8398883418565013],
          [109.07244302245147, -1.071640184126184],
          [108.50115395995147, -1.7745439000254541],
          [109.48992349120147, -1.730619145610487],
          [110.06121255370147, -3.245259038510266],
          [111.33562661620147, -3.4426761405977153],
          [112.17058755370147, -3.925074314651903],
          [113.18132974120147, -3.5742649570575513],
          [114.25798989745147, -3.727761338836346],
          [114.49968911620147, -4.451008054437248],
          [115.62029458495147, -4.144256185799882],
          [116.54314614745147, -4.363377320694263],
          [116.80681802245147, -3.1355660522092195],
          [116.78484536620147, -1.7745439000254541],
          [117.99334145995147, -0.8299744239790947],
          [118.32293130370147, 0.1807384355535991],
          [118.30095864745147, 0.6201797496097374],
          [119.33367349120147, 0.6860934318837462],
          [118.54265786620147, 1.9601414255777354],
          [118.03728677245147, 3.1893443110398327],
          [118.54265786620147, 3.934965970241232],
          [117.83953286620147, 4.745615892683102],
          [116.65300942870147, 4.876987255245337],
          [114.98308755370147, 3.1674054541050047],
          [114.54363442870147, 2.2455932959883516],
          [113.70867349120147, 1.7844540889773604],
          [112.63201333495147, 2.0260195125928204],
          [111.77507974120147, 1.6307138440462585],
          [110.63250161620147, 1.5648215076977423],
          [110.01726724120147, 2.267548912903311],
          [109.31414224120147, 2.487086228509065],
          [108.69890786620147, 1.6307138440462585]
          ])

modis = ee.ImageCollection('MODIS/006/MCD43A4')\
          .filterBounds(study_area)

yearlist = range(start_year, end_year)


# In[3]:


#CLOUD MASKING
def maskClouds(image):
  # Select the QA band.
  QA = image.select('BRDF_Albedo_Band_Mandatory_Quality_Band1')
  # Make a mask to get bit 10, the internal_cloud_algorithm_flag bit.
  bitMask = 1 << 10
  # Return an image masking out cloudy areas.
  return image.multiply(0.0001).updateMask(QA.bitwiseAnd(bitMask).eq(0))


# In[4]:


#PERHITUNGAN MNDVI

def calculate_mndvi (year):
 images = modis.filter(ee.Filter.calendarRange(year, year, 'year')).map(maskClouds).mean()
 NDVI = images.normalizedDifference(['Nadir_Reflectance_Band2', 'Nadir_Reflectance_Band1']).rename('NDVI')
 H1 = images.expression(
          '((C11*RED)-BLUE+C12)/((NIR*NIR)-(RED*RED))', {
          'C11': 0.55,
          'C12': 0.12,
          'RED': images.select('Nadir_Reflectance_Band1'),
          'BLUE': images.select('Nadir_Reflectance_Band3'),
          'NIR': images.select('Nadir_Reflectance_Band2')
          }).rename('H1')

 H2 = images.expression(
          '1/((C11*RED)-BLUE+C12)', {
          'C11': 0.55,
          'C12': 0.12,
          'RED': images.select('Nadir_Reflectance_Band1'),
          'BLUE': images.select('Nadir_Reflectance_Band3')
          }).rename('H2')

 mndvi = images.expression(
          '((1+(C2*H2))*NDVI)/(1+(C1*H1))', {
          'C1': 0.6,
          'C2': 0.03,
          'H1': H1,
          'H2': H2,
          'NDVI' : NDVI
          }).rename('MNDVI')

 return mndvi.set('year', year).set('month', 1).set('date', ee.Date.fromYMD(year,1,1)).set('system:time_start',ee.Date.fromYMD(year,1,1))


# In[5]:


mndvi_images = ee.ImageCollection([
    calculate_mndvi(year)
    for year in yearlist])


# In[6]:


#Thumbnail
parameter = {'min':0, 'max':1, 'palette':['e81410',  'f0fc0a',  '30bf21', '084f18']}
#Map.addLayer(mndvi_images,parameter,"MNDVI")

#Menambahkan file shp
pulau_Kalimantan_shp = 'SHP_Kalimantan/Pulau_Kalimantan_Clip.shp'
Danau_Kalimantan_shp = 'SHP_Kalimantan/Danau_Kalimantan.shp'
Tambang_Kalimantan_shp = 'SHP_Kalimantan/Tambang_Kalimantan.shp'

#Convert shp ke object ee
Pulau_Kalimantan = geemap.shp_to_ee(pulau_Kalimantan_shp)
Danau_Kalimantan = geemap.shp_to_ee(Danau_Kalimantan_shp)
Tambang_Kalimantan = geemap.shp_to_ee(Tambang_Kalimantan_shp)


# In[7]:


#Fungsi untuk mengambil setiap gambar didalam koleksi
def tresholdfunc(year):
    start_date = ee.Date.fromYMD(year, 1, 1)
    end_date = start_date.advance(1, 'year')
    
    image = mndvi_images \
        .filterDate(start_date, end_date) \
        .sort("year") \
        .first()
    
    return image


# In[8]:


#Fungsi menyatukan treshold pada gambar tiap tahun
years = ee.List.sequence(start_year, end_year)
year_list = years.getInfo()
images = years.map(tresholdfunc)

for index in range(0, 22):
    img = ee.Image(images.get(index))
    image = img.clip(Pulau_Kalimantan)
    threshold1 = image.updateMask(image.gte(-1.00).And(image.lte(0.20)).selfMask())
    threshold2 = image.updateMask(image.gte(0.21).And(image.lte(0.40)).selfMask().multiply(2))
    threshold3 = image.updateMask(image.gte(0.41).And(image.lte(0.60)).selfMask().multiply(3))
    threshold4 = image.updateMask(image.gte(0.61).And(image.lte(1.00)).selfMask().multiply(4))
    
    layer_name = "Vegetasi Tahun " + str(year_list[index])
    
    stack = ee.ImageCollection.fromImages([threshold1, threshold2, threshold3, threshold4])
    stacking = stack.mosaic()
    Map.addLayer(stacking, parameter, layer_name, value=False)


# In[9]:
# Menambahkan layer shape
Map.addLayer(Pulau_Kalimantan, {}, 'Batas Administrasi')
Map.addLayer(Danau_Kalimantan, {}, 'Danau Kalimantan')
Map.addLayer(Tambang_Kalimantan, {}, 'Tambang Kalimantan')

#Menambahkan Legenda
#add_legend = st.checkbox("Add a legend to the map", value=True)
legend_dict = {
    'Non Vegetasi': 'e81410',
    'Vegetasi Jarang': 'f0fc0a',
    'Vegatasi Sedang': '30bf21',
    'Vegatasi Rapat': '198f0d',
}

Map.add_legend(legend_title="Tingkat Kerapatan Vegetasi", legend_dict=legend_dict, position='bottomleft')

# In[10]:


# ################## ANIMATED THUMBNAIL ##########################
# out_gif=geemap.create_timelapse(
#     mndvi_images,
#     start_date='2001-01-01',
#     end_date='2021-12-31',
#     region=study_area,
#     frequency='year',
#     reducer='median',
#     date_format=None,
#     out_gif=None, 
#     vis_params=parameter,
#     dimensions=768,
#     frames_per_second=1,
#     crs='EPSG:3857',
#     overlay_data=None,
#     overlay_color='black',
#     overlay_width=1,
#     overlay_opacity=1.0,
#     title='Timelapse Vegetation Changes of Matano Kalimantan Island',
#     title_xy=('2%', '90%'),
#     add_text=True,
#     text_xy=('2%', '2%'),
#     text_sequence=None,
#     font_type='arial.ttf',
#     font_size=20,
#     font_color='white',
#     add_progress_bar=True,
#     progress_bar_color='white',
#     progress_bar_height=5,
#     loop=0,
#     mp4=False,
#     fading=False)
#m.addLayer(timeseries,parameter,"MNDVI")

#Map.centerObject(study_area, 5)
Map.to_streamlit()

st.subheader('Legend')
st.markdown(
"""
![](https://i.postimg.cc/g0hwvZdm/legend.png)
"""
)


