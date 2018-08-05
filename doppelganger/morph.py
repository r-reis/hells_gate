import requests
import os
import re
# from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

url = input()
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

all_images = soup.select('.fileThumb')
dir_name = soup.title.string
dir_name = dir_name.replace("/", "").replace("-", "").replace(" ", "_")


def get_images(all_images):
    images = []
    for image in all_images:
        img_name = image.get("href")
        # img_type = re.findall(r"src=\"(.+jpg)", str(image))
        images.append(img_name)
    return images


def save_image(file_name, page):
    local_file = open(file_name, "wb")
    local_file.write(page.read())
    local_file.close()
    return local_file


def download_images(images):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)
    for index, image in enumerate(images):
        img_type = re.findall(r"\....$", image)
        file_name = str(index) + img_type[0]
        url = 'http:' + image
        try:
            page = requests.get(url)
            page = BytesIO(page.content)
            print('downloading...', url)
            save_image(file_name, page)

        except url:
            print(url, "não encontrada")
            break
    print('download completed')


images = get_images(all_images)

images = [x for x in images if x]

download_images(images)
