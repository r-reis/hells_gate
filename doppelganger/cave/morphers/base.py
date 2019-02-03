import re
from cave import manipulate


class Morph:
    NAME = 'generic'
    URL = ''
    IMAGE_PATTERN = 'img'
    SSL = ''
    FOLDER = ''
    LINK = 'src'

    @staticmethod
    def image_predicate(image_name):
        if(image_name != None):
            return image_name

    @classmethod
    def get_images(cls, soup):
        return [
            cls.SSL + str(cls.image_predicate(image.get(cls.LINK)))
            for image in soup.select(cls.IMAGE_PATTERN)
        ]

    @classmethod
    def match_url(cls, url):
        return cls.URL in url

    @classmethod
    def setup_morpher(cls, loup):
        dir_name = soup.title.string
        dir_name = dir_name.replace("/", "").replace("-", "").replace(" ", "_")
        morph_type = cls.identify_race(soup)
        return cls(dir_name, soup, morph_type)

    @classmethod
    def download(cls, soup):
        images = cls.get_images(soup)
        manipulate.download_images(soup.title.string, images)
