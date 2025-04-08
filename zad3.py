import cv2
import numpy as np

img = cv2.imread('img/obrz2.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,70,50])
upper_red = np.array([10,255,255])
mask = cv2.inRange(hsv, lower_red, upper_red)

result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()