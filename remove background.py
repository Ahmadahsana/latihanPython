from sre_constants import SUCCESS
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

segmentor = SelfiSegmentation()

while True:
    SUCCESS, img = cap.read()
    imgOut = segmentor.removeBG(img, (0, 0, 0))

    cv2.imshow('remove background', imgOut)
    cv2.waitKey(1)
