from config import passportFilePath

from xmlPassportReader import getOrderedChannelNums, readTableLengthWave

def getChannelNumsByWavesRange(startWaveLength, endWaveLength):
    channels = list()

    waveLengthTable = readTableLengthWave(passportFilePath)

    for waveLength in waveLengthTable.keys():
        if(startWaveLength <= waveLength <= endWaveLength):
            channel = waveLengthTable[waveLength]["ChannelNumber"]
            channels.append(channel)

    return channels

def orderChannelNums(channelNums):
    global passportFilePath

    channelsOrder = getOrderedChannelNums(passportFilePath)
    ordered = list()

    for channel in channelNums:
        channel = int(channel)
        ordered.append(channelsOrder[channel])

    return ordered

def removeAthmosphereInfluencedChannels(channels):
    athmosphereInfluencedChannels = [77, 78, 79, 80, 81, 82, 88, 89, 90, 91, 92, 109, 110, 111, 112, 113, 114, 115, 116]
    correctedChannels = list()

    for channel in channels:
        if channel not in athmosphereInfluencedChannels:
            correctedChannels.append(channel)

    return correctedChannels