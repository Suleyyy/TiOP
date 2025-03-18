import cv2
import imutils

img = cv2.imread('img/obraz.jpg')

for x in range(0,360,15):
    rotated = imutils.rotate(img,x)
    cv2.imshow('rotated',rotated)
    cv2.waitKey(500)