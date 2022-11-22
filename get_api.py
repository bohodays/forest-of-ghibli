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
        '캘시퍼',
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
    'ISFJ 유형의 사람들은 내성적이고 평범해 보이지만, 근면하고 헌신적인 성격으로 주변 사람들에 대한 깊은 책임감을 가지고 있습니다. 또한  차분한 성격인 동시에 대인 관계 능력도 뛰어나기 때문에 주변 인물과 깊은 관계를 맺습니다. 이러한 성격은 소피가 스스로 하울의 성을 청소하는 모습이나, 성에 살고 있는 켈시퍼와 마르클 까지 세심하게 챙기는 모습을 통해 알 수 있습니다.',
    'INFJ 유형의 사람들은 대체적으로 다른 사람을 돕는 일을 인생의 사명으로 생각하며 정의를 추구할 방법을 찾습니다. 이들은 사회의 본질적인 문제를 해결하고 부당함을 해소하려는 열망이 있습니다. 하쿠가 치히로를 대하는 모습을 보면 이러한 성격을 살펴볼 수 있습니다. 유바바의 수하들을 보살피는 와중에도, 부모가 돼지로 변해버린 센을 유바바의 성에서 무사히 빠져 나갈 수 있게 돕습니다.',
    'INTJ 유형의 사람들은 보통 독립성이 매우 강하며 혼자서 행동하는 일을 두려워하지 않습니다. 또한 일반적으로 다른 사람의 의견을 묻지 않고 결정을 내리는 편입니다. 그래서 무신경한 사람처럼 보일 수도 있습니다. 시타는 영화에서 과묵하고 낯을 많이 가립니다. 그리고 혼자 살아온 시간이 길기 때문에, 생활력이 강한 인물입니다. 그래서 주변 인물들과 친밀한 관계를 잘 맺지 못하고 무심해 보입니다. 하지만 그녀가 영화 후반부에 자신을 지켜준 사람을 걱정하고, 불에 타고 있는 로봇의 손을 잡아주는 장면을 보면 꽤 인정이 많은 캐릭터인 것을 알 수 있습니다.',
    'ISTJ 유형의 사람들은 진실하게 행동하는 자신의 모습에서 자부심을 느끼며, 자기 생각을 솔직하게 이야기하고 어떤 것에 헌신하기로 한 경우 최선을 다합니다. 현실주의자라고도 불리는 이 성격은, 책임감이 강하여 다른 사람의 몫까지 짊어지려고 합니다. 세이타는 영화에서 하나뿐은 여동생을  혼자 돌봅니다. 가난한 와중에도 여동생의 건강과 안전을  항상 최우선으로 생각하면서 하루 하루를 버텨나가는 모습을 통해 그가 이 유형의 성격이라는 것을 알 수 있습니다.',
    'ISTP 유형의 사람들은 일반적으로, 고집이 세고 주관이 뚜렷한 편입니다. 그리고 관심 있는 분야가 아니라면 쳐다 보지도 않는 성격을 가지고 있습니다. 산은 인간이지만 인간 세계를 혐오하는 숲의 늑대에 의해 길러진 탓에 사회성이 좋지 않습니다. 그래서 고집이 세고 용감하고, 방어적이며 숲을 보호하는 것 이외에는 관심이 없습니다. 하지만 아시타카를 만나면서 이러한 그녀도 조금씩 변하기 시작합니다.',
    'ISFP 유형의 사람들은 다른 유형들에 비해 각자가 독특한 개성을 가지고 있습니다. 대부분 유연한 방식으로 삶에 적응하며 일부 성격과 달리 엄격한 일정과 계획을 따르는 일을 좋아하지 않습니다. 항상 어디론가 돌아다니는 하울과 어질러진 그의 성을 보면 자유로운 성격을 가지고 있다는 것을 알 수 있습니다. 이외에도, 불편한 상황이 오거나 무언가를 해야만하는 상황이 오면 피하는 경향이 있습니다.',
    'INFP 유형의 사람들은 에너지와 열정이 넘치는 마음을 지닌 성격입니다. 또한 이상주의적이고 공감 능력이 높으며, 깊고 의미 있는 관계를 원하고 다른 사람을 도와야 한다는 사명감을 느끼곤 합니다.  아시타카는 굉장히 도덕적인 마음의 소유자로, 어려움에 처한 사람은 내버려 두지 않고, 자신의 행동이 사람들의 미움을 사더라도 올곧은 자세와 마음을 유지해서 모두가 평화롭고 서로 공존할 수 있도록 노력합니다.',
    'INTP 유형의 사람들은 자신의 독특한 관점과 활기 넘치는 지성에 자부심을 느끼며, 우주의 미스터리에 대해 깊이 생각하곤 합니다. 상당히 희귀한 성격이지만 뛰어난 창의성과 독창성으로 많은 사람 사이에서 존재감을 드러내곤 합니다. 톰보는 하늘을 나는 것에 대해 관심이 많은 인물입니다. 톰보의 눈에 하늘을 날아 다니는 키키는 관심이 생길 수 밖에 없기 때문에 톰보는 키키에게 다가갑니다.  키키와 친해진 톰보는 키키를 위해 프로펠러가 달린 자전거를 발명해 키키와 함께 하늘을 날게 됩니다.',
    'ENFP 유형의 사람들은 대부분 자유로운 영혼이라고 알려져 있습니다. 낙관적인 삶의 태도로 즐거움을 쫓는 경향이 있지만, 한편으로는 다른사람과 감정적으로 깊고 의미있는 관계를 맺고 싶어 합니다. 또한 모든 사물과 사람이 연결되어 있다고 믿으며 이러한 관계에 대한 통찰을 추구합니다. 치히로는 비록 부모님이 돼지로 변해 유바바의 온천에 갇히게 되었지만, 그 안에서 만난 사람들과 깊은 관계를 맺습니다. 하쿠, 거미 할아버지, 그리고 치히로가 인간 인걸 알면서도 보살펴준 온천 종업원 린을 소중하게 여기는 것을 보면 치히로가 인정이 많은 것을 알 수 있습니다.',
    "'연예인'이라는 별명이 있는 ESFP 유형의 사람들은 매일을 즐겁게 살려고 하고 남들도 그렇길 바랍니다. 또한 관찰력이 뛰어나 다른 사람의 감정을 빠르게 알아챌 수 있습니다.  이러한 성격은 포뇨에게서도  잘 드러납니다. 포뇨는 항상 활기찬 인물로, 주인공 소스케의 집에 긍정적인 영향을 끼칩니다. 그러면서도 주변인물의 마음을 잘 읽어내고 배려하는 마음을 지녔습니다.",
    'ENTP의 성격을 가진 사람들은 똑똑하고 대담한 성격으로, 현재 상황에 이의를 제기하는데 거리낌이 없습니다. 하지만 악의를 가진 것은 아닙니다. 그저 논쟁에서 즐거움을 찾는 성향이 있을 뿐입니다. 켈시퍼는 하울의 성의 동력원이자 성의 관리자 입니다. 생긴 거만 봐도 알 수 있듯이 틱틱 대는 성격을 가지고 있으며 심술 쟁이 입니다. 주변 인물들에게 자주 투덜대지만 본성은 착하며 성 안의 식구들을 소중히 여깁니다.',
    'ESTP 성격의 사람들은 주변 사람들에게 영향력을 행사하곤 합니다. 또한 지능이 높고 활기찬 대화를 유지할 수 있는 성격임과 동시에 현실적인 주제에 대해 이야기하고 직접 행동하는 것을 좋아합니다. 돌라는 리더쉽이 있고, 타고난 해결사로써 문제를 해결하는 능력이 뛰어납니다. 이러한 성격은 비행선 ‘타이거 모스’를 타고 다니는 해적단 도라 일가의 두목으로 나오는 모습과 시타와 파즈를 도와주는 모습에서 살펴볼 수 있습니다.',
    'ESTJ 유형의 사람들은 전통과 질서를 중시하는 성격으로, 자신이 생각하는 옳고 그름과 사회적 기준에 따라 가족과 공동체가 화합 할 수 있도록 노력합니다. 이들은 정직, 헌신과 존엄성을 중시하며, 어려운 길을 기꺼이 앞장서고 다른 사람들에게 명확한 조언과 지도를 제공합니다. 에보시는 리더십과 안정성을 중시하는 인물로 조직을 주도해나가는 지도력이 있습니다. 또한 긴박한 상황 속에서도 침착함을 유지합니다. 이러한 성격은 에보시가 타타라 마을의 지도자이자 수장으로써 강인하고 당당한 모습으로 외부 세력에 대항해 마을을 지키는 장면을 통해 알 수 있습니다.',
    'ENFJ의 유형의 사람들은 다른 사람과 주변 세상에 긍정적인 영향력을 발휘하기 위해 최선을 다하며, 다른 사람이 더 나은 삶을 살도록 도우려고 합니다. 키키는 마음이 착하고 상냥하며 타인의 관심사에 귀 기울이고 그들을 배려합니다. 또한 책임감과 인내심이 강합니다. 이러한 성격은 키키가 코리코마을에 정착하며 점차 고객들과 새로운 친구들을 사귀게 되고 마지막에는 마을 모두의 사랑을 받는 모습과 마녀가 되기 위해 1년 동안 집을 떠나 훈련받는 모습에서 알 수 있습니다.',
    'ENTJ 유형의 사람들은 일반적으로 자신감 있고, 리더로서의 자질이 있습니다. 그리고 감정을 드러내는 것에 익숙하지 않습니다. 사츠키는 어리지만 동생에게 어른스러워 보이기 위해 노력하는 인물입니다. 그래서 속이 깊고 어른스러운 성격을 가지고 있으며, 감정을 겉으로 드러내지 않으려고 노력합니다. 하지만 영화가 끝날 무렵 할머니 앞에서 슬픔을 드러내는 모습에서 마냥 어른스럽기만 한 것은 아니라는 것을 볼 수 있습니다.',
    'ESFJ 유형의 성격을 가진 사람들에게 인생이란 남과 함께 나눌 때 가장 즐거운 것입니다. 이들은 여러 사람을 하나로 모으는 역할을 하며 솔직하고 개방적인 태도로 친구와 연인과 이웃을 대합니다. 메이는 솔직하고 개방적인 태도로 주변인들을 대합니다. 이타적인 성격으로, 친절하며 주변인에 대한 관심이 많습니다. 이러한 성격은 메이가 처음 토토로를 만나고 금방 친해지는 모습에서 살펴볼 수 있습니다.'
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
        '하울의 움직이는 성',
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


        'https://i.pinimg.com/564x/ec/cc/30/eccc301ce368263b76d672f575faeea0.jpg',
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



