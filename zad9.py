import cv2

img = cv2.imread('img/obraz.jfif')
roi = img[:299, :299]
cv2.imwrite('img/cropped_image.jpg', roi)
