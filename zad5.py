import cv2

image = cv2.imread('img/obraz.jpg')
mid = (image.shape[0]//2, image.shape[1]//2)
frag = image[mid[0]-100:mid[0]+100, mid[1]-100:mid[1]+100]
flipped_image = cv2.flip(frag, -1)
image[mid[0]-100:mid[0]+100, mid[1]-100:mid[1]+100] = flipped_image
cv2.imshow('flipped_image', image)

cv2.waitKey(0)