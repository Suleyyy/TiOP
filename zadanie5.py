import cv2
import imutils

img = cv2.imread('img/obraz.jpg')
rotated = imutils.rotate(img, 180)
cv2.imshow('obraz', rotated)
cv2.waitKey(0)