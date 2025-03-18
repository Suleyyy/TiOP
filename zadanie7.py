import cv2
import imutils

img = cv2.imread('img/obraz.jpg')
(h,w) = img.shape[:2]
(x,y) = w//2,h//2
M = cv2.getRotationMatrix2D((x,y),60,1)
rotated = cv2.warpAffine(img,M,(w,h))
rotated2 = imutils.rotate(img, 60)
cv2.imshow('obraz2',rotated)
cv2.imshow('obraz', rotated2)
cv2.waitKey(0)