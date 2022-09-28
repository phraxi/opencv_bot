import numpy as np
import cv2 as cv
import pyautogui
import win32gui
import win32ui
import win32con
from mss import mss
import time
from ewmh import EWMH


class WindowCapture:
    # properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0
    window_name = None

    # constructor
    def __init__(self, window_name):
        # find the handle for the window we want to capture
        self.hwnd = win32gui.FindWindow(None, window_name)
        self.window_name = window_name
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))

        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # account for the window border and titlebar and cut them off
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    # fast capture on Windows
    def fast_screen_cap_win(self):

        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        img = img[..., :3]
        img = np.ascontiguousarray(img)
        return img

    # Method to return a list with the names of all opened windows
    @staticmethod
    def list_window_names():
        li = []

        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                li.append(win32gui.GetWindowText(hwnd))

        win32gui.EnumWindows(win_enum_handler, None)
        return li

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # pos = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, pos):
        return pos[0] + self.offset_x, pos[1] + self.offset_y

'''
# Things for Linux can be ignored
def fast_screen_cap_lin():
    top = 0
    left = 0
    width = 600
    height = 400
    start_time = time.time()
    mon = {'top': top, 'left': left, 'width': width, 'height': height}
    with mss() as sct:
        while True:
            last_time = time.time()
            img = sct.grab(mon)
            print('FPS: {0}'.format(1 / (time.time() - last_time)))
            cv.imshow('test', np.array(img))
            cv.moveWindow('test', width + 100, 0)
            cv.resizeWindow('Test', width, height)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break


# selects needed window for screen capture
def select_window_lin():
    ewmh = EWMH()
    wins = ewmh.getClientList()
    win = ewmh.getActiveWindow()
    for i in wins:
        name = ewmh.getWmName(i)
        if str(name).__contains__('Mozilla'):  # replace with la name
            ewmh.setMoveResizeWindow(i, 1, 0, 0, 600, 400)
            ewmh.setActiveWindow(i)
            ewmh.display.flush()
'''



