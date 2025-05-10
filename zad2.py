import cv2


img = cv2.imread('img/obraz.jpg')
ksize = [(3,3), (5,5), (9,9), (15,15)]

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

#1.Im większy kernel tym większe rozmycie
#2.Optymalnym rozmairem kernela wydaje się 5x5