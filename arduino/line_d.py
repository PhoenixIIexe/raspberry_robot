import sys
import numpy as np
import cv2 as cv
from time import sleep, time


hsv_min = np.array((0, 0, 100), np.uint8)
hsv_max = np.array((255, 255, 255), np.uint8)

list_y = []
distortions = [180, 220]
normal = [180, 220]
sensor_d = {
    'line': 0,
    'cr': 0
}
k = 0
def sensor():
    img = cv.warpAffine(cv.VideoCapture(0).read()[1], cv.getRotationMatrix2D((320, 240), 180, 1.0), (640, 480))
    img = img[360: 480, 120: 520]
    
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    thresh = cv.inRange(hsv, hsv_min, hsv_max)
    
    contours, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #print(contours[1])
    for i in contours[1][5:-5]:
        x = i[0][0]
        if abs(200 - x) < 30 and normal.count(x) == 0:
            normal.append(x)
        else:
            distortions.append(x)
        
        list_y.append(i[0][1])
    try:
        if abs(max(normal) - max(distortions)) < 20 and abs(min(normal) - min(distortions)) < 20:
            #print('Линия')
            if max(normal) < 200:
                sensor_d['line'] = -1
            elif min(normal) > 200:
                sensor_d['line'] = 1
            else:
                if (max(normal)+min(normal))/2 - 200 < -5:
                    sensor_d['line'] = -1
                elif (max(normal)+min(normal))/2 - 200 > 5:
                    sensor_d['line'] = 1
                else:
                    sensor_d['line'] = 0
                    
        elif abs(max(normal) - max(distortions)) > 20 and abs(min(normal) - min(distortions)) < 20:
            if abs(list_y[distortions.index(max(distortions)) + len(normal)] - list_y[normal.index(max(normal)) + len(distortions)]) > 20:
                #print('Изгиб вправо')
                sensor_d['cr'] = 2
            else:
                #print('Г-образный изгиб вправо')
                sensor_d['cr'] = 1
        elif abs(max(normal) - max(distortions)) < 20 and abs(min(normal) - min(distortions)) > 20:
            if abs(list_y[distortions.index(max(distortions)) + len(normal)] - list_y[normal.index(max(normal)) + len(distortions)]) > 20:
                #print('Изгиб влево')
                sensor_d['cr'] = -2
            else:
                #print('Г-образный изгиб влево')
                sensor_d['cr'] = -1
        elif abs(max(normal) - max(distortions)) > 20 and abs(min(normal) - min(distortions)) > 20:
            #print('Перекресток')
            sensor_d['cr'] = 0
    except:
        if max(normal) < 200:
            sensor_d['line'] = -1
        elif min(normal) > 200:
            sensor_d['line'] = 1
        else:
            if (max(normal)+min(normal))/2 - 200 < -5:
                sensor_d['line'] = -1
            elif (max(normal)+min(normal))/2 - 200 > 5:
                sensor_d['line'] = 1
            else:
                sensor_d['line'] = 0
        
    return sensor_d

    """
    cv.drawContours( img, contours, -1, (0, 255, 255), 3, cv.LINE_AA, hierarchy, 2)
    cv.imshow('contours', img)

    cv.waitKey()
    cv.destroyAllWindows()
    """
