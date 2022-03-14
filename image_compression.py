from pathlib import Path
from PIL import Image, ImageOps
import PIL
import os
import argparse


def main():

    # Construct the argument parser
    parser = argparse.ArgumentParser(
        prog="Image compression utility",
        description="Program to compress images",
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
        help="Pick which type of faces to compress",
    )

    # Collect user supplied arguments
    args = parser.parse_args()


    # Work inside the `face_images` directory
    dir = Path("/home/dalton/desktop/face_research/face_images/" + args.type)

    # Collect all images that are .jpg files
    img_list = dir.rglob("*.jpg")

    # Switch working directory (maybe not needed?)
    os.chdir("face_images/")

    # for each image in the collection of images
    for img in img_list:
        try:
            print(img)

            # Convert to grayscale and overwrite
            with Image.open(img) as f:
                f = ImageOps.grayscale(f)
                f.save(str(img), optimize=True, quality=65)

            # Handle bad images by deleting them
        except PIL.UnidentifiedImageError:
            print("Removing bad or Empty image")
            img.unlink()


main()
