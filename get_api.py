# 지브리 애니메이션 영화들을 불러와서 Movie모델에 저장하는 api 함수
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt.settings")
import django
django.setup()
from movies.models import Movie

def f(query):
    params = {"api_key": "bd463403fc92a46ec88c4cc94afcc3cd",
            "language": "ko",
            "query": query,
            }
    
    url = "https://api.themoviedb.org/3/search/movie"
    res = requests.get(url, params = params)
    data = res.json()['results']
    
    if (len(data) > 0):
        for item in data:
            if query == "반딧불이의 묘":
                if item['id'] == 12477:
                    title=item['title'],
                    overview = item['overview'],
                    release_date = item['release_date'],
                    poster_path = item['poster_path'],
                    vote_average = item['vote_average']
                else:
                    continue
            elif query == "마녀 배달부 키키":
                if item['id'] == 16859:
                    title=item['title'],
                    overview = item['overview'],
                    release_date = item['release_date'],
                    poster_path = item['poster_path'],
                    vote_average = item['vote_average']
                else:
                    continue
            else:
                title=item['title'],
                overview = item['overview'],
                release_date = item['release_date'],
                poster_path = item['poster_path'],
                vote_average = item['vote_average']

            params_director = {"api_key": "bd463403fc92a46ec88c4cc94afcc3cd",
                "language": "ko",
                "movie_id": item['id'],
                }
            
            movie_id = item['id']
            url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
            res = requests.get(url, params = params_director)
            data = res.json()

            flag = False
            for item in data['crew']:
                if flag == True:
                    continue
                if item['job'] == 'Director':
                    Movie(
                        title=title[0],
                        overview = overview[0],
                        release_date = release_date[0],
                        poster_path = poster_path[0],
                        vote_average = vote_average,
                        director=item['name']
                    ).save()
                    flag = True

                    
            

if __name__ == '__main__':
    f('바람계곡의 나우시카')
    f('천공의 성 라퓨타')
    f('반딧불이의 묘')
    f('이웃집 토토로')
    f('마녀 배달부 키키')
    f('추억은 방울방울')
    f('붉은 돼지')
    f('바다가 들린다')
    f('폼포코 너구리 대작전')
    f('귀를 기울이면')
    f('모노노케 히메')
    f('이웃집 야마다군')
    f('센과 치히로의 행방불명')
    f('고양이의 보은')
    f('하울의 움직이는 성')
    f('게드전기: 어스시의 전설')
    f('벼랑 위의 포뇨')
    f('마루 밑 아리에티')
    f('코쿠리코 언덕에서')
    f('가구야공주 이야기')
    f('추억의 마니')
    f('붉은 거북')
    f('아야와 마녀')




