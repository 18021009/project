from osgeo import gdal
import numpy as np

class map:
    def __init__(self, matrix = None, mapInfo = None, _left = 0, _right = 0, _top = 0, _bottom = 0, _matrixSizeX = 0, _matrixSizeY = 0) -> None:
        self.matrix = matrix
        self.mapInfo = mapInfo
        self.left = _left
        self.right = _right
        self.top = _top
        self.bottom = _bottom
        self.matrixSizeX = _matrixSizeX
        self.matrixSizeY = _matrixSizeY

    def setMap(self, _file) -> None:
        dataset = gdal.Open(_file, gdal.GA_ReadOnly)
        self.mapInfo = dataset.GetGeoTransform()

        self.top = self.mapInfo[3]
        self.left = self.mapInfo[0]
        self.bottom = self.mapInfo[3] + self.mapInfo[5]*dataset.RasterYSize
        self.right = self.mapInfo[0] + self.mapInfo[1]*dataset.RasterXSize
        self.matrixSizeX = dataset.RasterXSize
        self.matrixSizeY = dataset.RasterYSize

        self.matrix = np.array(dataset.GetRasterBand(1).ReadAsArray())








