from cave.morphers.base import Morph
from cave.morphers import fourchan, deviantart, base


MORPHERS = [
    fourchan.FourChan,
    deviantart.DeviantArt,
    base.Morph,
]

__all__ = [
    'Morph',
    'MORPHERS',
]
