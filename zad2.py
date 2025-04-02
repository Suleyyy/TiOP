import cv2
import numpy as np

img = cv2.imread('img/obraz.jpg')
added = cv2.add(img,150)
added2 = img + np.uint8([150])
cv2.imshow('obraz',added)
cv2.imshow('obraz2',added2)

cv2.waitKey(0)
cv2.destroyAllWindows()