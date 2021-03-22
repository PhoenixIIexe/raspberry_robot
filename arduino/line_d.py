import sys
import numpy as np
import cv2 as cv


hsv_min = np.array((0, 0, 100), np.uint8)
hsv_max = np.array((255, 255, 255), np.uint8)

sensor_d = {
    'line': 0,
    'cr': 0
}

def sensor():
    img = cv.warpAffine(cv.VideoCapture(0).read()[1], cv.getRotationMatrix2D((320, 240), 180, 1.0), (640, 480))
    img = img[360: 480, 120: 520]

    sensor_d['cr'] = 101
    normal_y, distortions_y, distortions_r, distortions_l = [1000, 0, 0, 0]

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    thresh = cv.inRange(hsv, hsv_min, hsv_max)

    contours, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if contours != []:
        contours = ' '.join(''.join(''.join(''.join(list(map(str, contours[1][4:-3]))).split('[['))).split(']]')).split(' ')
        contours = list(map(int, list(filter(None, contours))[::2]))
        
        if sum(contours)//len(contours) < 200:
            sensor_d['line'] = -1
        elif sum(contours)//len(contours) > 200:
            sensor_d['line'] = 1
        else:
            if sum(contours)//len(contours) - 200 < -20:
                sensor_d['line'] = -1
            elif sum(contours)//len(contours) - 200 > 20:
                sensor_d['line'] = 1
            else:
                sensor_d['line'] = 0

        if abs(min(contours) - sum(contours)//len(contours)) > 20 and abs(max(contours) - sum(contours)//len(contours)) < 100:
            sensor_d['cr'] = -1
        elif abs(min(contours) - sum(contours)//len(contours)) < 100 and abs(max(contours) - sum(contours)//len(contours)) > 20:
            sensor_d['cr'] = 1
        elif abs(min(contours) - sum(contours)//len(contours)) > 100 and abs(max(contours) - sum(contours)//len(contours)) > 100:
            sensor_d['cr'] = 0
        
    print(sensor_d)
    return sensor_d