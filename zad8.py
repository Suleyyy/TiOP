import cv2

img = cv2.imread('img/obraz.jfif')
h, w = img.shape[0], img.shape[1]

for x in range(10, h, 10):
    roi = img[:, :x]
    cv2.imshow(f'obraz{x}', roi)
    cv2.moveWindow(f'obraz{x}', 100, 100)
    cv2.waitKey(0)
cv2.destroyAllWindows()
