from itertools import count

import cv2 as cv
import numpy as np
import os
from time import time
from window_capture import WindowCapture


def count_files_in_dir(di):
    return len([entry for entry in os.listdir(di) if os.path.isfile(os.path.join(di, entry))])


#WindowCapture.list_window_names(None)
wincap = WindowCapture('LOST ARK (64-bit, DX11) v.2.7.1.1')
loop_time = time()
while (True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    cv.imshow('Lost Ark Bot', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    pos = 'pos'
    neg = 'neg'

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('p'):
        cv.imwrite('pos/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('n'):
        cv.imwrite('neg/{}.jpg'.format(loop_time), screenshot)
print("Positive Screenshots: ", count_files_in_dir(pos))
print("Negative Screenshots: ", count_files_in_dir(neg))

