import cv2

image = cv2.imread('img/img1.jpg')
(h,w) = image.shape[:2]
image[h//2-50:h//2+50,w//2-50:w//2+50] = (0,0,255)
cv2.imshow('image', image)
cv2.waitKey(0)