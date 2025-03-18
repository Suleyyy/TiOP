import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), np.uint8)
cv2.circle(canvas, (50, 50), 40, (255,0,0),2)
cv2.circle(canvas, (300//2, 300//2), 60, (0,0,255),2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)