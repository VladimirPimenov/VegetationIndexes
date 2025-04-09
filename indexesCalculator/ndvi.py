import numpy as np

def calculateNDVIforChannels(redChannels: np.ndarray, nirChannels: np.ndarray) -> np.ndarray:
    NDVIimage = np.zeros((redChannels.shape[1], redChannels.shape[2]))
    
    channelCount = redChannels.shape[0]
    height = redChannels.shape[1]
    width = redChannels.shape[2]

    for channelNum in range(channelCount):
        for y in range(height):
            for x in range(width):
                redAvgPixelValue = calculateAvgPixelValue(x, y, redChannels)
                nirAvgPixelValue = calculateAvgPixelValue(x, y, nirChannels)

                NDVIpixel = calculateNDVI(redAvgPixelValue, nirAvgPixelValue)
                NDVIimage[y][x] = 100 * (NDVIpixel + 1)

    return NDVIimage

def calculateNDVI(red, nir):
    ndvi = (nir - red) / (nir + red)
    return ndvi

def calculateAvgPixelValue(pixelX, pixelY, channels):
    sumPixelValue = 0

    for channel in channels:
        sumPixelValue += channel[pixelY][pixelX]

    return sumPixelValue / len(channels)