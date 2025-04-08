import cv2
import numpy as np

img = cv2.imread("img/auto.jpg")

mask = np.zeros(img.shape[:2], np.uint8)
cv2.rectangle(mask, (90, 180), (460, 470), 255, -1)

(B, G, R) = cv2.split(img)
R = np.where(mask == 255, np.clip(R + 50, 0, 255), R)
merged = cv2.merge((B, G, R))

cv2.imshow("img", merged)
cv2.waitKey(0)