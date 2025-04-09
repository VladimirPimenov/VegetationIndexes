from osgeo import gdal
import numpy as np
from scipy.io import savemat, loadmat

def open_raster(p_file_name):
    return gdal.Open(p_file_name)


def get_shape(p_raster):
    return p_raster.RasterYSize, p_raster.RasterXSize, p_raster.RasterCount


def print_raster_info(p_raster):
    print('YSize: ' + str(p_raster.RasterYSize) + '\n' +
          'XSize: ' + str(p_raster.RasterXSize) + '\n' +
          'NBands: ' + str(p_raster.RasterCount))


def get_band(p_raster, p_band_num):
    return p_raster.GetRasterBand(p_band_num).ReadAsArray()

def saveTifAsMat(sourcePath, savePath):
    raster = open_raster(sourcePath)
    rows, cols, n_bands = get_shape(raster)
    hsi = np.zeros((rows, cols, n_bands))

    for n in range(1, n_bands + 1):
        hsi[:,:,n-1] = get_band(raster, n)
        print(f'{n}/{n_bands}')

    savemat(savePath, {'hsi':hsi})

def readHSIChannelFromMat(matFile: str, channel: int) -> np.ndarray:
    mat = loadmat(matFile)
    hsi = np.array(mat['hsi'])

    width = hsi.shape[1]
    height = hsi.shape[0]

    hsiChannel = np.zeros((height, width))

    for row in range(0, height):
        for col in range(0, width):
            hsiChannel[row][col] = hsi[row][col][channel]

    return hsiChannel