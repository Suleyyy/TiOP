import cv2

image = cv2.imread('images/image.jpg', cv2.IMREAD_GRAYSCALE)
print(f'channels {image.shape}')