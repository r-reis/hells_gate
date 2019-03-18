import argparse
from urllib import request
from bs4 import BeautifulSoup as bs4
from re import sub

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--artist", dest="artist",
       default=False, help="the name of an artist or band")
parser.add_argument("-m", "--music", dest="music", default=False, help="the name of music")
args = parser.parse_args()


def verify_args(args):
    default_page = 'https://www.azlyrics.com'
    regex = '(-|_| |)'
    if args.artist and args.music:
        artist, music = args.artist.lower(), args.music.lower()
        artist = sub(regex, '', artist)
        music = sub(regex, '', music)
        page = '/lyrics/' + artist + '/' + music + '.html'
        get_lyrics(default_page + page)
    elif args.artist:
        artist = args.artist.lower()
        artist = sub(regex, '', artist)
        page = '/s/' + artist + '.html'
        search_music(default_page + page)


def get_lyrics(page):
    soup = request.urlopen(page)
    soup = bs4(soup, 'html.parser')
    dirty_lyrics = soup.select(".col-lg-8.text-center")
    for i, item in enumerate(dirty_lyrics[0]):
        if i == 16:
            lyrics = item.text
    print(lyrics)


def search_music(page):
    soup = request.urlopen(page)
    soup = bs4(soup, 'html.parser')
    dirty_lyrics = soup.select("#listAlbum")
    dirty_lyrics = dirty_lyrics[0].findAll(["b", "a"])
    #filer_b = lambda x: x.name == "b"
    #albums = list(filter(filter_b, dirty_lyrics))
    album = []
    sugestion = []
    for item in dirty_lyrics:
        if item.name == "b":
            sugestion.append(album)
            album = []
        album.append(item)
    for i in range(1, len(list(sugestion))):
        print(sugestion[i][0].text)


verify_args(args)
