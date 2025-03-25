import cv2

image = cv2.imread('img/obraz.jpg')
cv2.imshow('image', image)

for x in range(1,-2,-1):
    flipped_image = cv2.flip(image, x)
    cv2.imshow(f'flipped_image{x}', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()