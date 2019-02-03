from bs4 import BeautifulSoup as beautiful
from bs4 import Comment
from cave import manipulate, judger

def run():
    url = input("desire:\n")
    # url = 'https://www.deviantart.com/monorirogue/gallery/'
    page = manipulate.get_url(url)
    soup = beautiful(page.text, "html.parser")
    morpher = judger.detect_morpher(url)
    morpher.download(soup)
