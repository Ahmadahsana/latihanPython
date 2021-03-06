from turtle import width
from unittest import result
from matplotlib.pyplot import hsv
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBlue = np.array([90, 50, 50])  # B G R
    upperBlue = np.array([130, 255, 255])  # R G B

    mask = cv2.inRange(hsv, lowerBlue, upperBlue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
