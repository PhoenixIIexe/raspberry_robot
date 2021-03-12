import cv2
image = cv2.imread('code_2.png')
code = list()

pixel = image[5, 5][::-1]
start_R, start_G, start_B = pixel[0], pixel[1], pixel[2]
r_RGB = 30

i, g = 0, 0

while True:
    pixel = image[i, g][::-1]
    if not (start_R - r_RGB <= pixel[0] <= start_R + r_RGB and start_G - r_RGB <= pixel[1] <= start_G + r_RGB and start_B - r_RGB <= pixel[2] <= start_B + r_RGB):
        break
    i += 1
    g += 1

x, y = i, g
while True:
    pixel = image[x, g][::-1]
    if start_R - r_RGB <= pixel[0] <= start_R + r_RGB and start_G - r_RGB <= pixel[1] <= start_G + r_RGB and start_B - r_RGB <= pixel[2] <= start_B + r_RGB:
        break
    x += 1
    

while True:
    pixel = image[i, y][::-1]
    if start_R - r_RGB <= pixel[0] <= start_R + r_RGB and start_G - r_RGB <= pixel[1] <= start_G + r_RGB and start_B - r_RGB <= pixel[2] <= start_B + r_RGB:
        break
    y += 1

'-------------------------------------------------------------------------------------'

x_s, y_s = x, y
while True:
    pixel = image[x_s, g][::-1]
    if not(start_R - r_RGB <= pixel[0] <= start_R + r_RGB and start_G - r_RGB <= pixel[1] <= start_G + r_RGB and start_B - r_RGB <= pixel[2] <= start_B + r_RGB):
        break
    x_s += 1
    

while True:
    pixel = image[i, y_s][::-1]
    if not(start_R - r_RGB <= pixel[0] <= start_R + r_RGB and start_G - r_RGB <= pixel[1] <= start_G + r_RGB and start_B - r_RGB <= pixel[2] <= start_B + r_RGB):
        break
    y_s += 1

'-------------------------------------------------------------------------------------'

x, y = int(0.5*x), int(0.5*y)
print(x, y, x_s, y_s)

for i in range(3):
    for g in range(3):
        pixel = image[x +  (x_s+60)*i, y + y_s*g][::-1]
        print(pixel[0], pixel[1], pixel[2], end=' ')
        if (190 <= pixel[0] <= 255 or 0 <= pixel[0] <= 40) and (30 <= pixel[1] <= 255 or 0 <= pixel[1] <= 100) and (150 <= pixel[2] <= 255 or 0 <= pixel[2] <= 150):
            print('yellow ', end='')
            continue
        if round(sum(pixel) / 3) - pixel[0] < 30 and round(sum(pixel) / 3) - pixel[1] < 30 and round(sum(pixel) / 3) - pixel[2] < 30:
            print('gray', end='')
            continue
    print('\n')
