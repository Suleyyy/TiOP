import cv2
import numpy as np

img = cv2.imread('img/typo.png')
cv2.imshow('typo', img)

mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.circle(mask, (740, 150),85, 255, -1)
cv2.rectangle(mask, (680, 200), (805, 526), 255,-1)
cv2.rectangle(mask, (550, 300), (930, 526), 255,-1)
blurred = cv2.GaussianBlur(img, (9, 9), 0)
foreground = cv2.bitwise_and(img, img, mask=mask)
background_mask = cv2.bitwise_not(mask)
background = cv2.bitwise_and(blurred, blurred, mask=background_mask)
result = cv2.add(foreground, background)
cv2.imshow('result', result)


cv2.waitKey(0)
