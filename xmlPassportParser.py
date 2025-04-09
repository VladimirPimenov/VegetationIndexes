def readTableLengthWave(passportFilePath: str) -> dict:
    channelWavesLength = dict()

    xmlPassportFile = open(passportFilePath, "r")

    tableOpenTag = "<TableLengthWave>"
    tableCloseTag = "</TableLengthWave>"
    isTableReading = False

    line = xmlPassportFile.readline()
    while(line):
        if(tableOpenTag in line):
            isTableReading = True
            line = xmlPassportFile.readline()
            continue
        elif(tableCloseTag in line):
            break

        if(isTableReading):
            readWaveLengthBlockInDict(xmlPassportFile, channelWavesLength)

        line = xmlPassportFile.readline()
    xmlPassportFile.close()

    return channelWavesLength

def readWaveLengthBlockInDict(xmlOpenedFile, destinationDict):
    blockCloseTag = "</WaveLength>"

    line = xmlOpenedFile.readline()
    while(line):
        if(blockCloseTag in line):
            destinationDict[waveLength] = channelNumber
            break
        
        if("<ChannelNumber>" in line):
            channelNumber = int(readTagValue(line, "<ChannelNumber>"))
        elif("<WaveLen>" in line):
            waveLength = float(readTagValue(line, "<WaveLen>"))

        line = xmlOpenedFile.readline()

def readTagValue(lineWithTag, tag):
    closeTag = tag.replace("<", "</")

    tagValue = lineWithTag.replace(tag, "")
    tagValue = tagValue.replace(closeTag, "")

    return tagValue.strip()