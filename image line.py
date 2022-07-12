import cv2
import numpy as np
# from object_detector import *

FILE_NAME = 'gambar/4.jpg'
try:
    # Read image from disk.
    img = cv2.imread(FILE_NAME)

    # Canny edge detection.
    edges = cv2.Canny(img, 100, 200)

    # Write image back to disk.
    cv2.imwrite('result.jpg', edges)
except IOError:
    print('Error while reading files !!!')
