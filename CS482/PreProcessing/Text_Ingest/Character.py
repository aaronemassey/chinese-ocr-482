import numpy as np

# helpful Character image wrapper for collecting all sorts of data into a singular object

@DeprecationWarning
class Character(object):

    #An image wrapper that collections metadata of a singular character image
    # Image Immutable, but other attributes are not

    def __init__(self,img,flags=None):

        self.img = np.copy(img)

    def get_image(self):
        return np.copy(self.img)