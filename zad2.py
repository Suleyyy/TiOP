import cv2

image = cv2.imread('img/obraz.jpg')

flipped_image = cv2.flip(image, 0)
cv2.imshow('flipped_image', flipped_image)
cv2.waitKey(0)