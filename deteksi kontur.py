from multiprocessing.connection import wait


import cv2
import numpy as np

gambar = cv2.imread('gambar/5.jpg')
gambarGray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gambarGray, 127, 255, 0)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])

cv2.drawContours(gambar, contours, -1, (0, 255, 0), 3)
cv2.drawContours(gambarGray, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', gambar)
cv2.imshow('Image GRAY', gambarGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
