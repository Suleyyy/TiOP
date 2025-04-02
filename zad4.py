import cv2

img = cv2.imread('img/obraz.jpg')
filter = cv2.add(img, (30,0,10,0))
filter = cv2.subtract(filter, (0,20,0,0))
cv2.imshow('obraz',filter)
cv2.waitKey(0)
cv2.destroyAllWindows()