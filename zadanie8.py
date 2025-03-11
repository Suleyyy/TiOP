import cv2

image = cv2.imread('img/img1.jpg')
image[99,] = (0,255,0)
cv2.imshow('image', image)
cv2.waitKey(0)