import numpy as np

def createMaskFromNDVI(ndvi: np.ndarray) -> np.ndarray:
    height = ndvi.shape[0]
    width = ndvi.shape[1]

    mask = np.zeros((height, width, 4), dtype = np.uint8)

    for y in range(height):
        for x in range(width):
            if(0.2 <= ndvi[y][x] < 0.4):
                mask[y][x] = [255, 0, 0, 200]
            else:
                mask[y][x] = [0, 0, 0, 0]
    return mask