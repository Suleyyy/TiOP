import cv2

image = cv2.imread('images/image.jpg')
#image = cv2.imread('images/zlasciezka.jpg')
cv2.imshow('image', image)
cv2.waitKey(0)