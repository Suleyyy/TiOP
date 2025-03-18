import cv2
import imutils

x = int(input('Podaj przesunięcie w poziomie: '))
y = int(input('Podaj przesunięcie w pionie: '))

img = cv2.imread('img/obraz.jpg')
shifted = imutils.translate(img,x,y)
cv2.imshow('shifted', shifted)

cv2.waitKey(0)