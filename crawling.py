import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt.settings")
import django
django.setup()
from movies.models import Movie


# 각 영화들의 명언을 크롤링해서 저장하는 함수
def ghibli_wise_saying():
    movies = Movie.objects.all()
    for movie in movies:
        req = requests.get(f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={movie.title}')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        wise_saying = soup.select(
            '#main_pack > div > div > div > h2 > span > strong > a'
        )
        if len(wise_saying) == 0:
            wise_saying = soup.select(
                '#main_pack > div > div > div > h2 > span > strong'
            )
        # if len(wise_saying) == 0:
        #     wise_saying = soup.select(
        #         '#main_pack > div > div > div > h2 > span > strong > a'
        #     )
        if len(wise_saying) == 0:
            wise_saying = soup.select(
                '#main_pack > div.sc_new.cs_common_simple._au_movie_content_wrap > div.cm_top_wrap > div.title_area.type_keep._title_area > h2 > span > strong'
            )
        if len(wise_saying) == 0:
            continue

        print(wise_saying[0].text)
        print()

    return

# 카카오 크롤링 (AI)
# def kakao_crawling_ai():
#     req = requests.get('https://tech.kakao.com/?s=ai')
#     html = req.text
#     soup = BeautifulSoup(html, 'html.parser')
#     my_titles = soup.select(
#         'h3 > a'
#         )
#     my_contents = soup.select(
#         'div.elementor-post__excerpt > p'
#         )

#     contents = []
#     for content in my_contents:
#         contents.append(content.text)
#     titles = []
#     links = []
#     for title in my_titles:
#         if title.text.strip() == 'Main':
#             continue
#         titles.append(title.text.strip())
#         links.append(title.get('href'))

#     for item in zip(titles, contents, links):
#         Article(
#             title=item[0],
#             content=item[1],
#             link=item[2],
#             company = '카카오',
#             tech = 'AI'
#         ).save()

#     return

    # crawlingData(
    #     title=titles,
    #     content=contents,
    #     link=links,
    #     company = 'nhn',
    #     tech = '클라우드'
    # ).save()




if __name__=='__main__':
    ghibli_wise_saying()


