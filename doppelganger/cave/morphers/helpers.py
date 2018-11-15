from itertools import Iterable

from bs4.element import Tag


class MorphMixin(object):

    def __init__(self):
        pass

    def _get_images(self):
        pass

    def get_images(soup_images):
        if not isinstance(soup_images, Iterable):
            soup_images = [soup_images]

        if not all(isinstance(image, Tag) for image in soup_images):
            raise Exception('All images must be tags')

        return self._get_images(soup_images)
