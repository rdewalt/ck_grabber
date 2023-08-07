"""Simple script to try and scrape comics"""
# Disable "line too long" in pylint
# pylint: disable=C0301


# run with:: (example) python3 gather.py -s 1998-10-05 -e 2023-08-06 -c zits -d 10
import argparse
import datetime as dt
import os
from time import sleep
import requests
from PIL import Image
import bs4 as bs


COOKIES = {'wordpress_logged_in_<HASH YOU NEED TO FILL IN>':'THE OTHER HALF YOU NEED TO FILL IN'}
HEADERS = {}

file_formats = {
    'BMP': '.bmp',
    'JPEG': '.jpg',
    'PNG': '.png',
    'GIF': '.gif',
    'TIFF': '.tif',
    'WEBP': '.webp'
}

def grab_day(strip_date):
    """Move the calendar day up one"""
    return dt.datetime.strftime((dt.datetime.strptime(strip_date,"%Y-%m-%d") + dt.timedelta(days=1)),"%Y-%m-%d")

def grab_strip(comic_name,strip_date):
    """This is where the work happens"""
    source = requests.get(f"https://comicskingdom.com/{comic_name}/{strip_date}",timeout=60, cookies=COOKIES, headers=HEADERS)
    soup = bs.BeautifulSoup(source.content, 'lxml')
    for images in soup.find_all('img', id="theComicImage"):
        comic=images.get("src")
        image=requests.get(comic,timeout=60, cookies=COOKIES, headers=HEADERS)
        if image.status_code == 200:
            with open(f"{comic_name}-{strip_date}",'wb') as file:
                image.raw.decode_content = True
                for chunk in image:
                    file.write(chunk)
            img = Image.open(f"{comic_name}-{strip_date}")
            image_extension=file_formats[img.format]
            year=dt.datetime.strptime(strip_date,"%Y-%m-%d").year
            dir_exists=os.path.exists(f"{comic_name}/{year}/")
            if not dir_exists:
                os.makedirs(f"{comic_name}/{year}/")
            os.rename(f"{comic_name}-{strip_date}",f"{comic_name}/{year}/{comic_name}-{strip_date}{image_extension}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--start', help='Start date')
    parser.add_argument('-e','--end', help='End date')
    parser.add_argument('-c','--comic', help='Strip to Gather')
    args = parser.parse_args()
    COMIC_STRIP=args.comic
    START_DATE=args.start
    END_DATE=args.end
    CURRENT_STRIP=START_DATE
    while(dt.datetime.strptime(CURRENT_STRIP,"%Y-%m-%d")<=dt.datetime.strptime(END_DATE,"%Y-%m-%d")):
        print(f"Grabbing strip for {CURRENT_STRIP}")
        grab_strip(COMIC_STRIP,CURRENT_STRIP)
        CURRENT_STRIP=grab_day(CURRENT_STRIP)
        sleep(1)
