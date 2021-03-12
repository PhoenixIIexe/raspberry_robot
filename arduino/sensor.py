from RGB_in_HSV import hsv
import cv2

img = cv2.imread("ard_1.png")

def sensor():
    height, width = img.shape[:2]
    height *= 0.5
    width *= 0.5
    height = round(height)
    width = round(width)

    sensor_d = {
        'cr': 1,
        'line': 0
    }

    if 0 <= hsv(img[width, height][::-1])[2] <= 0.2:
        if 0 <= hsv(img[width+70, height][::-1])[2] <= 0.2 or 0 <= hsv(img[width-70, height][::-1])[2] <= 0.2:
            sensor_d['cr'] = 0
        else:
            sensor_d['line'] = 0
    elif 0.8 <= hsv(img[width, height][::-1])[2] <= 1:
        for i in range(20):
            if 0 <= hsv(img[width+i, height][::-1])[2] <= 0.2:
                sensor_d['line'] = 1
            elif 0 <= hsv(img[width-i, height][::-1])[2] <= 0.2:
                sensor_d['line'] = -1
    
    return sensor_d

def line(m1, m2):
    if sensor()['line'] == 0:
        go(m1, m2)
    elif sensor()['line'] == 1:
        go(m1, 0.35*m2)
    elif sensor()['line'] == -1:
        go(m1, 0.35*m2)

#-----------------------------------------#
#CrossRoad

if sensor()['cr'] == 0:
    pass
#-----------------------------------------#