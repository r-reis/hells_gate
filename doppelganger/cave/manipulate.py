import requests
import os
import re
from io import BytesIO

BASE_PATH = 'vault/'


def get_url(url):
    return requests.get(url)


def save_image(file_name, page):
    local_file = open(file_name, "wb")
    local_file.write(page.read())
    local_file.close()
    return local_file


def download_images(path, image_urls):
    path = path.replace("/", "")
    file_path = os.path.join(BASE_PATH, path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    os.chdir(file_path)
    index = 0
    for index, image in enumerate(image_urls):
        img_type = re.findall(r"\.\w+$", image)
        if not img_type:
            continue
        file_name = str(index) + img_type[0]
        try:
            page = requests.get(image)
            page = BytesIO(page.content)
            print('downloading...', image)
            save_image(file_name, page)

        except Exception as ex:
            print(ex)
            print("not found =(")
            raise

    if index:
        print("download completed\n")
        print(index + 1, "files downloaded")
    else:
        print("nothing found")
