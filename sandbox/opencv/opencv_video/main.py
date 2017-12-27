#coding: utf-8

import numpy as np
import cv2

g_slider_position = 0
g_run = 1
g_dontset = 0
g_cap = cv2.VideoCapture('../v_7.mov')

def on_trackbar_slide(pos):
    global g_dontset
    global g_run
    g_cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
    if not g_dontset:
        g_run = 1
    g_dontset = 0

def get_fps(g_cap):
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
    if int(major_ver) < 3:
        fps = g_cap.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = g_cap.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    return fps

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.moveWindow('image', 60, 24)

frames = int(g_cap.get(cv2.CAP_PROP_FRAME_COUNT))
tmpw = int(g_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
tmph = int(g_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("frames: {}, width: {}, height: {}".format(frames, tmpw, tmph))

cv2.createTrackbar('Position', 'image', g_slider_position, frames, on_trackbar_slide)


fps = get_fps(g_cap)
current_pos = 0
while g_cap.isOpened():
    if g_run != 0:
        ret, frame = g_cap.read()

        current_pos = int(g_cap.get(cv2.CAP_PROP_POS_FRAMES))
        g_dontset = 1
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.setTrackbarPos('Position', 'image', current_pos)
        cv2.imshow('image', frame)
        g_run = g_run - 1
        # print('g_run: {}'.format(g_run))

    fps_msec = int(1000.0/fps)
    c = cv2.waitKey(fps_msec) & 0xFF
    # print('{}'.format(c))

    if c == ord('f'):
        g_run = 1
        print('Per frame mode')
    if c == ord('c'):
        current_pos = current_pos - 2
        g_cap.set(cv2.CAP_PROP_POS_FRAMES, current_pos)
        g_run = 1
        print('<<<')
    if c == ord('v'):
        g_run = 1
        print('>>>')

    if c == ord('p'):
        g_run = -1
        print('move mode')
    if c == ord('q'):
        print('quit')
        break
    '''
    if cv2.waitKey(fps_msec) & 0xFF == ord('q'):
        break
    '''

g_cap.release()
cv2.destroyAllWindows()