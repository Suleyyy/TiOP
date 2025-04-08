import cv2

img = cv2.imread("img/img2.jpg")

(B, G, R) = cv2.split(img)

cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.waitKey(0)