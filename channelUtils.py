from config import passportFilePath

from xmlPassportReader import getOrderedChannelNums, readTableLengthWave

def getChannelNumsByWavesRange(startWaveLength, endWaveLength):
    channels = list()

    waveLengthTable = readTableLengthWave(passportFilePath)

    for waveLength in waveLengthTable.keys():
        if(startWaveLength <= waveLength <= endWaveLength):
            channels.append(waveLengthTable[waveLength]["ChannelNumber"])

    return channels

def orderChannelNums(channelNums):
    global passportFilePath

    channelsOrder = getOrderedChannelNums(passportFilePath)
    ordered = list()

    for channel in channelNums:
        channel = int(channel)
        ordered.append(channelsOrder[channel])

    return ordered
