import cv2

img = cv2.imread("img/img2.jpg")

(B,G,R) = cv2.split(img)

cv2.imshow("obraz", B)
cv2.imshow("obraz1", G)
cv2.imshow("obraz2", R)

cv2.imwrite("img/B.jpg", B)
cv2.imwrite("img/G.jpg", G)
cv2.imwrite("img/R.jpg", R)

cv2.waitKey(0)