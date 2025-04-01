import cv2

img = cv2.imread('img/obraz.jfif')
roi = img[100:200, 200:300]
img[:100,:100] = roi
cv2.imshow('obraz', img)
cv2.moveWindow('obraz', 100, 100)
cv2.waitKey(0)