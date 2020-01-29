import cv2
import numpy as np
import vision_tools as vt



def __list_text_block_images(image,vectors):
    """
    :param image:
    :param vectors:
    :return:list of subimages
    """

    output = []
    for rectangle in vectors:
        x = rectangle[0]
        y = rectangle[1]
        width = rectangle[2]
        height = rectangle[3]
        img = image[x:x+height, y:y+width]
        output.append(np.array(img,dtype='float32'))
    return output


def run(image,flags=None):
    """
    :param image: an image to find blocks of text with
    :param flags:
    :param comparison: image utilized for comparison
    :return: a list of sub images that are blocks of text
    """



    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=5)  # dilate
    contours, heirarchy = cv2.findContours(dilated,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    rectangle_vectors = []

    # for each contour found, draw a rectangle around it on original image
    for contour in contours:
        # get rectangle bounding contour
        [col, row, width, height] = cv2.boundingRect(contour)

        # discard areas that are too small
        if height < 40 or width < 40:
            continue

        cv2.rectangle(image,(row,col),(row,col),(255,0,0))

        rectangle_vectors.append((row,col,width,height))

    output = __list_text_block_images(thresh,rectangle_vectors)
    return output





