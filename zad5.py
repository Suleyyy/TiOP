import cv2

img = cv2.imread('img/obraz5.jpg', cv2.IMREAD_GRAYSCALE)
shapes = [None, cv2.MORPH_RECT, cv2.MORPH_CROSS, cv2.MORPH_ELLIPSE]
name = ['None','Rect','Cross','Ellipse']
for x, shape in enumerate(shapes):
    kernel = cv2.getStructuringElement(shape, (5,5))
    eroded = cv2.erode(img, kernel, iterations=3)
    dilated = cv2.dilate(eroded, kernel, iterations=3)
    opening = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(closing, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow(f'eroded {name[x]}', gradient)
    cv2.imshow('img', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()

#Cross i ellipse doładniejszy przy większym rozmiarze kernela