from .utils import calculateAvgPixelValue

import numpy as np

def calculateARVIforChannels(redChannels: np.ndarray, 
                            nirChannels: np.ndarray, 
                            blueChannels: np.ndarray,
                            alpha: int) -> np.ndarray:
    ARVIimage = np.zeros((redChannels.shape[1], redChannels.shape[2]))
    
    height = redChannels.shape[1]
    width = redChannels.shape[2]

    for y in range(height):
        for x in range(width):
            redAvgPixelValue = calculateAvgPixelValue(x, y, redChannels)
            nirAvgPixelValue = calculateAvgPixelValue(x, y, nirChannels)
            blueAvgPixelValue = calculateAvgPixelValue(x, y, blueChannels)

            ARVIimage[y][x] = calculateARVI(redAvgPixelValue, 
                                            nirAvgPixelValue, 
                                            blueAvgPixelValue, 
                                            alpha)

    return ARVIimage

def calculateARVI(red, nir, blue, alpha):
    rb = red - alpha*(red - blue)
    arvi = (nir - rb) / (nir + rb)
    return arvi