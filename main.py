from config import channelsMatFilePath

from tifFileHandler import saveTifAsMat, readHSIChannelFromMat
from channelUtils import orderChannelNums, getChannelNumsByWavesRange, removeAthmosphereInfluencedChannels
from rgbConverter import convertNDVItoRGB
from maskCreator import createMaskFromNDVI
import indexesCalculating

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def simpleNDVIcalculating(redChannelNum, nirChannelNum):
    redChannelNum = orderChannelNums([redChannelNum])[0]
    nirChannelNum = orderChannelNums([nirChannelNum])[0]

    redChannel = readHSIChannelFromMat(channelsMatFilePath, redChannelNum)
    redChannel = np.array([redChannel])

    nirChannel = readHSIChannelFromMat(channelsMatFilePath, nirChannelNum)
    nirChannel = np.array([nirChannel])

    ndvi = indexesCalculating.calculateNDVIforChannels(redChannel, nirChannel)
    return ndvi    
def rangeNDVIcalculating(redWavesRange, nirWavesRange):
    redChannelNums = getChannelNumsByWavesRange(redWavesRange[0], redWavesRange[1])
    redChannelNums = orderChannelNums(redChannelNums)
    redChannelNums = removeAthmosphereInfluencedChannels(redChannelNums)

    nirChannelNums = getChannelNumsByWavesRange(nirWavesRange[0], nirWavesRange[1])
    nirChannelNums = orderChannelNums(nirChannelNums)
    nirChannelNums = removeAthmosphereInfluencedChannels(nirChannelNums)

    print(f"Red channels: {redChannelNums}")
    print(f"Nir channels: {nirChannelNums}")

    redChannels = np.zeros((len(redChannelNums), 2388, 999))
    nirChannels = np.zeros((len(nirChannelNums), 2388, 999))
    fillChannelsFromMat(redChannels, redChannelNums)
    fillChannelsFromMat(nirChannels, nirChannelNums)

    ndvi = indexesCalculating.calculateNDVIforChannels(redChannels, nirChannels)
    return ndvi

def simpleARVIcalculating(redChannelNum, nirChannelNum, blueChannelNum):
    redChannelNum = orderChannelNums([redChannelNum])[0]
    blueChannelNum = orderChannelNums([blueChannelNum])[0]
    nirChannelNum = orderChannelNums([nirChannelNum])[0]

    redChannel = readHSIChannelFromMat(channelsMatFilePath, redChannelNum)
    redChannel = np.array([redChannel])

    blueChannel = readHSIChannelFromMat(channelsMatFilePath, blueChannelNum)
    blueChannel = np.array([blueChannel])

    nirChannel = readHSIChannelFromMat(channelsMatFilePath, nirChannelNum)
    nirChannel = np.array([nirChannel])

    arvi = indexesCalculating.calculateARVIforChannels(redChannel, nirChannel, blueChannel, 0.5)
    return arvi
def rangeARVIcalculating(redWavesRange, nirWavesRange, blueWavesRange):
    redChannelNums = getChannelNumsByWavesRange(redWavesRange[0], redWavesRange[1])
    redChannelNums = orderChannelNums(redChannelNums)

    nirChannelNums = getChannelNumsByWavesRange(nirWavesRange[0], nirWavesRange[1])
    nirChannelNums = orderChannelNums(nirChannelNums)

    blueChannelNums = getChannelNumsByWavesRange(blueWavesRange[0], blueWavesRange[1])
    blueChannelNums = orderChannelNums(blueChannelNums)

    print(f"Red channels: {redChannelNums}")
    print(f"Nir channels: {nirChannelNums}")
    print(f"Blue channels: {blueChannelNums}")

    redChannels = np.zeros((len(redChannelNums), 2388, 999))
    nirChannels = np.zeros((len(nirChannelNums), 2388, 999))
    blueChannels = np.zeros((len(blueChannelNums), 2388, 999))
    fillChannelsFromMat(redChannels, redChannelNums)
    fillChannelsFromMat(nirChannels, nirChannelNums)
    fillChannelsFromMat(blueChannels, blueChannelNums)

    arvi = indexesCalculating.calculateARVIforChannels(redChannels, nirChannels, blueChannels, 0.5)
    return arvi

def simpleSAVIcalculating(redChannelNum, nirChannelNum):
    redChannelNum = orderChannelNums([redChannelNum])[0]
    nirChannelNum = orderChannelNums([nirChannelNum])[0]

    redChannel = readHSIChannelFromMat(channelsMatFilePath, redChannelNum)
    redChannel = np.array([redChannel])

    nirChannel = readHSIChannelFromMat(channelsMatFilePath, nirChannelNum)
    nirChannel = np.array([nirChannel])

    savi = indexesCalculating.calculateSAVIforChannels(redChannel, nirChannel, 0.5)
    return savi
def rangeSAVIcalculating(redWavesRange, nirWavesRange):
    redChannelNums = getChannelNumsByWavesRange(redWavesRange[0], redWavesRange[1])
    redChannelNums = orderChannelNums(redChannelNums)

    nirChannelNums = getChannelNumsByWavesRange(nirWavesRange[0], nirWavesRange[1])
    nirChannelNums = orderChannelNums(nirChannelNums)

    print(f"Red channels: {redChannelNums}")
    print(f"Nir channels: {nirChannelNums}")

    redChannels = np.zeros((len(redChannelNums), 2388, 999))
    nirChannels = np.zeros((len(nirChannelNums), 2388, 999))
    fillChannelsFromMat(redChannels, redChannelNums)
    fillChannelsFromMat(nirChannels, nirChannelNums)

    savi = indexesCalculating.calculateSAVIforChannels(redChannels, nirChannels, 0.5)
    return savi

def fillChannelsFromMat(channels, channelNums):
    currentChannel = 0

    for channelNum in channelNums:
            channels[currentChannel] = readHSIChannelFromMat(channelsMatFilePath, channelNum)
            currentChannel += 1

def main():
    #ndvi = simpleNDVIcalculating(72, 85)
    #ndvi = rangeNDVIcalculating([630, 750], [750, 1400])

    #mask = createMaskFromNDVI(ndvi)
    #ndvi = convertNDVItoRGB(ndvi)

    # img = Image.fromarray(mask)
    # img.save("mask.png")

    #arvi = simpleARVIcalculating(75, 85, 14)
    arvi = rangeARVIcalculating([630, 750], [750, 1400], [440, 485])

    plt.imshow(arvi)
    plt.show()

    #savi = simpleSAVIcalculating(72, 85)
    #savi = rangeSAVIcalculating([630, 750], [750, 1400])


if __name__ == "__main__":
    main()