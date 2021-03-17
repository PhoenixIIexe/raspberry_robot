import sys
import numpy as np
import cv2 as cv
from time import sleep, time


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

    try:
      default = contours[1][-3][0][0] - contours[1][-4][0][0]
      for i in range(4, len(contours[1])//2):

          if -20 <= contours[1][i][0][0] - contours[1][-(i+1)][0][0] - default <= 20:
              if contours[1][i][0][1] < normal_y:
                  normal_y = contours[1][i][0][1]
              default = abs(contours[1][-(i+1)][0][0] - contours[1][i][0][0])
              if contours[1][i][0][0] < 200:
                  sensor_d['line'] = -1
              elif contours[1][-(i+1)][0][0] > 200:
                  sensor_d['line'] = 1
              else:
                  if contours[1][i][0][0] - 200 < 5:
                      sensor_d['line'] = -1
                  elif 200 - contours[1][-(i+1)][0][0] < 5:
                      sensor_d['line'] = 1
                  else:
                      sensor_d['line'] = 0

          elif contours[1][i][0][0] - contours[1][-(i+1)][0][0]  - default > 20 and distortions_r + distortions_l < 350:
              if abs(contours[1][-(i+1)][0][0] - contours[1][i][0][0]) > distortions_r:
                  distortions_r = abs(contours[1][-(i+1)][0][0] - contours[1][i][0][0])
              distortions_y = contours[1][i][0][1]
              sensor_d['cr'] = 1

          elif contours[1][i][0][0] - contours[1][-(i+1)][0][0] - default < -20 and distortions_r + distortions_l < 350:
              if abs(contours[1][-(i+1)][0][0] - contours[1][i][0][0]) > distortions_l:
                  distortions_l = abs(contours[1][-(i+1)][0][0] - contours[1][i][0][0])
              distortions_y = contours[1][i][0][1]
              sensor_d['cr'] = -1

          elif distortions_r + distortions_l >= 350:
              sensor_d['cr'] = 0
              break


      if sensor_d['cr'] in [-1, 1] and abs(distortions_y - normal_y) > 20:
          sensor_d['cr'] = -2 if sensor_d['cr'] == -1 else 2
    except:
      pass

      
    print(sensor_d)
    return sensor_d