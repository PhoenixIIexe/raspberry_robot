import cv2
from RGB_in_HSV import hsv
image = cv2.imread('code_2.png')
code = list()

pixel = image[2, 2][::-1]
print(hsv(pixel))
start_R, start_G, start_B = pixel[0], pixel[1], pixel[2]
r_RGB = 30

i, g = 0, 0

while True:
    pixel = image[i, g][::-1]
    if not (0.9 <= hsv(pixel)[2] <= 1):
        break
    i += 1
    g += 1

x, y = i, g
while True:
    pixel = image[x, g][::-1]
    if 0.9 <= hsv(pixel)[2] <= 1:
        break
    x += 1
    

while True:
    pixel = image[i, y][::-1]
    if 0.9 <= hsv(pixel)[2] <= 1:
        break
    y += 1

'-------------------------------------------------------------------------------------'

x_s, y_s = x, y
while True:
    pixel = image[x_s, g][::-1]
    if not(0.9 <= hsv(pixel)[2] <= 1):
        break
    x_s += 1
    

while True:
    pixel = image[i, y_s][::-1]
    if not(0.9 <= hsv(pixel)[2] <= 1):
        break
    y_s += 1

'-------------------------------------------------------------------------------------'

x, y = int(0.5*x), int(0.5*y)
y_s += 50
print(x, y, x_s, y_s)

for i in range(3):
    for g in range(3):
        pixel = image[x +  (x_s+60)*i, y + y_s*g][::-1]
        print(pixel[0], pixel[1], pixel[2], end=' ')
        if 0.4 <= hsv(pixel)[2] <= 0.6:
            print('gray', end='')
            #print('\t', hsv(pixel), end='\t')
            continue
        if 30 <= hsv(pixel)[0] < 90:
            print('yellow ', end='')
            #print('\t', hsv(pixel), end='\t')
            continue
    print('\n')
