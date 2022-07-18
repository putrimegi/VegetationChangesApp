#!/usr/bin/env python
# coding: utf-8

# In[3]:


import ee
import geemap


# In[4]:


js_snippet="""modis = ee.ImageCollection('MODIS/006/MCD43A4') \
              .filterBounds(table2)

#MEMILIH TAHUN
startYear = 2001
endYear = 2021

startdate=ee.Date.fromYMD(startYear,01,01)
enddate=ee.Date.fromYMD(endYear+1,12,31)
year_list = ee.List.sequence(startYear, endYear)

#CLOUD MASKING
def maskClouds(image):
  # Select the QA band.
  QA = image.select('BRDF_Albedo_Band_Mandatory_Quality_Band1')
  # Make a mask to get bit 10, the internal_cloud_algorithm_flag bit.
  bitMask = 1 << 10
  # Return an image masking out cloudy areas.
  return image.multiply(0.0001).updateMask(QA.bitwiseAnd(bitMask).eq(0))

#PERHITUNGAN MNDVI

def func_aei (ynz):
  images = modis.filter(ee.Filter.calendarRange(ynz, ynz, 'year')) \
              .map(maskClouds) \
              .mean()

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

              return mndvi.set('year', ynz).clip(table2) \
              .set('month', 1) \
              .set('date', ee.Date.fromYMD(ynz,1,1)) \
              .set('system:time_start',ee.Date.fromYMD(ynz,1,1))

mndvi_images =  ee.ImageCollection.fromImages(year_list.map(func_aei
).flatten())

).flatten())

print(mndvi_images, 'mNDVI')

for i in range(i=2019, i<=2021, 1):
  mndviresult = mndvi_images.filter(ee.Filter.eq('year', i)).first()
  mndvi_clipped = mndviresult.clip(table2)
  print(mndvi_clipped,'Nilai MNDVI'+i)

#KLASIFIKASI VEGETASI

  threshold1 = mndvi_clipped.select('MNDVI').gt(-1).And(mndvi_clipped.select('MNDVI').lt(0.2)).selfMask()
  threshold2 = mndvi_clipped.select('MNDVI').gt(0.2).And(mndvi_clipped.select('MNDVI').lt(0.4)).selfMask().multiply(2)
  threshold3 = mndvi_clipped.select('MNDVI').gt(0.4).And(mndvi_clipped.select('MNDVI').lt(0.6)).selfMask().multiply(3)
  threshold4 = mndvi_clipped.select('MNDVI').gt(0.6).And(mndvi_clipped.select('MNDVI').lt(1)).selfMask().multiply(4)

  threshold1 = threshold1.toShort().select(0).rename('MNDVI')
  threshold2 = threshold2.toShort().select(0).rename('MNDVI')
  threshold3 = threshold3.toShort().select(0).rename('MNDVI')
  threshold4 = threshold4.toShort().select(0).rename('MNDVI')

# STACKING LAYER
stacking_layer = ee.ImageCollection.fromImages([threshold1, threshold2, threshold3, threshold4])
print(stacking_layer,'staking'+i)
# Mosaic the ImageCollection.
stacking = stacking_layer.mosaic()
Map.addLayer(stacking, {'palette': ['e81410',  'f0fc0a',  '30bf21', '198f0d'], 'min':1, 'max':4},'Vegetasi'+i)

#MENAMPILKAN LAYER
#Map.addLayer(threshold1,{palette: 'e81410'}, 'Non Vegetasi '+i)
#Map.addLayer(threshold2,{palette: 'f0fc0a'}, 'Vegetasi Jarang '+i)
#Map.addLayer(threshold3,{palette: '30bf21'}, 'Vegetasi Sedang '+i)
#Map.addLayer(threshold4,{palette: '198f0d'}, 'Vegetasi Rapat '+i)
#  Map.addLayer(mndvi_clipped,mndviParams,'mDVI Result '+i)

#MENGHITUNG LUAS PIXEL
#stateArea = threshold1.geometry().area()
#stateAreaSqKm = ee.Number(stateArea).divide(1e6).round()
#print(stateAreaSqKm, 'Luasan Kelas 1 '+i)

#FOKUSAN AREA
Map.centerObject(table2)

studyarea = poligon

#MEMBUAT PANEL LEGENDA
panel=ui.Panel({
  'style': {
    'position':'bottom-left',
    'padding':'5px'
  }
})
color = ['e81410', 'f0fc0a', '30bf21','198f0d']
lc_class=['Non Vegetasi','Vegetasi Jarang','Vegetasi Sedang','Vegetasi Rapat']

def list_legend(color, desc):

  c=ui.Label({
    'style': {
      'backgroundColor': color,
      'padding':'10px'
    }
  })
  ds=ui.Label({
    'value': desc,
    'style':{
      'padding':'10px'
    }
  })
  return ui.Panel({
    'widgets':[c, ds],
    'layout': ui.Panel.Layout.Flow('horizontal')
  })

fora in range(a=0, a<4, 1):
  panel.add(list_legend(color[a], lc_class[a]))

Map.add(panel)

"""


