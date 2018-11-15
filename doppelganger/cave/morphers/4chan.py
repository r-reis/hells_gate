from .helpers import MorphMixin


class FourChanMorph(MorphMixin):

    def _get_images(soup_images):
        return [image.get('href') for image in soup_images]
