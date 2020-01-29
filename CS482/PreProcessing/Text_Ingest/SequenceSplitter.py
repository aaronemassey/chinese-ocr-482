import cv2
import numpy as np
import vision_tools as vt



def __list_characters_from_sequence(sequence,character_vectors):
    """
    :param sequence: an image that is a sequence of candidate characters
    :param character_vectors: Coordinates that describe each character
    :return: a list of candidate character images
    """

    output =[]
    for v in character_vectors:
        output.append(__create_character_image(sequence,v))
    return output


def __create_character_image(img,pair):
    """
    :param img:
    :param pair: a vector of column and length
    :return:
    """

    pre_output = []
    rows = img.shape[0]
    start_col = pair[0]
    end_col = pair[0] + pair[1]


    for row in range(rows):
        pre_output.append([])
        for col in range(start_col,end_col):
            pre_output[row].append(img[row][col])

    return np.array(pre_output, dtype='float32')





def __col_has_text(sequence,col):
    """
    :param sequence: an image that is a sequence of characters
    :param col:
    :return: boolean val
    """
    for row in sequence:
        if row[col] != 0:
            return True
    return False


def run(sequences):
    """
    :param sequences: a list of image rows that are sequences of characters each
    :return: a list of images that comprise every character
    """



    character_imgs = []

    for sequence in sequences:


        rows,cols = sequence.shape

        length = 0 # length of character
        starting_column = None #starting column of character

        for col in range(cols):
            # if character in column
            if __col_has_text(sequence,col):

                # if starting a new character
                if starting_column == None:
                    starting_column = col
                    length += 1
                    continue

                else: # else continuing to read a character
                    length += 1
            else: # this column is without a chaqracter
                # if ending a character
                if starting_column != None:
                    character_imgs.append(__create_character_image(sequence,(starting_column,length)))
                    starting_column = None
                    length = 0


    return character_imgs