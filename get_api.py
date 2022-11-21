# 지브리 애니메이션 영화들을 불러와서 Movie모델에 저장하는 api 함수
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt.settings")
import django
django.setup()
from movies.models import Movie, Director, Character

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
        # 미야자키 하야오
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        # 타카하타 이사오
        '오늘이 안되면 내일이 있어. 언제나 내일이 있어. <추억은 방울방울>',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '오늘이 안되면 내일이 있어. 언제나 내일이 있어. <추억은 방울방울>',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '역시 난 그녀를 늘 좋아했었다고.. 그렇게 느낀 순간이었다. <바다가 들린다>',
        '오늘이 안되면 내일이 있어. 언제나 내일이 있어. <추억은 방울방울>',
        # 콘도 요시후미
        '자기안의 원석을 찾아내서 오랜시간 다듬어 가는거란다. <귀를 기울이면>',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '오늘이 안되면 내일이 있어. 언제나 내일이 있어. <추억은 방울방울>',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        '너는 너 자신이 되어야 해 <고양이의 보은>',
        # 미야자키 고로
        '살아있다는 건 누구에게나 미래가 있다는 것. 뒤돌아보면, 바로 거기에 미래가 있단다. <코쿠리코 언덕에서>',
        '미래의 시작은 언제나 즐거운 상상에 있다.',
        # 요네바야시 히로마사
        '난 네 생각대로 살았으면 해, 그래도  자신을 소중히 해줘. <추억의 마니>',
        '살아있다는 건 누구에게나 미래가 있다는 것. 뒤돌아보면, 바로 거기에 미래가 있단다. <코쿠리코 언덕에서>',
        '오늘이 안되면 내일이 있어. 언제나 내일이 있어. <추억은 방울방울>',
        '난 네 생각대로 살았으면 해, 그래도  자신을 소중히 해줘. <추억의 마니>',
        '자그레브 국제 애니메이션 영화제(그랑프리-장편), 애니어워드(최우수 독립 장편 애니메이션)',
        '살아있다는 건 누구에게나 미래가 있다는 것. 뒤돌아보면, 바로 거기에 미래가 있단다. <코쿠리코 언덕에서>'
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
        'https://blog.kakaocdn.net/dn/cZOtQt/btrk18LJy49/kUUMN3eiSmbrKDhhBlavDk/img.png',
        'https://image.cine21.com/resize/cine21/still/2006/0518/M0020054_still3[S750,750].jpg',
        'https://mblogthumb-phinf.pstatic.net/MjAxNzA3MDdfMjAy/MDAxNDk5NDE2Mzg4Mjc5.8TdiNJtU6l2ma0hpDyRNLbTLoqe8zeYy8688Spq8ryYg.q-synK2mKIbEnrPjsoe3N6cewhdc6D1BFOcDBaMJ_BEg.PNG.heedyy/%EC%84%BC%EA%B3%BC_%EC%B9%98%ED%9E%88%EB%A1%9C%EC%9D%98_%ED%96%89%EB%B0%A9%EB%B6%88%EB%AA%85_%285%29_1920x1080.png?type=w800',
        'https://img.insight.co.kr/static/2020/10/20/700/img_20201020113407_usd4k5l9.webp',
        'https://m.media-amazon.com/images/M/MV5BMTMzMDkyODg0MF5BMl5BanBnXkFtZTcwMTQ4ODAyNw@@._V1_.jpg',
        'http://todonavi.com/wp-content/uploads/2020/10/e94d54c7c5fc529b1fc03a0e86d70c31.jpg',
        'https://mblogthumb-phinf.pstatic.net/MjAyMDEyMTBfMTEg/MDAxNjA3NTgxNjEzMDY0.B6Pg57afNyzJJwtCrDJlsHZ423W01lmaS-vQ9PBHexYg.KlCtmlh1UuaOQZqA9yF-357We3k6NLmUtnU3U7Tw4Y8g.JPEG.htae_/ponyo040.jpg?type=w800',
        'https://mblogthumb-phinf.pstatic.net/MjAxODA3MDRfODUg/MDAxNTMwNjQ1MjU3MTcw.XrnZV7SbpKMWdgX3pN-sFNYXZCzoRytfcL63azy5Q6Qg.g5NfQ2eLizL41LXcfBbwTlwVutQ_yiJa90Utrw1k88og.JPEG.dbghk78/xs5lPjHSjWdKIAx1TRn1H5I9zeo.jpg?type=w800',
        'https://i.ytimg.com/vi/SACP7brT-mA/maxresdefault.jpg',
        'https://p4.wallpaperbetter.com/wallpaper/750/1/160/animated-movies-kaguya-princess-the-tale-of-princess-kaguya-wallpaper-preview.jpg',
        'https://www.ghibli.jp/gallery/marnie016.jpg',
        'https://p4.wallpaperbetter.com/wallpaper/72/62/418/the-red-turtle-4k-pc-hd-wallpaper-preview.jpg',
        'https://www.nextflicks.tv/wp-content/uploads/2022/01/Earwig-and-the-Witch.jpg'
    ]

    for i in range(1,24):
        movie = Movie.objects.get(pk=i)
        movie.backgroundImg = background_imgs[i-1]
        movie.save()

    return


