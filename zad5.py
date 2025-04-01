import cv2

img = cv2.imread('img/obraz2.jfif')
roi = img[110:250, 200:320]
cv2.imshow('obraz', roi)
cv2.moveWindow('obraz', 100, 100)
cv2.waitKey(0)