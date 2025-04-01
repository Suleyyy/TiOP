import cv2
import numpy as np

img = cv2.imread('img/obraz.jpg')
added = cv2.add(img,50)
intensity = np.uint8([50])
added2 = cv2.add(img,intensity)
cv2.imshow('obraz',added)
cv2.imshow('obraz2',added2)

cv2.waitKey(0)