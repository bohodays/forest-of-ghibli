import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt.settings")
import django
django.setup()
from movies.models import Movie


def img_crawling():
    req = requests.get('https://movie.naver.com/movie/bi/mi/photoView.naver?code=30270')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.select_one(
        '#photo_area > div > div.img_src._img_area > div > div > div > img'
        )
    print(imgs)
    print(imgs.get("src"))


    return

if __name__=='__main__':
    img_crawling()