# In[5]:


geemap.js_snippet_to_py(js_snippet, add_new_cell=True, import_ee=True, import_geemap=True, show_map=True)


# In[7]:


import ee
import geemap

Map = geemap.Map()
import geemap

Map = geemap.Map()

modis = ee.ImageCollection('MODIS/006/MCD43A4')               .filterBounds(table2)

#MEMILIH TAHUN
startYear = 2001
endYear = 2021

startdate=ee.Date.fromYMD(startYear,1,1)
enddate=ee.Date.fromYMD(endYear+1,12,31)
year_list = ee.List.sequence(startYear, endYear)

#CLOUD MASKING
def maskClouds(image):
  # Select the QA band.
  QA = image.select('BRDF_Albedo_Band_Mandatory_Quality_Band1')
  # Make a mask to get bit 10, the internal_cloud_algorithm_flag bit.
  bitMask = 1 << 10
  # Return an image masking out cloudy areas.
  return image.multiply(0.0001).updateMask(QA.bitwiseAnd(bitMask).eq(0))

#PERHITUNGAN MNDVI

def calculate_mndvi (year):
  images = modis \
              .filter(ee.Filter.calendarRange(year, year, 'year')) \
              .map(maskClouds) \
              .mean()

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

return mndvi\
    .set('year', year) \
    .set('month', 1) \
    .set('date', ee.Date.fromYMD(year,1,1)) \
    .set('system:time_start',ee.Date.fromYMD(year,1,1))

mndvi_images = ee.ImageCollection.fromImages([
    calculate_mndvi(year)
    for year in yearlist
])

print(mndvi_images.getInfo())
#KLASIFIKASI VEGETASI

  threshold1 = mndvi_images.select('MNDVI').gt(-1).And(mndvi_images.select('MNDVI').lt(0.2)).selfMask()
  threshold2 = mndvi_images.select('MNDVI').gt(0.2).And(mndvi_images.select('MNDVI').lt(0.4)).selfMask().multiply(2)
  threshold3 = mndvi_images.select('MNDVI').gt(0.4).And(mndvi_images.select('MNDVI').lt(0.6)).selfMask().multiply(3)
  threshold4 = mndvi_images.select('MNDVI').gt(0.6).And(mndvi_images.select('MNDVI').lt(1)).selfMask().multiply(4)

  threshold1 = threshold1.toShort().select(0).rename('MNDVI')
  threshold2 = threshold2.toShort().select(0).rename('MNDVI')
  threshold3 = threshold3.toShort().select(0).rename('MNDVI')
  threshold4 = threshold4.toShort().select(0).rename('MNDVI')

# STACKING LAYER
stacking_layer = ee.ImageCollection.fromImages([threshold1, threshold2, threshold3, threshold4])
print(stacking_layer,'staking'+i)
# Mosaic the ImageCollection.
stacking = stacking_layer.mosaic()
Map.addLayer(stacking, {'palette': ['e81410',  'f0fc0a',  '30bf21', '198f0d'], 'min':1, 'max':4},'Vegetasi'+i)

#MENAMPILKAN LAYER
#Map.addLayer(threshold1,{palette: 'e81410'}, 'Non Vegetasi '+i)
#Map.addLayer(threshold2,{palette: 'f0fc0a'}, 'Vegetasi Jarang '+i)
#Map.addLayer(threshold3,{palette: '30bf21'}, 'Vegetasi Sedang '+i)
#Map.addLayer(threshold4,{palette: '198f0d'}, 'Vegetasi Rapat '+i)
#  Map.addLayer(mndvi_clipped,mndviParams,'mDVI Result '+i)

#MENGHITUNG LUAS PIXEL
#stateArea = threshold1.geometry().area()
#stateAreaSqKm = ee.Number(stateArea).divide(1e6).round()
#print(stateAreaSqKm, 'Luasan Kelas 1 '+i)

#FOKUSAN AREA
Map.centerObject(table2)

studyarea = poligon

#MEMBUAT PANEL LEGENDA
panel=ui.Panel({
  'style': {
    'position':'bottom-left',
    'padding':'5px'
  }
})
color = ['e81410', 'f0fc0a', '30bf21','198f0d']
lc_class=['Non Vegetasi','Vegetasi Jarang','Vegetasi Sedang','Vegetasi Rapat']

def list_legend(color, desc):

  c=ui.Label({
    'style': {
      'backgroundColor': color,
      'padding':'10px'
    }
  })
  ds=ui.Label({
    'value': desc,
    'style':{
      'padding':'10px'
    }
  })
  return ui.Panel({
    'widgets':[c, ds],
    'layout': ui.Panel.Layout.Flow('horizontal')
  })

fora in range(a=0, a<4, 1):
  panel.add(list_legend(color[a], lc_class[a]))

Map.add(panel)

MapMap


# In[ ]:




