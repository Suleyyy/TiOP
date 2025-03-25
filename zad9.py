import cv2
import imutils

image = cv2.imread('img/obraz.jpg')
for x in range(200,400,20):
    resized = imutils.resize(image, height=int(image.shape[0]*(x/100.0)), inter=cv2.INTER_LANCZOS4)
    cv2.imshow(f'obraz', resized)
    cv2.waitKey(500)