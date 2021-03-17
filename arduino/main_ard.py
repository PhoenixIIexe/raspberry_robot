import RPi.GPIO as GPIO
from time import sleep, time
from line_d_v2 import sensor
import cv2

GPIO.setmode(GPIO.BCM)
#---------------------------------------------------------------------#
pin1_d = 18
pin1_sp = 17
pin2_d = 22

pin2_sp = 27

GPIO.setup(pin1_d, GPIO.OUT)
GPIO.setup(pin2_d, GPIO.OUT)
GPIO.setup(pin1_sp, GPIO.OUT)
GPIO.setup(pin2_sp, GPIO.OUT)

motor1 = GPIO.PWM(pin1_sp, 100)
motor2 = GPIO.PWM(pin2_sp, 100)
#---------------------------------------------------------------------#
def go(m1, m2):
    GPIO.output(pin1_d, GPIO.HIGH if m1 >= 0 else GPIO.LOW)
    GPIO.output(pin2_d, GPIO.HIGH if m2 >= 0 else GPIO.LOW)
    motor1.start(m1 if m1 <= 100 else 100)
    motor2.start(m2 if m2 <= 100 else 100)

#---------------------------------------------------------------------#
def line(m1, m2):
    if sensor()['line'] == 0:
        go(m1, m2)
    elif sensor()['line'] == -1:
        go(0.5*m1, m2)
    elif sensor()['line'] == 1:
        go(m1, 0.5*m2)
#---------------------------------------------------------------------#

temp = round(time())
while round(time()) - temp < 20:
    line(50, 50)


motor1.stop()
motor2.stop()
GPIO.cleanup()
