import cv2
import imutils

image = cv2.imread('img/obraz.jpg')
resized = imutils.resize(image, height=800, inter=cv2.INTER_LANCZOS4)
cv2.imwrite('img/resized_output.jpg', resized)