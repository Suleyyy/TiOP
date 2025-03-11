import cv2

image = cv2.imread('img/img1.jpg')
(h,w) = image.shape[:2]
x = int(input('Podaj współrzędną x: '))
y = int(input('Podaj współrzędną y: '))
if x > h or x < 0 or y > w or y < 0:
    raise ValueError
else:
    image[x,y] = (0,0,0)
    cv2.imshow('image', image)
    cv2.waitKey(0)

