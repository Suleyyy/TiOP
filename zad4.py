import cv2

img = cv2.imread('img/obraz4.jpg', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
closing2 = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel2)
cv2.imshow('closing', closing)
cv2.imshow('img', img)
cv2.imshow('closing2', closing2)
cv2.waitKey(0)