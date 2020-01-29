import cv2
import SequenceFinder as SF
import SequenceSplitter as SS
from Character import Character
import numpy as np
import vision_tools as vt

MINIMUM_THRESH = 150

def run(image,flags=None):
    """
    :param image: thresholded that consists mainly of a block of text
    :param flags:
    :return: a list of Character objects
    """

    #check constraints on input
    if type(image).__module__ != np.__name__:
        raise ValueError("Image is not a valid np array")
    if image.ndim != 2:
        raise ValueError("Not grayscale image given")
    if image.dtype != 'float32':
        raise ValueError('np.array Datatype must be float32')



    sequence_images = SF.run(image)
    character_images = SS.run(sequence_images)

    return character_images