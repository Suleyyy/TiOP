import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 300, 20):
    cv2.rectangle(canvas,(300//2-r//2,300//2-r//2), (300//2+r//2,300//2+r//2), (255,0,0), 2)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)