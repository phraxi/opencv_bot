from itertools import count

import cv2 as cv
import numpy as np
import os
from time import time
from window_capture import WindowCapture


# utility function to count all files in dir
def count_files_in_dir(di):
    return len([entry for entry in os.listdir(di) if os.path.isfile(os.path.join(di, entry))])


# method to find the window of LA (or other app) that needs to be captured
def find_la_win():
    wins = WindowCapture.list_window_names()
    for i in wins:
        if i.__contains__('LOST ARK'):
            la_win = WindowCapture(i)
            print(i)
    return la_win


# initializes screen capture of the chosen window and renders images every second to an
# open cv window
def ini_capture(window):
    loop_time = time()
    while True:
        # get an updated image of the game
        screenshot = window.fast_screen_cap_win()
        cv.imshow('Lost Ark Bot', screenshot)
        # print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()
        pos = 'pos'
        neg = 'neg'

        # waits 1 ms every loop to process key presses
        key = cv.waitKey(1)
        # press 'q' with the output window focused to exit.
        if key == ord('q'):
            cv.destroyAllWindows()
            break
        # press 'p' to take a positive screenshot and write it in pos dir
        elif key == ord('p'):
            cv.imwrite('pos/{}.jpg'.format(loop_time), screenshot)
        # press 'n' to take a negative screenshot and write it in neg dir
        elif key == ord('n'):
            cv.imwrite('neg/{}.jpg'.format(loop_time), screenshot)
    # print("Positive Screenshots: ", count_files_in_dir(pos))
    # print("Negative Screenshots: ", count_files_in_dir(neg))


win = find_la_win()
ini_capture(win)
