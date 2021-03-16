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


img = cv.warpAffine(cv.VideoCapture(0).read()[1], cv.getRotationMatrix2D((320, 240), 180, 1.0), (640, 480))[360: 480, 120: 520]
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
thresh = cv.inRange(hsv, hsv_min, hsv_max)

contours, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
m_line = contours[1][7][0][0]
print(m_line)
white_d = True


def sensor():
    local white_d
    distortions = []
    normal = []
    normal_y, distortions_y = 0, 0
    sensor_d['cr'] = 101


    img = cv.warpAffine(cv.VideoCapture(0).read()[1], cv.getRotationMatrix2D((320, 240), 180, 1.0), (640, 480))
    img = img[360: 480, 120: 520]

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    thresh = cv.inRange(hsv, hsv_min, hsv_max)
    
    contours, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    try:
      for i in contours[1]:
          x = i[0][0]
          if abs(m_line - x) < 100 :
              if distortions != [] and normal.count(x) == 1:
                  distortions.append(x)
                  distortions_y = i[0][1]
              else:
                  normal.append(x)
                  normal_y = i[0][1]
          else:
              distortions.append(x)
              distortions_y = i[0][1]
      print(normal, distortions)
      try:         
          if abs(max(normal) - max(distortions)) > 20 and abs(min(normal) - min(distortions)) < 20:
              if abs(distortions_y - normal_y) > 20:
                  sensor_d['cr'] = 2
              else:
                  sensor_d['cr'] = 1
          elif abs(max(normal) - max(distortions)) < 20 and abs(min(normal) - min(distortions)) > 20:
              if abs(distortions_y - normal_y) > 20:
                  sensor_d['cr'] = -2
              else:
                  sensor_d['cr'] = -1
          elif abs(max(normal) - max(distortions)) > 20 and abs(min(normal) - min(distortions)) > 20:
              sensor_d['cr'] = 0
      except:
          pass
      finally:
          sensor = normal if normal != [] else distortions
          if max(sensor) < m_line:
              sensor_d['line'] = -1
          elif min(sensor) > m_line:
              sensor_d['line'] = 1
          else:
              if (max(sensor)+min(sensor))/2 - m_line < -20:
                  sensor_d['line'] = -1
              elif (max(sensor)+min(sensor))/2 - m_line > 20:
                  sensor_d['line'] = 1
              else:
                  sensor_d['line'] = 0
      white_d = True
    except:
      if white_d:
        if sensor_d['line'] == 1:
          sensor_d['line'] = -1
        else:
          sensor_d['line'] = 1
        white_d = False

    print(sensor_d)
    return sensor_d