import cv2

image = cv2.imread('images/image.jpg')
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 400, 600)
cv2.imshow('image', image)
cv2.waitKey(0)