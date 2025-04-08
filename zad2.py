import cv2
import numpy as np

img = cv2.imread("img/obraz.jfif")
mask = np.zeros(img.shape[:2], np.uint8)
cv2.rectangle(mask, (210,65), (270,80), 255, -1)
img[mask == 255] = (0,0,0)

cv2.imshow("masked", img)
cv2.waitKey(0)