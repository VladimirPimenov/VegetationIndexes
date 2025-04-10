import numpy as np

from tifFileHandler import saveTifAsMat, readHSIChannelFromMat
from xmlPassportParser import readTableLengthWave
from visualizer import showNDVI
import indexesCalculator

def getChannelNumsByWavesRange(startWaveLength, endWaveLength, channelTable):
    channels = list()

    for waveLength in channelTable.keys():
        if(startWaveLength <= waveLength <= endWaveLength):
            channels.append(channelTable[waveLength])

    return channels

def fillChannelsFromMat(matPath, channels, channelNums):
    currentChannel = 0

    for channelNum in channelNums:
            channels[currentChannel] = readHSIChannelFromMat(matPath, channelNum)
            currentChannel += 1

            print(f"Channel {channelNum} readed")

def main():
    hsiPath = "./0041_0306_34728_1_04894_06_L1A.tif"
    matSavePath = "./hsi.mat"
    passportFilePath = "./0041_0306_34728_1_04894_06_L1A.xml"

    # channel72 = readHSIChannelFromMat(matSavePath, 72)
    # redChannels = np.array([channel72])
    # print("channel72 readed")

    # channel85 = readHSIChannelFromMat(matSavePath, 85)
    # nirChannels = np.array([channel85])
    # print("channe82 readed")

    channelTable = readTableLengthWave(passportFilePath)

    redChannelNums = getChannelNumsByWavesRange(630, 750, channelTable)
    nirChannelNums = getChannelNumsByWavesRange(750, 850, channelTable)
    redChannels = np.zeros((len(redChannelNums), 2388, 999))
    nirChannels = np.zeros((len(nirChannelNums), 2388, 999))

    print(redChannelNums)
    print(nirChannelNums)

    fillChannelsFromMat(matSavePath, redChannels, redChannelNums)
    fillChannelsFromMat(matSavePath, nirChannels, nirChannelNums)

    ndvi = indexesCalculator.calculateNDVIforChannels(redChannels, nirChannels)

    showNDVI(ndvi)

if __name__ == "__main__":
    main()