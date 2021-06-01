import pandas as pd
import numpy as np
from sklearn import linear_model
import math


df = pd.read_csv('buffer_1_data.csv')

#  Data preeprocessing (Handle Missing Values)

# _wind_speed = df.wind_speed1.median()
# df.wind_speed1 = df.wind_speed1.fillna(_wind_speed)

# _temperature = df.temperature1.median()
# df.temperature1 = df.temperature1.fillna(_temperature)

# _satellite_NO2 = df.satellite_NO21.median()
# df.satellite_NO21 = df.satellite_NO21.fillna(_satellite_NO2)

# _road_density = df.road_density1.median()
# df.road_density1 = df.road_density1.fillna(_road_density)

# _relative_humidity = df.relative_humidity1.median()
# df.relative_humidity1 = df.relative_humidity1.fillna(_relative_humidity)

# _pressure = df.pressure1.median()
# df.pressure1 = df.pressure1.fillna(_pressure)

# _population_density = df.population_density1.median()
# df.population_density1 = df.population_density1.fillna(_population_density)

# _pblh = df.pblh1.median()
# df.pblh1 = df.pblh1.fillna(_pblh)

# _NDVI = df.NDVI1.median()
# df.NDVI1 = df.NDVI1.fillna(_NDVI)

# _dpt = df.dpt1.median()
# df.dpt1 = df.dpt1.fillna(_dpt)

# df.to_csv('buffer_1_data.csv', index=False)

# #2

# df = pd.read_csv('buffer_2_data.csv')

# #  Data preeprocessing (Handle Missing Values)

# _wind_speed = df.wind_speed2.median()
# df.wind_speed2 = df.wind_speed2.fillna(_wind_speed)

# _temperature = df.temperature2.median()
# df.temperature2 = df.temperature2.fillna(_temperature)

# _satellite_NO2 = df.satellite_NO22.median()
# df.satellite_NO22 = df.satellite_NO22.fillna(_satellite_NO2)

# _road_density = df.road_density2.median()
# df.road_density2 = df.road_density2.fillna(_road_density)

# _relative_humidity = df.relative_humidity2.median()
# df.relative_humidity2 = df.relative_humidity2.fillna(_relative_humidity)

# _pressure = df.pressure2.median()
# df.pressure2 = df.pressure2.fillna(_pressure)

# _population_density = df.population_density2.median()
# df.population_density2 = df.population_density2.fillna(_population_density)

# _pblh = df.pblh2.median()
# df.pblh2 = df.pblh2.fillna(_pblh)

# _NDVI = df.NDVI2.median()
# df.NDVI2 = df.NDVI2.fillna(_NDVI)

# _dpt = df.dpt2.median()
# df.dpt2 = df.dpt2.fillna(_dpt)

# df.to_csv('buffer_2_data.csv', index=False)

# #3

# df = pd.read_csv('buffer_3_data.csv')

# #  Data preeprocessing (Handle Missing Values)

# _wind_speed = df.wind_speed3.median()
# df.wind_speed3 = df.wind_speed3.fillna(_wind_speed)

# _temperature = df.temperature3.median()
# df.temperature3 = df.temperature3.fillna(_temperature)

# _satellite_NO2 = df.satellite_NO23.median()
# df.satellite_NO23 = df.satellite_NO23.fillna(_satellite_NO2)

# _road_density = df.road_density3.median()
# df.road_density3 = df.road_density3.fillna(_road_density)

# _relative_humidity = df.relative_humidity3.median()
# df.relative_humidity3 = df.relative_humidity3.fillna(_relative_humidity)

# _pressure = df.pressure3.median()
# df.pressure3 = df.pressure3.fillna(_pressure)

# _population_density = df.population_density3.median()
# df.population_density3 = df.population_density3.fillna(_population_density)

# _pblh = df.pblh3.median()
# df.pblh3 = df.pblh3.fillna(_pblh)

# _NDVI = df.NDVI3.median()
# df.NDVI3 = df.NDVI3.fillna(_NDVI)

# _dpt = df.dpt3.median()
# df.dpt3 = df.dpt3.fillna(_dpt)

# df.to_csv('buffer_3_data.csv', index=False)



a = pd.read_csv("buffer_1_data.csv")
b = pd.read_csv("buffer_2_data.csv")
merged = a.merge(b, on=['time', 'lat', 'long', 'name'], how='inner')
merged.to_csv('merge.csv', index=False)

c = pd.read_csv("merge.csv")
d = pd.read_csv("buffer_3_data.csv")
merged = c.merge(d, on=['time', 'lat', 'long', 'name'], how='inner')

merged.to_csv('merge.csv', index=False)


















# _road_dens = df.road_dens.median()
# df.road_dens = df.road_dens.fillna(_road_dens)

# _pp_dens = df.pp_dens.median()
# df.pp_dens = df.pp_dens.fillna(_pp_dens)

# _earth_no2 = df.earth_no2.median()
# df.earth_no2 = df.earth_no2.fillna(_earth_no2)




# # training model

# reg = linear_model.LinearRegression()
# reg.fit(df[['wind_speed', 'road_dens', 'pp_dens', 'earth_no2']], df.NO2)

# print(reg.coef_)
# # [-1.05050221e+02 -5.40138834e-02  1.60809930e+00  1.05491448e+02]
# print(reg.intercept_)
# # 511.7305174172126