import sys
import numpy as np
import cv2 as cv
from time import sleep, time


hsv_min = np.array((0, 0, 100), np.uint8)
hsv_max = np.array((255, 255, 255), np.uint8)

distortions = [1000, 0, 0]
normal = [1000, 0, 0]
k = 0
def main():
    #img = cv.imread(fn)[0+50: cv.imread(fn).shape[1]-50, 0+50: cv.imread(fn).shape[0]-70]
    img = cv.imread('line_3.png')
    # img = cv.VideoCapture(0).read()[1]

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    thresh = cv.inRange(hsv, hsv_min, hsv_max)

    contours, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for i in contours[1][5:-5]:
        x = i[0][0]
        if abs(254 - x) < 65: # 254 130
            if normal[0] > x:
                normal[0] = x
            elif normal[1] < x:
                normal[1] = x
                normal[2] = i[0][1]
        else:
            if distortions[0] > x:
                distortions[0] = x
            elif distortions[1] < x:
                distortions[1] = x
                distortions[2] = i[0][1]

    print(normal, '\n\n', distortions)
    if distortions == [1000, 0, 0]:
        print('Линия')
    elif abs(normal[1] - distortions[1]) > 20 and abs(normal[0] - distortions[0]) < 20:
        if abs(distortions[2] - normal[2]) > 20:
            print('Изгиб вправо')
        else:
            print('Г-образный изгиб вправо')
    elif abs(normal[1] - distortions[1]) < 20 and abs(normal[0] - distortions[0]) > 20:
        if abs(distortions[2] - normal[2]) > 20:
            print('Изгиб влево')
        else:
            print('Г-образный изгиб влево')
    elif abs(normal[1] - distortions[1]) > 20 and abs(normal[0] - distortions[0]) > 20:
        print('Перекресток')

    cv.drawContours( img, contours, -1, (0, 255, 255), 3, cv.LINE_AA, hierarchy, 2)
    cv.imshow('contours', img)

    cv.waitKey()
    cv.destroyAllWindows()

temp = round(time())
while round(time()) - temp < 1:
    main()