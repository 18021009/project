from math import nan
from Station import station
import numpy as np
import datetime
import pandas as pd
from Map import map
from Point import point


def road_density(buffer = 0, dataFile = 'str') -> None:
    dataStation = pd.read_csv(dataFile)
    dataStationArray = dataStation.values
    

    _map = map()
    _map.setMap('map/road_density/road_dens.tif')
    for data in dataStationArray:
        _point = point(data[2], data[1])
        _point.set_position_on_matrix(_map)
        _station = station(_point, buffer)
        _station.setBufferValue(_map)

        data[8] = _station.bufferValue

    newDataStation = pd.DataFrame(dataStationArray, columns=['time', 'lat', 'long', 'NO2', 'name', 'wind_speed' + str(buffer), 'temperature' + str(buffer), 'satellite_NO2' + str(buffer), 'road_density' + str(buffer), 'relative_humidity' + str(buffer), 'pressure' + str(buffer), 'population_density' + str(buffer), 'pblh' + str(buffer), 'NDVI' + str(buffer), 'dpt' + str(buffer)])
    newDataStation.to_csv(dataFile, float_format='{:f}'.format, index=False)



road_density(1, 'buffer_1_data.csv')
road_density(2, 'buffer_2_data.csv')
road_density(3, 'buffer_3_data.csv')