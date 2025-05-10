import cv2

img = cv2.imread('img/obraz.jpg')
ksize = [(3,3),(5,5),(7,7)]
i = 1

for kX, kY in ksize:
    blur = cv2.blur(img,(kX,kY))
    cv2.imshow(f'blur{i}', blur)
    gblur = cv2.GaussianBlur(img, (kX, kY), 0)
    cv2.imshow(f'gblur{i}', gblur)
    mblur = cv2.medianBlur(img, kX)
    cv2.imshow(f'mblur{i}', mblur)
    i += 1
    cv2.waitKey(0)

params = [(11,21,7),(11,41,21),(11,61,39)]

for (diameter,sigmaColor,SigmaSpace) in params:
    bfilter = cv2.bilateralFilter(img, diameter, sigmaColor, SigmaSpace)
    cv2.imshow(f'bfilter{i}', bfilter)
    i +=1


cv2.waitKey(0)

#1.Najlepiej usuwa szum medianBlur
#2.Najwięcej szczegółów zachowuje bilateralFilter
#3.W zależności jaki efekt checmy osiągnąć, zaleta jednego sposobu będzie wadą u innego


