import cv2
import numpy as np

img = cv2.imread('img/obraz.jpg')
added = cv2.subtract(img,80)
added2 = img - np.uint8([80])
cv2.imshow('obraz',added)
cv2.imshow('obraz2',added2)

cv2.waitKey(0)