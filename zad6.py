import cv2

flip = int(input('Podaj sposób odbicia (0,1,-1): '))
image = cv2.imread('img/obraz.jpg')

flipped_image = cv2.flip(image, flip)
cv2.imshow('flipped_image', flipped_image)
cv2.waitKey(0)