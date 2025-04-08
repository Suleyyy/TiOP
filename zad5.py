import cv2
import numpy as np

img = cv2.imread("img/auto.jpg")

mask = np.zeros(img.shape[:2], np.uint8)
cv2.rectangle(mask, (90, 180), (460, 470), 255, -1)
masked_img = cv2.bitwise_and(img, img, mask=mask)
(B, G, R) = cv2.split(img)
R = cv2.add(B, 50)
merge = cv2.merge((B, G, R))
new = cv2.bitwise_and(img,merge, mask=mask)
cv2.imshow("img", new)
cv2.waitKey(0)