from tifFileHandler import saveTifAsMat, readHSIChannelFromMat
from matplotlib import pyplot as plt

sourcePath = "./0041_0306_34728_1_04894_06_L1A.tif"
savePath = "./hsi.mat"

saveTifAsMat(sourcePath, savePath)
hsiChannel = readHSIChannelFromMat(savePath, 120)

plt.imshow(hsiChannel)
plt.show()