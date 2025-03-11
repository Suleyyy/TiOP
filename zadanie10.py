import cv2

image = cv2.imread('img/img1.jpg')
(b,g,r) = image[50,50]
(b2,g2,r2) = image[200,200]
print(f'Różnica blue: {abs(b2-b)} ')
print(f'Różnica green: {abs(g2-g)} ')
print(f'Różnica red: {abs(r2-r)} ')
