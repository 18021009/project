from math import nan
from os import name
from Station import station
import numpy as np
import datetime
import pandas as pd
from Map import map
from Point import point

# standardline date data.csv to college.csv

# ds = pd.read_csv('data.csv')

def changeToDate(output_file):
    ds = pd.read_csv('data.csv')

    day_delta = datetime.timedelta(days=1)
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2020, 1, 1)
    for i in range((end_date - start_date).days):
        day = start_date + i*day_delta
        _day = day.strftime('X%m/X%d/%Y').replace('X0','X').replace('X','')
        ds['time'] = ds['time'].replace({_day: day})
        ds.to_csv(output_file, index=False)

def buffer_data(input_file, buffer):

    dataStation = pd.read_csv(input_file)
    dataStation['wind_speed'] = nan
    dataStation['temperature'] = nan
    dataStation['satellite_NO2'] = nan
    dataStation["road_density"] = nan
    dataStation["relative_humidity"] = nan
    dataStation["pressure"] = nan
    dataStation["population_density"] = nan
    dataStation["pblh"] = nan
    dataStation["NDVI"] = nan
    dataStation["dpt"] = nan

    dataStationArray = dataStation.values
    dataStation = pd.DataFrame(dataStationArray, columns=['time', 'lat', 'long', 'NO2', 'name', 'wind_speed' + str(buffer), 'temperature' + str(buffer), 'satellite_NO2' + str(buffer), 'road_density' + str(buffer), 'relative_humidity' + str(buffer), 'pressure' + str(buffer), 'population_density' + str(buffer), 'pblh' + str(buffer), 'NDVI' + str(buffer), 'dpt' + str(buffer)])
    dataStation.to_csv(input_file, float_format='{:f}'.format, index=False)


changeToDate('buffer_1_data.csv')
buffer_data('buffer_1_data.csv', 1)

changeToDate('buffer_2_data.csv')
buffer_data('buffer_2_data.csv', 2)


changeToDate('buffer_3_data.csv')
buffer_data('buffer_3_data.csv', 3)


# a = pd.read_csv("buffer_1_data.csv")
# b = pd.read_csv("buffer_2_data.csv")
# merged = a.merge(b, on=['time', 'lat', 'long', 'name'], how='inner')
# merged.to_csv('merge.csv', index=False)

# c = pd.read_csv("merge.csv")
# d = pd.read_csv("buffer_3_data.csv")
# merged = c.merge(d, on=['time', 'lat', 'long', 'name'], how='inner')

# merged.to_csv('merge.csv', index=False)





# buffer_radius

# _buffer_radius = 1

# dataStation = pd.read_csv('college.csv')
# dataStation['wind_speed'] = -999.0
# dataStation["road_dens"] = -999.0
# dataStation["pp_dens"] = -999.0
# dataStation["earth_no2"] = -999.0

# dataStationArray = dataStation.values


# # add wind speed to dataStationArray

# start_date = datetime.date(2019, 1, 1)
# end_date = datetime.date(2020, 1, 1)
# day_delta = datetime.timedelta(days=1)

# for i in range((end_date - start_date).days):
#     fileName = "WSPDCombine_"
#     day = start_date + i*day_delta
#     file = "map/wind_speed/" + fileName + day.strftime('%Y%m%d') + ".tif"
#     _map = map()
#     _map.setMap(file)
#     for data in dataStationArray:
#         if((data[0] == day.strftime('%Y-%m-%d'))):
#             _point = point(data[2], data[1])
#             _point.set_position_on_matrix(_map)
#             _station = station(_point, _buffer_radius)
#             _station.setBufferValue(_map)
#             data[5] = np.float64(_station.bufferValue)



# #  add road to college.csv


# _map = map()
# _map.setMap('map/road_density/road_dens.tif')

# for data in dataStationArray:
#     _point = point(data[2], data[1])
#     _point.set_position_on_matrix(_map)
#     _station = station(_point, _buffer_radius)
#     _station.setBufferValue(_map)

#     data[6] = _station.bufferValue

# # add population_density
# _map = map()
# _map.setMap('map/population_density/ppd.tif')

# for data in dataStationArray:
#     _point = point(data[2], data[1])
#     _point.set_position_on_matrix(_map)
#     _station = station(_point, _buffer_radius)
#     _station.setBufferValue(_map)

#     data[7] = _station.bufferValue


# # add earth_no2

# for i in range((end_date - start_date).days):
#     fileName = "NO2_"
#     day = start_date + i*day_delta
#     file = "map/NO2/" + fileName + day.strftime('%Y%m%d') + ".tif"
#     _map = map()
#     _map.setMap(file)
#     for data in dataStationArray:
#         if((data[0] == day.strftime('%Y-%m-%d'))):
#             _point = point(data[2], data[1])
#             _point.set_position_on_matrix(_map)
#             _station = station(_point, _buffer_radius)
#             _station.setBufferValue(_map)
#             data[8] = _station.bufferValue

# newDataStation = pd.DataFrame(dataStationArray, columns=['time', 'lat', 'long', 'NO2', 'name', 'wind_speed', 'road_dens', 'pp_dens', 'earth_no2'])

# newDataStation.to_csv('college_2.csv', float_format='{:f}'.format, index=False)




