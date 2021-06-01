from math import nan
from Station import station
import numpy as np
import datetime
import pandas as pd
from Map import map
from Point import point


# buffer_radius

# _buffer_radius = 1

# dataStation = pd.read_csv('college.csv')
# dataStation['wind_speed'] = -999.0

# dataStationArray = dataStation.values


# # # add wind speed to dataStationArray

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

# newDataStation = pd.DataFrame(dataStationArray, columns=['time', 'lat', 'long', 'NO2', 'name', 'wind_speed'])
# newDataStation.to_csv('buffer_1_data.csv', float_format='{:f}'.format, index=False)



def NDVI(buffer = 0, dataFile = 'str') -> None:
    dataStation = pd.read_csv(dataFile)
    dataStationArray = dataStation.values
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2020, 1, 1)
    day_delta = datetime.timedelta(days=1)

    for i in range(int((end_date - start_date).days / 16)):
        fileName = "MOD13Q1_"
        day = start_date + i*16*day_delta
        file = "map/NDVI/" + fileName + day.strftime('%Y%m%d') + "_Ndvi" + ".tif"
        _map = map()
        _map.setMap(file)
        for data in dataStationArray:
            if((data[0] == day.strftime('%Y-%m-%d'))):
                _point = point(data[2], data[1])
                _point.set_position_on_matrix(_map)
                _station = station(_point, buffer)
                _station.setBufferValue(_map)
                data[13] = np.float64(_station.bufferValue)

    newDataStation = pd.DataFrame(dataStationArray, columns=['time', 'lat', 'long', 'NO2', 'name', 'wind_speed' + str(buffer), 'temperature' + str(buffer), 'satellite_NO2' + str(buffer), 'road_density' + str(buffer), 'relative_humidity' + str(buffer), 'pressure' + str(buffer), 'population_density' + str(buffer), 'pblh' + str(buffer), 'NDVI' + str(buffer), 'dpt' + str(buffer)])
    newDataStation.to_csv(dataFile, float_format='{:f}'.format, index=False)



NDVI(1, 'buffer_1_data.csv')
NDVI(2, 'buffer_2_data.csv')
NDVI(3, 'buffer_3_data.csv')