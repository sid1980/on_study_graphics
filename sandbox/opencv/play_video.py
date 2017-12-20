#coding: utf-8

import numpy as np
import cv2

cap = cv2.VideoCapture('v_7.mov')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    fps_msec = int(1000/25.0)
    if cv2.waitKey(fps_msec) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()