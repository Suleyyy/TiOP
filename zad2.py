import cv2

img1 = cv2.imread("img/obraz.jfif")
img2 = cv2.imread("img/obraz2.jpg")

final = cv2.bitwise_xor(img1, img2)

cv2.imshow("xor", final)
cv2.waitKey(0)