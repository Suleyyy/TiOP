import cv2

img = cv2.imread('img/noise.jpg')
cv2.imshow('img', img)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for i, (diameter, sigmaColor, sigmaSpace) in enumerate(params):
    blurred = cv2.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)
    cv2.imshow(f'bblurred{i}', blurred)

ksize = [(3,3),(5,5),(7,7)]

for i, (kX, kY) in enumerate(ksize):

    blur = cv2.blur(img, (kX, kY))
    cv2.imshow(f'blurred{i}', blur)
    mblur = cv2.medianBlur(img, kX)
    cv2.imshow(f'mblur{i}', mblur)
    gblur = cv2.GaussianBlur(img, (kX, kY), 0)
    cv2.imshow(f'gblur{i}', gblur)

cv2.waitKey(0)

#1.Tak
#2.Tak
#3.Im wyższy parametr SigmaColor tym większe rozmycie, zmieniając inne parametry nie widziałem różnicy, prócz tego że wysoki diameter zwiesza okno na chwile