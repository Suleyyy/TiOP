import cv2
import numpy as np

triangle = np.zeros((300,300), dtype="uint8")
triangle_cnt = np.array([(0,300),(150,0),(300,300)])
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.drawContours(triangle, [triangle_cnt], 0, 255, -1)
bit_or = cv2.bitwise_or(triangle, circle)
bit_and = cv2.bitwise_and(triangle, circle)
bit_xor = cv2.bitwise_xor(triangle, circle)
bit_not = cv2.bitwise_not(triangle)
bit_not2 = cv2.bitwise_not(circle)
cv2.imshow("or", bit_or)
cv2.imshow("and", bit_and)
cv2.imshow("xor", bit_xor)
cv2.imshow("not", bit_not)
cv2.imshow("not2", bit_not2)
cv2.waitKey(0)