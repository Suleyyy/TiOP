import cv2
import numpy as np

img = cv2.imread("img/obraz.jpeg")

(B, G, R) = cv2.split(img)
new = cv2.merge([G, R, B])
cv2.imshow("img", img)
cv2.imshow("new", new)
new2 = cv2.merge((B, G, np.zeros_like(B)))
cv2.imshow("new2", new2)
cv2.waitKey(0)