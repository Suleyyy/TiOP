import cv2

img = cv2.imread('img/obraz.jfif')
h,w = img.shape[0]//2, img.shape[1]//2
roi = img[:, h:]
cv2.imshow('obraz', roi)
cv2.moveWindow('obraz', 100, 100)
cv2.waitKey(0)