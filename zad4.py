import cv2

image = cv2.imread('images/image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('images/image_gray.jpg', image)