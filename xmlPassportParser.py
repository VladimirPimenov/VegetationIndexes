def readTableLengthWave(passportFilePath: str) -> dict:
    table = dict()
    tableOpenTag = "<TableLengthWave>"
    tableCloseTag = tableOpenTag.replace("<", "</")

    xmlPassportFile = open(passportFilePath, "r")
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
            readWaveLengthBlockToDict(xmlPassportFile, table)

        line = xmlPassportFile.readline()
    xmlPassportFile.close()

    return table

def readWaveLengthBlockToDict(xmlOpenedFile, destinationDict):
    blockOpenTag = "<WaveLength>"
    blockCloseTag = blockOpenTag.replace("<", "</")

    blockKey = "<WaveLen>"

    block = dict()

    line = xmlOpenedFile.readline()
    while(line):
        if(blockOpenTag in line):
            continue
        elif(blockCloseTag in line):
            break
        
        lineTag = readTag(line)

        if(lineTag == blockKey):
            waveLen = readTagValue(line, lineTag)
        else:
            tagValue = readTagValue(line, lineTag)
            block[lineTag] = tagValue

        line = xmlOpenedFile.readline()

    destinationDict[waveLen] = block

def readTag(line):
    tag = ""
    isTagReading = False

    for symb in line:
        if(symb == '<'):
            isTagReading = True
        elif(symb == '>'):
            tag += symb
            break

        if(isTagReading):
            tag += symb

    return tag

def readTagValue(lineWithTag, tag):
    closeTag = tag.replace("<", "</")

    tagValue = lineWithTag.replace(tag, "")
    tagValue = tagValue.replace(closeTag, "")

    return tagValue.strip()