from .utils import calculateAvgPixelValue

import numpy as np

def calculateSAVIforChannels(redChannels: np.ndarray, nirChannels: np.ndarray, L: int) -> np.ndarray:
    GEMIimage = np.zeros((redChannels.shape[1], redChannels.shape[2]))
    
    height = redChannels.shape[1]
    width = redChannels.shape[2]

    for y in range(height):
        for x in range(width):
            redAvgPixelValue = calculateAvgPixelValue(x, y, redChannels)
            nirAvgPixelValue = calculateAvgPixelValue(x, y, nirChannels)

            GEMIimage[y][x] = calculateSAVI(redAvgPixelValue, nirAvgPixelValue, L)

    return GEMIimage

def calculateSAVI(red, nir, L):
    savi = ((nir - red) / (nir + red + L)) * (1 + L)
    return savi