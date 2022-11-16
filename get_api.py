# 지브리 애니메이션 영화들을 불러와서 Movie모델에 저장하는 api 함수
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt.settings")
import django
django.setup()
from movies.models import Movie, Director

def get_api(query):
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
                    if item['name'] == 'Hayao Miyazaki':
                        item['name'] = '미야자키 하야오'
                        profileImg = 'movies/imgs/미야자키_하야오.png'
                    elif item['name'] == 'Goro Miyazaki':
                        item['name'] = '미야자키 고로'
                        profileImg = 'movies/imgs/고로_미야자키.png'
                    elif item['name'] == 'Isao Takahata':
                        item['name'] = '타카하타 이사오'
                        profileImg = 'movies/imgs/타카하타_이사오.png'
                    elif item['name'] == 'Hiroyuki Morita':
                        item['name'] = '모리타 히로유키'
                        profileImg = 'movies/imgs/모리타_히로유키.png'
                    elif item['name'] == 'Yoshifumi Kondō':
                        item['name'] = '콘도 요시후미'
                        profileImg = 'movies/imgs/콘도_요시후미.png'
                    elif item['name'] == 'Hiromasa Yonebayashi':
                        item['name'] = '요네바야시 히로마사'
                        profileImg = 'movies/imgs/요네바야시_히로마사.png'
                    elif item['name'] == 'Tomomi Mochizuki':
                        item['name'] = '모치즈키 토모미'
                        profileImg = 'movies/imgs/모치즈키_토모미.png'
                    elif item['name'] == 'Michael Dudok de Wit':
                        item['name'] = '미카엘 뒤독 더빗'
                        profileImg = 'movies/imgs/미카엘.png'
                    Director(
                        name = item['name'],
                        profileImg = profileImg
                    ).save()
                    Movie(
                        title=title[0],
                        overview = overview[0],
                        release_date = release_date[0],
                        poster_path = poster_path[0],
                        vote_average = vote_average,
                        director=item['name']
                    ).save()
                    flag = True
    return
                    

def save_wise_saying():
    wise_sayings = [
        '아무리 강한 무기가 있어도, 수많은 로보트를 조종해도, 땅을 떠나서는 살 수 없는 거예요!',
        '누가 이 세계를 이런 꼴로 만들어버린걸까요..?',
        '아니...난 아무것도 필요없어..오빠만 있으면 돼..가지마.가지마..다시는 안 간다고 해..',
        '토토로를 봤어! 토토로가있었어',
        '키키, 너무 겉모양에만 신경쓰지마. 중요한 건 마음가짐이야.',
        '오늘이 안되면 내일이 있다...언제라도 내일은 있다.',
        '날지않는 돼지는 그냥 돼지일 뿐이야.',
        '역시 난 좋아했던 거야. 그렇게 느껴졌다.',
        '원하는걸 포기한다면 그것은 원하는게 아니다.',
        '자기안의 원석을 찾아내서 오랜시간 다듬어 가는거란다.',
        '숲을 파괴한 인간들이 내 이빨을 피해가려고 내놓은 아이가 바로 산이다!',
        '아무리 힘든 일이 있어도 "어쩔 수 없잖아" 하며 한 번 뒤돌아보게 만드는 이 말을 주문인 양 외우면서 다시 시작할 수밖에 없잖습니까?',
        '정말 소중한 것이 사라졌는데도 아직도 모르겠습니까?',
        '고양이를 도운 것도, 일이 꼬인것도 모두 나의 소중한 시간 이었어.',
        '어째서...? 난 이미 충분히 도망쳤어. 이제야 지켜야만 하는 것이 생겼어... 너야.',
        '목숨은 죽는다는것을 알기에 소중한 거야.',
        '포뇨, 소스케 좋아 !',
        '아리에티 너는 나에게 심장의 일부분과같은 존재야, 잊지않아 영원히',
        '선배가 좋아요.',
        '돌아라 돌아오렴 아득한 시간이여. 돌아와서 마음을 떠올려 다오. 새, 벌레, 짐승, 풀, 나무, 꽃. 사람의 정을 주고 키워서 기다린다고 하면 지금 돌아가리라.',
        '또 나를 찾아줘',
        '대사가 없는 작품입니다.',
        '메리크리스마스 아야츠루'
    ]
    for i in range(1,24):
        movie = Movie.objects.get(pk=i)
        movie.wise_saying = wise_sayings[i-1]
        movie.save()
    
    return

