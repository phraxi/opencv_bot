import os
import sys
import numpy as np
import cv2 as cv
import pyautogui
# import win32gui
# import win32ui
# import win32con

from mss import mss
from time import time


def slow_capture():
    loop_time = time()
    while (True):
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        cv.imshow('Hi', screenshot)
        print('FPS{}'.format(1 / (time() - loop_time)))
        loop_time = time()
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


def fast_capture():
    top = 0
    left = 0
    width = 1280
    height = 720
    start_time = time()
    mon = {'top': top, 'left': left, 'width': width, 'height': height}
    with mss() as sct:
        while True:
            last_time = time()
            img = sct.grab(mon)
            print('FPS: {0}'.format(1 / (time() - last_time)))
            cv.imshow('test', np.array(img))
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break

    '''
    def fast_capture_win():
        w = 1920  # set this
        h = 1080  # set this
        bmpfilenamename = "out.bmp"  # set this
    
        hwnd = win32gui.FindWindow(None, windowname)
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
        dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
    '''


if __name__ == '__main__':
    #fast_capture()
    slow_capture()
