import cv2

startX = int(input("Podaj start szerokości: "))
endX = int(input("Podaj start szerokości: "))
startY = int(input("Podaj start szerokości: "))
endY = int(input("Podaj start szerokości: "))
img = cv2.imread('img/obraz.jfif')
roi = img[startY:endY, startX :endX]
cv2.imshow('obraz', roi)
cv2.moveWindow('obraz', 100, 100)
cv2.waitKey(0)