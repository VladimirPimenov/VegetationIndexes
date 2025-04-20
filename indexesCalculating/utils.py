def calculateAvgPixelValue(pixelX, pixelY, channels):
    sumPixelValue = 0

    for channel in channels:
        sumPixelValue += channel[pixelY][pixelX]

    return sumPixelValue / len(channels)