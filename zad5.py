import cv2
import imutils

image = cv2.imread('img/obraz.jpg')
resized = imutils.resize(image, width=500)

cv2.imshow('obraz', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()