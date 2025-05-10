import cv2
import numpy as np

img = cv2.imread('img/obraz.jpg')

noise = np.zeros_like(img, dtype=np.float32)

cv2.randu(noise, (0,0,0), (40,40,40))

noisy_img = cv2.add(img.astype(np.float32), noise)
noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

cv2.imshow('img', noisy_img)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for i, (diameter, sigmaColor, sigmaSpace) in enumerate(params):
    blurred = cv2.bilateralFilter(noisy_img, diameter, sigmaColor, sigmaSpace)
    cv2.imshow(f'bblurred{i}', blurred)

ksize = [(3,3),(5,5),(7,7)]

for i, (kX, kY) in enumerate(ksize):

    blur = cv2.blur(noisy_img, (kX, kY))
    cv2.imshow(f'blurred{i}', blur)
    mblur = cv2.medianBlur(noisy_img, kX)
    cv2.imshow(f'mblur{i}', mblur)
    gblur = cv2.GaussianBlur(noisy_img, (kX, kY), 0)
    cv2.imshow(f'gblur{i}', gblur)

cv2.waitKey(0)

#1.BilateralFilter