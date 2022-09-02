import os
import sys
import numpy as np
import cv2 as cv
import pyautogui
import PIL
import win32gui
import win32ui
import win32con

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


if __name__ == '__main__':
    #capture_win()
    fast_capture()
    #slow_capture()
