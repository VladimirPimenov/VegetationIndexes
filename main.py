import numpy as np

from tifFileHandler import saveTifAsMat, readHSIChannelFromMat
from xmlPassportReader import readTableLengthWave, getOrderedChannelNums
from visualizer import showNDVI
import indexesCalculator

hsiPath = "./0041_0306_34728_1_04894_06_L1A.tif"
channelsMatFilePath = "./hsi.mat"
passportFilePath = "./0041_0306_34728_1_04894_06_L1A.xml"

def getChannelNumsByWavesRange(startWaveLength, endWaveLength, channelTable):
    channels = list()

    for waveLength in channelTable.keys():
        if(startWaveLength <= waveLength <= endWaveLength):
            channels.append(channelTable[waveLength]["ChannelNumber"])

    return channels

def orderChannelNums(channelNums):
    global passportFilePath

    channelsOrder = getOrderedChannelNums(passportFilePath)
    ordered = list()

    for channel in channelNums:
        channel = int(channel)
        ordered.append(channelsOrder[channel])

    return ordered

def simpleNDVIcalculating(redChannelNum, nirChannelNum):
    global channelsMatFilePath

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
    global channelsMatFilePath
    global passportFilePath

    waveLengthTable = readTableLengthWave(passportFilePath)
    channelsOrder = getOrderedChannelNums(passportFilePath)

    redChannelNums = getChannelNumsByWavesRange(redWavesRange[0], redWavesRange[1], waveLengthTable)
    redChannelNums = orderChannelNums(redChannelNums)

    nirChannelNums = getChannelNumsByWavesRange(nirWavesRange[0], nirWavesRange[1], waveLengthTable)
    nirChannelNums = orderChannelNums(nirChannelNums)

    print(f"Red channels: {redChannelNums}")
    print(f"Nir channels: {nirChannelNums}")

    redChannels = np.zeros((len(redChannelNums), 2388, 999))
    nirChannels = np.zeros((len(nirChannelNums), 2388, 999))
    fillChannelsFromMat(channelsMatFilePath, redChannels, redChannelNums)
    fillChannelsFromMat(channelsMatFilePath, nirChannels, nirChannelNums)

    ndvi = indexesCalculator.calculateNDVIforChannels(redChannels, nirChannels)
    showNDVI(ndvi)

def fillChannelsFromMat(channelsMatFilePath, channels, channelNums):
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