import cv2

img = cv2.imread('img/obraz.jpg')
(h,w) = img.shape[:2]
M = cv2.getRotationMatrix2D((0,0),30,1)
rotated = cv2.warpAffine(img,M,(w,h))
cv2.imshow('obraz', rotated)
cv2.waitKey(0)