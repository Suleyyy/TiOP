import cv2

image = cv2.imread('img/obraz.jpg')
resized = cv2.resize(image, (image.shape[0]//2, image.shape[1]//2), interpolation=cv2.INTER_AREA)

cv2.imshow('obraz', resized)
cv2.waitKey(0)