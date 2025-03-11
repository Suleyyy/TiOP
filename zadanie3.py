import cv2

image = cv2.imread('img/img1.jpg')
(h,w) = image.shape[:2]
h2 = h//2
w2 = w//2
(b,g,r) = image[h2, w2]
print(b,g,r)