import numpy as np

def convertNDVItoRGB(NDVIimage):
    RGBimage = np.zeros((NDVIimage.shape[0], NDVIimage.shape[1], 3), dtype = np.uint8)

    height = NDVIimage.shape[0]
    width = NDVIimage.shape[1]

    for y in range(height):
        for x in range(width):
            RGBimage[y][x] = getRGBcolorFromNDVI(NDVIimage[y][x])
    return RGBimage

def getRGBcolorFromNDVI(ndvi):
    if(-1 <= ndvi < -0.9):
        rgb = [0, 0, 14]
    elif(-0.9 <= ndvi < -0.8):
        rgb = [0, 0, 43]
    elif(-0.8 <= ndvi < -0.7):
        rgb = [0, 0, 68]
    elif(-0.7 <= ndvi < -0.6):
        rgb = [0, 0, 93]
    elif(-0.6 <= ndvi < -0.5):
        rgb = [0, 0, 121]
    elif(-0.5 <= ndvi < -0.4):
        rgb = [0, 0, 148]
    elif(-0.4 <= ndvi < -0.3):
        rgb = [0, 0, 173]
    elif(-0.3 <= ndvi < -0.2):
        rgb = [0, 0, 199]
    elif(-0.2 <= ndvi < -0.1):
        rgb = [0, 0, 255]
    elif(-0.1 <= ndvi < 0.0):
        rgb = [221, 221, 231]
    elif(0.0 <= ndvi < 0.1):
         rgb = [175, 143, 101]
    elif(0.1 <= ndvi < 0.2):
         rgb = [150, 110, 159]
    elif(0.2 <= ndvi < 0.3):
         rgb = [166, 132, 35]
    elif(0.3 <= ndvi < 0.4):
         rgb = [182, 175, 10]
    elif(0.4 <= ndvi < 0.5):
         rgb = [136, 190, 0]
    elif(0.5 <= ndvi < 0.6):
        rgb = [49, 190, 0]
    elif(0.6 <= ndvi < 0.7):
        rgb = [0, 176, 0]
    elif(0.7 <= ndvi < 0.8):
         rgb = [0, 148, 0]
    elif(0.8 <= ndvi < 0.9):
        rgb = [0, 121, 0]
    elif(0.9 <= ndvi <= 1.0):
        rgb = [0, 88, 0]
    return rgb