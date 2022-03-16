import matplotlib.pyplot as plt
from matplotlib.image import imread
from pathlib import Path
from PIL import Image
import os
from itertools import islice
from math import ceil
import argparse

def chunks(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def main():

    # Construct the argument parser
    parser = argparse.ArgumentParser(
        prog="Image viewer utility",
        description="Program to view images",
        epilog="Author: Dalton Hensley",
    )

    # Provide implementation for `type` user argument
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        required=True,
        default="human_faces",
        choices=["human_faces", "cat_faces"],
        help="Pick which type of faces to view",
    )

    # Collect user supplied arguments
    args = parser.parse_args()


    # Number of human images to show at a time
    CHUNK_SIZE = 6

    # Directory of images
    img_dir = Path("face_images/" + args.type)

    # Collect the paths of images into a list
    img_list = list(img_dir.rglob("*.jpg"))

    # Split this collection of human images into 6. This is because we only
    # want to work with 6 images at a time.
    chunked_list = chunks(img_list, CHUNK_SIZE)

    # Walk through the batches of human images and display the human
    for chunk_idx, chunk in enumerate(chunked_list):
        print(f"Batch: {chunk_idx + 1}")
        for img_idx, img in enumerate(chunk):
            print("image " + str(img_idx + 1) + ":", str(img))
            plt.subplot(3, 2, img_idx + 1)

            img_slice = plt.imread(img)
            plt.imshow(img_slice, cmap="gray")

        plt.tight_layout()
        plt.show()


main()