def save_wise_saying_director():
    wise_sayings = [
        # 미야자키 하야오 (0)
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        # 미야자키 고로 (1)
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
    ]

    for i in range(1,24):
        director = Director.objects.get(pk=i)
        director.wise_saying = wise_sayings[i-1]
        director.save()

    return


def background_img():
    background_imgs = [
        'https://blog.kakaocdn.net/dn/YNmKl/btqInMyCIDX/kzunkFFKxFDcD3dEzKmOO1/img.jpg',
        'https://www.themoviedb.org/t/p/original/sof3WWQkFJWYUYLekB2AQsHH8kO.jpg',
        'https://movie-phinf.pstatic.net/20140527_61/14011807186707bxkw_JPEG/movie_image.jpg?type=m665_443_2',
        'https://wallpaperaccess.com/full/371944.jpg',
        'https://mblogthumb-phinf.pstatic.net/MjAyMDA2MDVfNTIg/MDAxNTkxMzQ0MTk2OTQ3.8SO4O5vt52ynZRz0bMgIUoAxk2t55gctm7FqoiyYKksg.hvzIA0AmjoCFna5bAAaydAGCC7TwjDC9T_P5O3qrHu0g.JPEG.pola0216/%EC%95%84%EC%9D%B4%ED%8F%B0%EB%B0%B0%EA%B2%BD%ED%99%94%EB%A9%B4%EC%A7%80%EB%B8%8C%EB%A6%AC01.jpg?type=w800',
        'https://pbs.twimg.com/media/DTzh1AsVoAADfro.jpg',
        'https://i.pinimg.com/originals/8f/40/99/8f40996e594eafa9f9a0fd27b8852789.jpg',
        'http://aniland1.cafe24.com/studio_ghibri/download/img/ocean-waves.jpg',
        'https://movie-phinf.pstatic.net/20111222_26/1324494911821X2uMr_JPEG/movie_image.jpg?type=m665_443_2',
        'https://t1.daumcdn.net/tistoryfile/fs4/9_tistory_2008_03_20_11_09_47e1c751f34ee?original',

        
        # 작업해야 됨
        'https://movie-phinf.pstatic.net/20111222_227/1324490975580VT6mm_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20111222_161/1324483673805cncT9_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20111223_180/1324647483094XPBf5_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20150108_83/1420706407615GKsAa_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20141119_192/1416356967659SuqYP_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20111221_127/1324474450767xFGrV_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20111221_52/1324455332537ItLuH_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20111222_5/1324534713810nmp4z_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20111223_118/1324621639230xCenO_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20111223_294/1324646972387jhaNK_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20140513_260/13999479042099cfCD_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20150304_168/1425432318297jKlPz_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20160513_4/1463120606278RnuKH_JPEG/movie_image.jpg?type=m665_443_2',
        'https://movie-phinf.pstatic.net/20210429_120/1619660050576j0QoT_JPEG/movie_image.jpg?type=m665_443_2'
    ]

    for i in range(1,24):
        movie = Movie.objects.get(pk=i)
        movie.backgroundImg = background_imgs[i-1]
        movie.save()

    return


if __name__ == '__main__':
    get_api('천공의 성 라퓨타')
    get_api('바람계곡의 나우시카')
    get_api('반딧불이의 묘')
    get_api('이웃집 토토로')
    get_api('마녀 배달부 키키')
    get_api('추억은 방울방울')
    get_api('붉은 돼지')
    get_api('바다가 들린다')
    get_api('폼포코 너구리 대작전')
    get_api('귀를 기울이면')
    get_api('모노노케 히메')
    get_api('이웃집 야마다군')
    get_api('센과 치히로의 행방불명')
    get_api('하울의 움직이는 성')
    get_api('고양이의 보은')
    get_api('게드전기: 어스시의 전설')
    get_api('벼랑 위의 포뇨')
    get_api('마루 밑 아리에티')
    get_api('코쿠리코 언덕에서')
    get_api('가구야공주 이야기')
    get_api('추억의 마니')
    get_api('붉은 거북')
    get_api('아야와 마녀')
    save_wise_saying()
    save_wise_saying_director()
    background_img()




