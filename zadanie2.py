import cv2

image = cv2.imread('img/img1.jpg')
(h, w) = image.shape[:2]
print(h,w)
cv2.imshow('image', image)
image[h-1, w-1] = (0, 0, 255)
cv2.imshow('image2', image)
cv2.waitKey(0)
