import cv2
import numpy as np

def show_image(imgs,time=None):
    """
    :param img:
    :param time: optional param for how long the image is supplied, in seconds if None, then show until "q"
    """

    #TODO implement time parameter
    if time !=None:
        raise NotImplementedError()
    if len(imgs) >= 50:
        Warning("May have passed in an img instead of list of imgs")

    if len(imgs) == 0:
        Warning("Empty image list")
        return


    for index in range(len(imgs)):
        window_name = "%d" % index
        cv2.imshow(window_name,imgs[index])

    #show img until user hits strokes 'q'
    eight_bit_mask = 0xFF
    quit_val = ord("q")
    save_val = ord("s")
    while (True):
        key = cv2.waitKey(1)
        if (key & eight_bit_mask) == quit_val:
            cv2.destroyAllWindows()
            break