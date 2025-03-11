import cv2

image = cv2.imread('img/img1.jpg')
image[50:100, 50:100] = (255,255,255)
cv2.imshow('image', image)
cv2.waitKey(0)