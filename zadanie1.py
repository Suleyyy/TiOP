import cv2

image = cv2.imread('img/img1.jpg')
(b,g,r) = image[0,0]
print(b,g,r)