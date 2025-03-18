import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), np.uint8)
cv2.rectangle(canvas, (150, 150), (250, 250), (0, 0, 255), 2)
cv2.circle(canvas, (400//2, 400//2), 30, (0,0,255),2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)