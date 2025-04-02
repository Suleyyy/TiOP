import cv2

img = cv2.imread('img/obraz.jpg')
img2 = cv2.imread('img/obraz2.jpg')

diff = cv2.absdiff(img, img2)

print(diff)