def character_info_save():
    name_list = [
        '소피',
        '하쿠',
        '시타',
        '세이타',
        '산',
        '하울',
        '아시타카',
        '톰보',
        '치히로',
        '포뇨',
        '지지',
        '돌라',
        '에보시',
        '키키',
        '사츠키',
        '메이'
    ]

    MBTI_list = [
        'ISFJ',
        'INFJ',
        'INTJ',
        'ISTJ',
        'ISTP',
        'ISFP',
        'INFP',
        'INTP',
        'ENFP',
        'ESFP',
        'ENTP',
        'ESTP',
        'ESTJ',
        'ENFJ',
        'ENTJ',
        'ESFJ'
    ]

    info_list = [
        '소피는 내성적이고 평범해 보이지만, 그녀는 나이에 비해 너무 성숙하고 진지합니다. 그녀는 마법사 하울의 게으름에 지쳐 그의 성을 청소할 정도로 부지런하고, 칼시퍼와 터닙 헤드의 친구인 마클랜드의 어머니인 것 처럼 챙깁니다.',
        '하쿠는 여러 성격을 가지고 있습니다. 그는 때로는 마음씨가 착하고, 때로는 엄하고, 예민할 수도 있습니다. 그는 현명하고 상황에 맞게 행동할 수 있고,  누군가를 신경 쓸 때면 기꺼이 목을 내어줄 정도로 아낍니다. 영화의 처음부터 끝까지, 그는 치히로를 다치지 않게 하고 그녀가 안전하게 떠날 수 있도록 돕기 위해 모든 힘을 쏟는걸 보면 알 수 있죠.',
        '시타는 내성적이고 낯선 사람들에게 다소 수줍어합니다. 그녀의 과묵하고 수줍은 성격에도 불구하고, 시타는 공손하고, 친절하고, 지적이며, 영화는 그녀가 라퓨타의 진정한 후계자로서 무스카로부터 왕국의 남은 것을 구하는 것으로 끝을 맺습니다.  시타는 또한 파즈의 안전을 위해 자신을 멀리해야 한다고 주장하는 동시에 파즈를 사랑할 정도로 그가 그녀를 위해 하는 방식으로 그를 보호하려고 노력함으로써 그녀가 파즈를 깊이 사랑한다는 것을 보여주었습니다.',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut neque, officiis aliquam eius amet ratione non mollitia nam molestiae quod ab rerum ducimus hic laborum reprehenderit. Voluptatem natus neque ut.(세이타)',
        '그녀는 고집이 세고, 성질이 급하고, 용감하고, 방어적이며, 그녀의 주된 관심사는 그녀가 함께 사는 숲과 동물들을 보호하는 것입니다. 처음에 산은 자신의 인간성을 거부하고 자신을 늑대로만 생각하며 상당히 비인간적인 것처럼 보여집니다. 그럼에도 불구하고 그녀는 결국 그녀의 인간성를 처음 본 아시타카를 받아들이게 됩니다.',
        '하울는 자신감이 있을 뿐만 아니라 다소 허영심이 있어 보이며, 자신 외에 다른 사람들에 대해서는 별로 신경을 쓰지 않는 것 같은 모습으로 비춰집니다.하지만 시간이 지나면서 그의 실제 성격이 드러나게 되는데, 그는 사랑스럽고 매력적이며 지적이지만, 고집이 세고 정직하지 못한 경향이 있을 뿐만 아니라 자신의 삶에 관해서는 비밀스러워지는 경향이 있습니다.. 그는 보통 불편한 상황이나 그의 헌신적인 참여가 필요한 상황에 관여하는 것을 피합니다.',
        '아시타카는 극도로 도덕적인 마음의 소유자로, 어려움에 처한 사람은 내버려 두지 않고 도와주고, 생판 남인 타타라 마을과 숲의 분쟁에도 적극적으로 뛰어들어 숲과 인간이 평화롭게 살아갈 수 있도록 돕고자 합니다. 그는 자신의 행동이 사람들의 미움을 사더라도 올곧은 자세와 마음을 유지해서 모두가 평화롭고 서로 공존할 수 있도록 노력합니다. 아시타카는 원래 저주에의해 재앙신처럼 공포와 증오에 잠식되어야 했지만그는 세상을 사심 없이 볼 수 있었고, 그에 따라 항상 옳은 행동을 하고자 하는 인물입니다. 심지어 위험이나 죽음 앞에서도 너무나도 초연한 태도를 유지합니다.',
        '톰보는 키키가 정착한 마을의 친구입니다.  키키가 마을에 왔을 때부터 관심을 보이며 친해지려 해 키키를 파티에 초대하고 기다리지만 문제가 생겨 키키에게 바람맞습니다. 이후 오소노가 키키에게 "코포리"에게 물건을 전해 달라고 부탁하는데, 본명을 들은 적 없는 키키는 그 사람이 톰보란 사실을 알리가 없었고 알고보니 둘의 화해를 위해 오소노가 꾸민 일임을 깨닫게 됩니다. 키키가 처음으로 마을에서 사귄 친구이며, 처음 만났을 때는 서먹했지만 꾸준히 다가간 결과, 키키가 마음을 열어 소중한 친구가 됩니다. 톰보는 발명가 기질이 있어, 자전거 비행기를 만들어 키키와 함께 하늘을 날게 됩니다.',
        '치히로가 유능한 인물로 성장한 것이 영화 전개의 핵심인 것을 보면 치히로의 성격을 알 수 있습니다. 영화 초반에 그녀는  쉽게 겁에 질려버리는 어린 소녀에 불과 하지만 그녀가 사랑하는 사람들을 위해 두려움을 제쳐두는 것을 배운 근면하고 책임감 있고 용감한 어린 소녀로 성장합니다. 그녀는 친구들을 보호하고 부모님을 구하기 위해, 치히로는 용기 있고, 자상하고, 눈치 빠르고, 믿을 수 있는 소녀가 되기 위해 그녀의 예전 성격을 버리고 그녀의 환경에 적응합니다.',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut neque, officiis aliquam eius amet ratione non mollitia nam molestiae quod ab rerum ducimus hic laborum reprehenderit. Voluptatem natus neque ut.(포뇨)',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut neque, officiis aliquam eius amet ratione non mollitia nam molestiae quod ab rerum ducimus hic laborum reprehenderit. Voluptatem natus neque ut.(지지)',
        '처음에 돌라는 라퓨타의 보물을 손에 넣기만 하면 되는 거만하고, 탐욕스럽고, 이기적인 모습으로 영화에 나옵니다. 그러나 나중에 그녀는 다소 마음이 여린 사람이라는 것이 밝혀지고 마지못해 시타와 파즈를 좋아하게 됩니다. 특히 시타는 돌라에게 어린 시절의 자신을 떠올리게 합니다. 돌라는 또한 용감하고 지략이 풍부하며, 이런 성격은 그녀가 그녀의 인생 동안 성공적이고 존경 받는 항공 해적이 되도록 도왔습니다.',
        '에보시는 세상에 긍정적으로 영향을 미치고 싶어하는 강하고 오만한 인물입니다. 마을 사람들은 아이언타운의 리더로서 그녀를 사랑하고, 그녀는 그들을 모두 아이언타운으로 데려와서 주민들을 억압적인 환경으로부터 해방시켜준 사람입니다. 또한 리더십이 있는 성격으로, 긴박한 상황속에서도 침착함을 유지 합니다.',
        '키키는 마녀가 되기 위해 필요한 훈련을 받기 위해 13살에 카리키야에 있는 집을 1년 동안 떠날 정도로 강한 의지를 가지고 있습니다. 그녀는 아주 친절하고, 호기심이 많고, 마음이 착하고, 상냥하고, 쾌활합니다. 하지만, 그녀는 때로는 다소 완고하고 고집이 강하기도 합니다. 그녀는 그녀의 애완용 검은 고양이인 지지에게 매우 애착을 가지고 있으며, 그를 그녀의 가장 친한 친구라고 소개합니다. 키키는 코리코에 처음 도착했을 때 특별히 인기가 있는 것은 아니지만, 점차 고객들과 새로운 친구들을 사귀게 되고 마지막에는 마을 모두의 사랑을 받게 됩니다.',
        '사츠키는 독립적이고 어른스러운 성격을 가지고 있습니다. 그녀는 끊임없이 슬픔과 압박감을 느끼지만, 그것을 드러내지 않고, 그녀가 아픈 어머니에 대해 느끼는 슬픔은 영화가 끝날 무렵 할머니 앞에서 무너질 때 비로소 드러납니다. 그녀는 또한 분명히 어른처럼 행동하고 메이의 좋은 롤모델이 되어야 한다는 것에 매우 압박감을 느낍니다.',
        '메이는 이웃집 토토로에 나오는 사츠키의 여동생입니다. 미야자키 감독의 1987년 메모에 따르면, 믿음직스럽고 재빠른 사츠키와 대조적으로 메이는 외곬으로 인내심이 강한 아이입니다. 고집이 세지만 명랑한 그녀는 집요하고 소심하지 않다는 점에서 언니를 닮았습니다. 그러나 처음에는 수줍음이 많고 말수가 적은 경향이 있어 사츠키보다 훨씬 더 관찰력이 있습니다. 메이는 성격에 어두운 그림자가 전혀 없는 대담하고 행복한 소녀입니다. 그녀는 언니의 뒤를 쫓아가서 언니의 흉내를 냅니다. 하지만 그녀가 흥미로운 것을 발견하면, 그녀는 그것에 집착하게 되고 집에 가는 길이나 시간을 잊어버리게 되어 그녀의 언니를 화나게 합니다.'
    ]

    movie_list = [
        '하울의 움직이는 성',
        '센과 치히로의 행방불명',
        '천공의 성 라퓨타',
        '반딧불이의 묘',
        '모노노케 히메',
        '하울의 움직이는 성',
        '모노노케 히메',
        '마녀 배달부 키키',
        '센과 치히로의 행방불명',
        '벼랑 위의 포뇨',
        '마녀 배달부 키키',
        '천공의 성 라퓨타',
        '모노노케 히메',
        '마녀 배달부 키키',
        '이웃집 토토로',
        '이웃집 토토로'
    ]

    image_list = [
        'https://static.wikia.nocookie.net/studio-ghibli/images/0/01/Mei_Kusakabe.jpg/revision/latest?cb=20181012193530',
        'https://static.wikia.nocookie.net/studio-ghibli/images/8/89/Haku-2.png/revision/latest?cb=20201008131345',
        'https://static.wikia.nocookie.net/studio-ghibli/images/7/7a/Castle-7.png/revision/latest?cb=20180429093339',
        'https://static.wikia.nocookie.net/studio-ghibli/images/2/21/Seita_Yokokawa.jpg/revision/latest?cb=20210215103515',
        'https://static.wikia.nocookie.net/studio-ghibli/images/3/3f/San.jpg/revision/latest/top-crop/width/360/height/450?cb=20210214204849',
        'https://i.pinimg.com/originals/37/bf/f9/37bff986a60b0c0837cf9f1a10d0f412.jpg',
        'https://static.wikia.nocookie.net/studio-ghibli/images/4/49/Ashitaka.jpg/revision/latest?cb=20220118140313',
        'https://static.wikia.nocookie.net/studio-ghibli/images/6/6f/Tombo.jpg/revision/latest/top-crop/width/360/height/450?cb=20210214130031',
        'https://static.wikia.nocookie.net/studio-ghibli/images/8/8e/Chihiro_Ogino.jpg/revision/latest?cb=20210214130251',
        'https://static.wikia.nocookie.net/studio-ghibli/images/b/bc/Brunhilda.png/revision/latest/top-crop/width/360/height/450?cb=20201016144049',
        'https://static.wikia.nocookie.net/studio-ghibli/images/b/b4/Jiji.jpg/revision/latest/top-crop/width/360/height/450?cb=20210218143145',
        'https://static.wikia.nocookie.net/disney/images/c/c3/5688-2094236141.jpg/revision/latest?cb=20140915192650',
        'https://static.wikia.nocookie.net/studio-ghibli/images/5/53/Eboshi.jpg/revision/latest/top-crop/width/360/height/450?cb=20220118140456',
        'https://static.wikia.nocookie.net/studio-ghibli/images/5/59/Kiki.jpg/revision/latest/top-crop/width/360/height/450?cb=20210214125850',
        'https://static.wikia.nocookie.net/studio-ghibli/images/f/f2/Satsuki_Kusakabe.jpg/revision/latest?cb=20210215103238',
        'https://static.wikia.nocookie.net/studio-ghibli/images/0/01/Mei_Kusakabe.jpg/revision/latest?cb=20181012193530'
    ]

    for item in zip(name_list, MBTI_list, info_list, movie_list, image_list):
        Character(
            name = item[0],
            MBTI = item[1],
            info = item[2],
            movie = item[3],
            image = item[4]
        ).save()

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
    character_info_save()



