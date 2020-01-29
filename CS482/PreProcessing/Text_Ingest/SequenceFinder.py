import cv2
import numpy as np
import vision_tools as vt



def __row_has_text(image_row_line):
    """
    :param image:
    :param image_row:
    :return:
    """
    if np.count_nonzero(image_row_line) == 0:
        return False
    return True


def __create_sequence_image(img,pair):
    """
    :param pair:
    :return:
    """

    pre_output = []
    start_row = pair[0] - 2
    end_row = pair[1] + start_row + 2

    for row in range(start_row,end_row):
        pre_output.append(img[row])

    return np.array(pre_output,dtype='float32')


def __process_vectors_to_image_sequences(img,row_vectors):
    """
    :param img:
    :param row_vectors:
    :return: list of character sequences as images
    """

    output = []
    for pair in row_vectors:
        output.append(__create_sequence_image(img,pair))

    return output


def run(img, flags=None):
    """
    :param img: binary image hopefully with text
    :param flags:
    :return: a list of every coordinate sequence of text in input binary image

    assumes blocks of text

    """

    bordered_img = cv2.copyMakeBorder(img, 0, 50, 0, 50, borderType=cv2.BORDER_CONSTANT, value=0)

    row_vector_sequences = []

    rows,cols = img.shape
    start_row_depth_vector = None
    depth = 0

    #get the rows that have text and their associated depths

    for row in range(rows):


        # if we found a part of a sequence of text
        if __row_has_text(bordered_img[row]):
            # if we're starting a new sequence
            if start_row_depth_vector == None:
                start_row_depth_vector = row
                depth += 1
                continue
            # if we're continuing a sequence
            elif start_row_depth_vector != None:
                depth += 1
                continue
            # a sequence of a text has ended or not been found
        else:
            if start_row_depth_vector != None:
                row_vector_sequences.append((start_row_depth_vector,depth))
                start_row_depth_vector = None
                depth = 0
                continue
            # we simply continue looking otherwise


    output = __process_vectors_to_image_sequences(img,row_vector_sequences)

    return output


