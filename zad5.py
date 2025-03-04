import cv2

image = cv2.imread('images/image.jpg')
image2 = cv2.imread('images/image_gray.jpg')
cv2.imshow('image', image)
cv2.imshow('image2', image2)
cv2.waitKey(0)