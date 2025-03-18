import cv2
import numpy as np

img = cv2.imread('img/twarz.jpeg')
img = cv2.resize(img, (400, 400))
cv2.circle(img, (150, 180), 30, (0,0,255),-1)
cv2.circle(img, (250, 180), 30, (0,0,255),-1)
cv2.rectangle(img, (130, 280), (260, 320), (0,255,0),-1)
cv2.circle(img, (200, 200), 155, (255,0,0),2)
cv2.imshow('twarz', img)
cv2.waitKey(0)