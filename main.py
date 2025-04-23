from config import channelsMatFilePath

from tifFileHandler import saveTifAsMat, readHSIChannelFromMat
from channelUtils import orderChannelNums, getChannelNumsByWavesRange
from visualizer import showNDVI, convertNDVItoRGB
import indexesCalculating

import numpy as np
from matplotlib import pyplot as plt

def simpleNDVIcalculating(redChannelNum, nirChannelNum):
    redChannelNum = orderChannelNums([redChannelNum])[0]
    nirChannelNum = orderChannelNums([nirChannelNum])[0]

    redChannel = readHSIChannelFromMat(channelsMatFilePath, redChannelNum)
    redChannel = np.array([redChannel])
    print(f"Channel {redChannelNum} readed")

    nirChannel = readHSIChannelFromMat(channelsMatFilePath, nirChannelNum)
    nirChannel = np.array([nirChannel])
    print(f"Channel {nirChannelNum} readed")

    ndvi = indexesCalculating.calculateNDVIforChannels(redChannel, nirChannel)
    showNDVI(ndvi)
def rangeNDVIcalculating(redWavesRange, nirWavesRange):
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

    ndvi = indexesCalculating.calculateNDVIforChannels(redChannels, nirChannels)
    showNDVI(ndvi)

def simpleARVIcalculating(redChannelNum, nirChannelNum, blueChannelNum):
    redChannelNum = orderChannelNums([redChannelNum])[0]
    blueChannelNum = orderChannelNums([blueChannelNum])[0]
    nirChannelNum = orderChannelNums([nirChannelNum])[0]

    redChannel = readHSIChannelFromMat(channelsMatFilePath, redChannelNum)
    redChannel = np.array([redChannel])
    print(f"Channel {redChannelNum} readed")

    blueChannel = readHSIChannelFromMat(channelsMatFilePath, blueChannelNum)
    blueChannel = np.array([blueChannel])
    print(f"Channel {blueChannelNum} readed")

    nirChannel = readHSIChannelFromMat(channelsMatFilePath, nirChannelNum)
    nirChannel = np.array([nirChannel])
    print(f"Channel {nirChannelNum} readed")

    arvi = indexesCalculating.calculateARVIforChannels(redChannel, nirChannel, blueChannel, 0.5)
    
    arvi = convertNDVItoRGB(arvi)
    plt.imshow(arvi)
    plt.show()
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
    arvi = convertNDVItoRGB(arvi)

    plt.imshow(arvi)
    plt.show()

def simpleSAVIcalculating(redChannelNum, nirChannelNum):
    redChannelNum = orderChannelNums([redChannelNum])[0]
    nirChannelNum = orderChannelNums([nirChannelNum])[0]

    redChannel = readHSIChannelFromMat(channelsMatFilePath, redChannelNum)
    redChannel = np.array([redChannel])
    print(f"Channel {redChannelNum} readed")

    nirChannel = readHSIChannelFromMat(channelsMatFilePath, nirChannelNum)
    nirChannel = np.array([nirChannel])
    print(f"Channel {nirChannelNum} readed")

    savi = indexesCalculating.calculateSAVIforChannels(redChannel, nirChannel, 0.5)

    plt.imshow(savi)
    plt.show()
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

    plt.imshow(savi)
    plt.show()

def fillChannelsFromMat(channels, channelNums):
    currentChannel = 0

    for channelNum in channelNums:
            channels[currentChannel] = readHSIChannelFromMat(channelsMatFilePath, channelNum)
            currentChannel += 1

            print(f"Channel {channelNum} readed")

def main():
    #simpleNDVIcalculating(72, 85)
    #rangeNDVIcalculating([630, 635], [750, 755])

    #simpleARVIcalculating(75, 85, 14)
    #rangeARVIcalculating([630, 750], [750, 1400], [440, 485])

    simpleSAVIcalculating(72, 85)
    rangeSAVIcalculating([630, 750], [750, 1400])

if __name__ == "__main__":
    main()