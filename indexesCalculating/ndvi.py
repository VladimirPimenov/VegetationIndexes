from .utils import calculateAvgPixelValue

import numpy as np

def calculateNDVIforChannels(redChannels: np.ndarray, nirChannels: np.ndarray) -> np.ndarray:
    NDVIimage = np.zeros((redChannels.shape[1], redChannels.shape[2]))
    
    height = redChannels.shape[1]
    width = redChannels.shape[2]

    for y in range(height):
        for x in range(width):
            redAvgPixelValue = calculateAvgPixelValue(x, y, redChannels)
            nirAvgPixelValue = calculateAvgPixelValue(x, y, nirChannels)

            NDVIimage[y][x] = calculateNDVI(redAvgPixelValue, nirAvgPixelValue)

    return NDVIimage

def calculateNDVI(red, nir):
    ndvi = (nir - red) / (nir + red)
    return ndvi