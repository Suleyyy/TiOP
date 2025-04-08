import cv2

img = cv2.imread("img/img2.jpg")
(B, G, R) = cv2.split(img)
R = cv2.add(R, 50)
new_img = cv2.merge([B, G, R])
cv2.imshow("img", img)
cv2.imshow("new_img", new_img)
cv2.waitKey(0)