import cv2
import argparse
import sys
from Page_Ingest import BlockFinder
from Text_Ingest import ProduceCharacters
import vision_tools as vt
import os.path





def work_image(image,flags=None):

    text_blocks = BlockFinder.run(original)
    character_img_list = []
    for block in text_blocks:
        character_img_list = character_img_list + ProduceCharacters.run(block)

    return character_img_list

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="PreProcesses an input Image File for Chinese OCR")
    parser.add_argument("<image_path>",help="Path to an image to be worked over")
    parser.add_argument("--output_dir",help="Optional argument that forces script to write PreProcessed image to arg directory")

    args_dict = vars(parser.parse_args())
    if not (os.path.isfile(args_dict["<image_path>"])):
        raise ValueError("Image Path Given Invalid")

    output_dir = os.path.join(os.path.curdir,"OUTPUT/")

    if args_dict["output_dir"] != None:
        output_dir = args_dict["output_dir"]

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
        print "Output Directory Did not Exist. Creating Output Directory..."


    original = cv2.imread(args_dict["<image_path>"], cv2.IMREAD_COLOR)
    images = work_image(original)


    char_idx = 0
    for image in images:
        image_name = "char%d" % char_idx
        image_name = image_name + os.path.splitext(args_dict["<image_path>"])[-1]
        output_path = os.path.join(output_dir,image_name)
        cv2.imwrite(output_path,image)
        char_idx += 1

