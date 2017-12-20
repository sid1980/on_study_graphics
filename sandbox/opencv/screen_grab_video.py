#coding: utf-8

import numpy as np
import cv2
from PIL import ImageGrab
width = 1280
height = 720


fourcc = cv2.VideoWriter_fourcc('X','V','I','D') #you can use other codecs as well.
vid = cv2.VideoWriter('record.avi', fourcc, 20, (width, height))

cap = cv2.VideoCapture(0)

while(True):
    img = ImageGrab.grab() #x, y, w, h
    # img = ImageGrab.grab(bbox=(100, 10, 600, 500)) #x, y, w, h
    # res = cv2.resize(img, None, fx=img.height/height,fy=img.width/width, interpolation=cv2.INTER_CUBIC)
    # print((int)(img.height/height), (int)(img.width/width))
    res = cv2.resize(np.array(img), (width, height), interpolation=cv2.INTER_CUBIC)
    img_np = np.array(res)

    # prepare capture frame
    ret, frame = cap.read()
    rows, cols, channels = frame.shape
    roi = img_np[0:rows, 0:cols]
    # cv2.addWeighted(img_np, 0.5, frame, 0.5, 0)

    # merge two image
    img_np[0:rows, 0:cols] = frame

    # save on disk
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    vid.write(img_np)

    cv2.imshow("frame", img_np)
    key = cv2.waitKey(41)
    if key == 27:
        break

vid.release()
cv2.destroyAllWindows()
