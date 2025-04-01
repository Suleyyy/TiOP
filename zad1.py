import cv2

img = cv2.imread('img/obraz.jfif')
roi = img[:99,:99]
cv2.imshow('obraz', roi)
cv2.moveWindow('obraz', 100, 100)
cv2.waitKey(0)