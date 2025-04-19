from config import channelsMatFilePath

from tifFileHandler import saveTifAsMat, readHSIChannelFromMat
from channelUtils import orderChannelNums, getChannelNumsByWavesRange
from visualizer import showNDVI
import indexesCalculator

import numpy as np

def simpleNDVIcalculating(redChannelNum, nirChannelNum):
    redChannelNum = orderChannelNums([redChannelNum])[0]
    nirChannelNum = orderChannelNums([nirChannelNum])[0]

    redChannel = readHSIChannelFromMat(channelsMatFilePath, redChannelNum)
    redChannel = np.array([redChannel])
    print(f"Channel {redChannelNum} readed")

    nirChannel = readHSIChannelFromMat(channelsMatFilePath, nirChannelNum)
    nirChannel = np.array([nirChannel])
    print(f"Channel {nirChannelNum} readed")

    ndvi = indexesCalculator.calculateNDVIforChannels(redChannel, nirChannel)
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

    ndvi = indexesCalculator.calculateNDVIforChannels(redChannels, nirChannels)
    showNDVI(ndvi)

def fillChannelsFromMat(channels, channelNums):
    currentChannel = 0

    for channelNum in channelNums:
            channels[currentChannel] = readHSIChannelFromMat(channelsMatFilePath, channelNum)
            currentChannel += 1

            print(f"Channel {channelNum} readed")

def main():
    simpleNDVIcalculating(72, 85)

    #rangeNDVIcalculating([630, 635], [750, 755])

if __name__ == "__main__":
    main()