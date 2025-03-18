import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), np.uint8)
mid = 512//2
cv2.line(canvas, (mid, mid), (512, 512), (255, 0, 0), 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)