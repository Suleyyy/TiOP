import cv2
import imutils

img = cv2.imread('img/obraz.jpg')
rotated = imutils.rotate(img,30)
rotated2 = imutils.rotate(rotated,30)
rotated3 = imutils.rotate(rotated2,30)
cv2.imshow('obraz',rotated3)
rotated_once = imutils.rotate(img,90)
cv2.imshow('obraz2',rotated_once)
cv2.waitKey(0)