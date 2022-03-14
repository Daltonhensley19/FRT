import requests
from selenium import webdriver
from time import sleep
import os
import argparse
from pathlib import Path


def main():

    # Construct the argument parser
    parser = argparse.ArgumentParser(
        prog="Random Face Scraper",
        description="Program to scrape random faces.",
        epilog="Author: Dalton Hensley",
    )

    # Provide implementation for `count` user argument
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        required=False,
        default=5,
        help="Number of faces to scrape",
    )

    # Collect user supplied arguments
    args = parser.parse_args()

    SCRAPE_CYCLE = args.count
    TOTAL_IMGS = args.count

    # Scrap on Firefox
    url = "https://this-person-does-not-exist.com/en"
    driver = webdriver.Firefox()

    # Begin at the target website
    driver.get(url)

    # Switch working directory to save images inside `face_images`
    os.chdir("face_images/")

    # Process until we do all scrape cycles
    img_count = 1
    while SCRAPE_CYCLE != 0:

        # Find the face image on the target website
        img = driver.find_element_by_id("avatar").get_attribute("src")
        print(img)

        print(f"Scrapping Image {img_count} of {TOTAL_IMGS}...\n")

        # Get a http request handle to the img url
        r = requests.get(img)
        print(r)

        # Get the image name out of the url
        img_name = img.split("/")[-1]

        # Save face image using the http request handle
        with open(str(img_name), "wb") as f:
            f.write(r.content)

        # Refresh the browser to get a new face
        print("Refreshing...")
        driver.refresh()
        sleep(2)
        os.system("clear")

        SCRAPE_CYCLE -= 1
        img_count += 1

    # Close Firefox when complete
    driver.quit()


main()
