import cv2
import imutils

img = cv2.imread('img/obraz.jpg')
rotated = imutils.rotate(img,75)
cv2.imwrite('img/rotated_output.jpg',rotated)