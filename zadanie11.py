import cv2
index = []
brightness = 0
image = cv2.imread('img/img1.jpg')
(h, w) = image.shape[:2]
for y in range(h):
    for x in range(w):
        (b,g,r) = image[y,x]
        mean = (int(b)+int(g)+int(r))/3.0
        if mean > brightness:
            index.clear()
            brightness = mean
            index.append([y,x])
        elif mean == brightness:
            index.append([y,x])

print(f'jasnosc: {brightness}')
for x in index:
    print(f'index: {x[0]} {x[1]}')
    print(f'wartosci: {image[x[0],x[1]]}')