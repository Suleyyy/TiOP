import cv2
import numpy as np

img = cv2.imread("img/obraz.jfif")
mask = np.zeros(img.shape[:2], np.uint8)
cv2.rectangle(mask, (200,40), (290,120), 255,-1)

masked = cv2.bitwise_or(img, img, mask=mask)

cv2.imshow("masked", masked)
cv2.waitKey(0)