import cv2
import matplotlib.pyplot as plt

gambar = cv2.imread('gambar/2.jpg')

# plt.imshow(gambar)


while True:
    cv2.imshow('Hai', gambar)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
