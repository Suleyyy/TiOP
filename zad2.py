import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/obraz2.jpg', cv2.IMREAD_GRAYSCALE)
lista = []

for x in range(1, 10):
    dilated = cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=x)
    area = cv2.countNonZero(dilated)
    lista.append(area)
    cv2.imshow('dilated', dilated)
    cv2.waitKey(1000)

cv2.destroyAllWindows()

plt.plot(range(1, 10), lista)
plt.xlabel('liczba iteracji')
plt.ylabel('biale piksele')
plt.show()
print(lista)