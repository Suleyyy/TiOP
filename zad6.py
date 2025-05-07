import cv2

img = cv2.imread('img/obraz6.jpg', cv2.COLOR_BGR2GRAY)

closing = cv2.morphologyEx(img, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (2,2)), iterations=1)


cv2.imshow('closing', closing)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()