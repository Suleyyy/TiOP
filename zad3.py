import cv2

img = cv2.imread('img/obraz3.jpg')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()