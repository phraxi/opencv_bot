import cv2 as cv
import numpy as np
import os
from time import time

import window_capture
from window_capture import WindowCapture


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
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('p'):
        cv.imwrite('pos/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('n'):
        cv.imwrite('neg/{}.jpg'.format(loop_time), screenshot)
print('Done.')

