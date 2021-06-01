from math import nan
from Station import station
import numpy as np
import datetime
import pandas as pd
from Map import map
from Point import point


def dpt(buffer = 0, dataFile = 'str') -> None:
    dataStation = pd.read_csv(dataFile)
    dataStationArray = dataStation.values
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2020, 1, 1)
    day_delta = datetime.timedelta(days=1)

    for i in range((end_date - start_date).days):
        fileName = "DPT_"
        day = start_date + i*day_delta
        file = "map/dpt/" + fileName + day.strftime('%Y%m%d') + '_00' ".tif"
        _map = map()
        _map.setMap(file)
        for data in dataStationArray:
            if((data[0] == day.strftime('%Y-%m-%d'))):
                _point = point(data[2], data[1])
                _point.set_position_on_matrix(_map)
                _station = station(_point, buffer)
                _station.setBufferValue(_map)
                data[14] = np.float64(_station.bufferValue)

    newDataStation = pd.DataFrame(dataStationArray, columns=['time', 'lat', 'long', 'NO2', 'name', 'wind_speed' + str(buffer), 'temperature' + str(buffer), 'satellite_NO2' + str(buffer), 'road_density' + str(buffer), 'relative_humidity' + str(buffer), 'pressure' + str(buffer), 'population_density' + str(buffer), 'pblh' + str(buffer), 'NDVI' + str(buffer), 'dpt' + str(buffer)])
    newDataStation.to_csv(dataFile, float_format='{:f}'.format, index=False)



dpt(1, 'buffer_1_data.csv')
dpt(2, 'buffer_2_data.csv')
dpt(3, 'buffer_3_data.csv')