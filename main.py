from tifFileHandler import saveTifAsMat, readHSIChannelFromMat
from xmlPassportParser import readTableLengthWave

hsiPath = "./0041_0306_34728_1_04894_06_L1A.tif"
matSavePath = "./hsi.mat"

passportFilePath = "./0041_0306_34728_1_04894_06_L1A.xml"
table = readTableLengthWave(passportFilePath)

print(table)