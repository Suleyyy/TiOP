import cv2

image = cv2.imread('img/img1.jpg')
(h,w) = image.shape[:2]
h2 = h//9
w2 = w//9
tl = image[4*h2:5*h2, 4*w2:5*w2]
cv2.imshow('image', tl)
cv2.waitKey(0)