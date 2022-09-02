import cv2 as cv
import numpy as np
import os
from time import time
from window_capture import WindowCapture


# initialize the WindowCapture class
wincap = WindowCapture('LOST ARK (64-bit, DX11) v.2.6.0.1')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    cv.imshow('Lost Ark Bot', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')