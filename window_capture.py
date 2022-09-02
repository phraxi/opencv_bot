import os
import sys

import cv2
import numpy as np
import cv2 as cv
import pyautogui
import Xlib
from PIL import ImageGrab
#import win32gui
#import win32ui
#import win32con

from mss import mss
import time
from ewmh import EWMH
import random as rd

# slowest screen capture with pyautogui
def slow_screen_capture():
    loop_time = time.time()
    while (True):
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        cv.imshow('Hi', screenshot)
        print('FPS{}'.format(1 / (time.time() - loop_time)))
        loop_time = time.time()
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


def fast_screen_capture():
    top = 0
    left = 0
    width = 1280
    height = 720
    start_time = time.time()
    mon = {'top': top, 'left': left, 'width': width, 'height': height}
    with mss() as sct:
        while True:
            last_time = time.time()
            img = sct.grab(mon)
            print('FPS: {0}'.format(1 / (time.time() - last_time)))
            cv.imshow('test', np.array(img))
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break
'''
# fast capture for windows (still slower)
def capture_win():
    w, h = 1280, 720
    start_time = time()
    while{True}:
        last_time = time()
        # for now we will set hwnd to None to capture the primary monitor
        # hwnd = win32gui.FindWindow(None, window_name)
        hwnd = None

    # get the window image data
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (h, w, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel to work with cv.matchTemplate()
        img = img[..., :3]

        # make image C_CONTIGUOUS to avoid errors with cv.rectangle()
        img = np.ascontiguousarray(img)
        print('FPS: {0}'.format(1 / (time()-last_time)))
        cv.imshow('Steam', img)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


def win_enum_handler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        print(hex(hwnd), win32gui.GetWindowText(hwnd))
'''

# selects needed window for screen capture
def select_window():
    ewmh = EWMH()
    wins = ewmh.getClientList()
    win = ewmh.getActiveWindow()
    for i in wins:
        name = ewmh.getWmName(i)
        #print(name)
        if str(name).__contains__('Mozilla'):  # replace with la name
            ewmh.setMoveResizeWindow(i, 1, 0, 0, 1280, 720)
            ewmh.setActiveWindow(i)
            ewmh.display.flush()
            time.sleep(2)
        #print(name)


if __name__ == '__main__':
    #select_window()
    #capture_screen_win()
    test_screen_capture()
    #slow_screen_capture()
