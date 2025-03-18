import cv2
import imutils

img = cv2.imread('img/obraz.jpg')
shifted = imutils.translate(img,100,50)
cv2.imshow('shifted', shifted)
cv2.waitKey(0)
# nie zauważyłem różnicy