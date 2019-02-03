from cave.morphers import MORPHERS
from helpers import get_classes, get_modules


def detect_morpher(url):
    for morpher in MORPHERS:
        match = morpher.match_url(url)
        if match:
            return morpher
    return morphers.base.Morph
