import cv2

image = cv2.imread('img/obraz.jpg')
cv2.imshow('obraz', image)
eroded = cv2.erode(image, None, (3,3))
eroded_rect = cv2.erode(image, cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)))
eroded_elip = cv2.erode(image, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)))
cv2.imshow('eroded', eroded)
cv2.imshow('eroded_rect', eroded_rect)
cv2.imshow('eroded_elip', eroded_elip)
cv2.waitKey(0)