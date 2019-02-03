from cave.morphers.base import Morph


class FourChan(Morph):
    NAME = '4chan'
    URL = '4chan.org'
    IMAGE_PATTERN = '.fileThumb'
    SSL = 'http:'
    LINK = 'href'
