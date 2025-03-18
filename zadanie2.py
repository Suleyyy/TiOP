import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), np.uint8)
cv2.rectangle(canvas, (0, 0), (100, 50), (0, 255, 0), 2)
cv2.rectangle(canvas, (300, 300), (400, 400), (0, 0, 255), 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)