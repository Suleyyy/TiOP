import cv2

img = cv2.imread("img/img2.jpg")

(B, G, R) = cv2.split(img)
new_img = cv2.merge([R, G, B])
cv2.imshow("original", img)
cv2.imshow("new_img", new_img)
cv2.waitKey(0)