from msvcrt import getch
from os import listdir
import cv2

key, k = 0, int(listdir()[-3][4:-4] if listdir().count('cam_0.png') == 1 else -1)+1
cap = cv2.VideoCapture(0)
clovo = ''

while key != 27:
    key = ord(getch())
    if key == 13:
        for i in range(30):
            cap.read()

        ret, frame = cap.read()

        cv2.imwrite(f'cam_{k}.png', frame)

        k += 1


        print(clovo)
        clovo = ''
    elif key == 96:
        clovo += chr(key)


cap.release()