import cv2

image = cv2.imread('images/image.jpg')
(h,w,c) = image.shape
print(f'channels {c}')