import cv2

img = cv2.imread('img/obraz.jfif')
h,w = img.shape[0], img.shape[1]
for x in range(0,h,h//3):
    i = 1
    for y in range(0,w,w//3):
        roi = img[y:y+w//3, x:x+w//3]
        cv2.imshow(f'obraz{i}', roi)
        cv2.moveWindow(f'obraz{i}', 100+x, 100+y)
        cv2.waitKey(1000)
    i += 1
cv2.destroyAllWindows()