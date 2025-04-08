import numpy as np

from tifFileHandler import saveTifAsMat, readHSIChannelFromMat
from xmlPassportParser import readTableLengthWave

def getChannelNumsByWavesRange(startWaveLength, endWaveLength, channelTable):
    channels = list()

    for waveLength in channelTable.keys():
        if(startWaveLength <= waveLength <= endWaveLength):
            channels.append(channelTable[waveLength])

    return channels

def main():
    hsiPath = "./0041_0306_34728_1_04894_06_L1A.tif"
    matSavePath = "./hsi.mat"
    passportFilePath = "./0041_0306_34728_1_04894_06_L1A.xml"

    channelTable = readTableLengthWave(passportFilePath)

    redChannelNums = getChannelNumsByWavesRange(630, 750, channelTable)
    nirChannelNums = getChannelNumsByWavesRange(750, 1400, channelTable)
    #hsiShape = (2388, 999)

    print(redChannelNums)
    print(nirChannelNums)

if __name__ == "__main__":
    main()