from pathlib import Path
from PIL import Image, ImageOps
import PIL
import os


def main():

    # Work inside the `face_images` directory
    dir =  Path("face_images").resolve()

    # Collect all images that are .jpg files
    img_list = dir.rglob("*.jpg")

    # Switch working directory (maybe not needed?)
    os.chdir(str(dir))

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
