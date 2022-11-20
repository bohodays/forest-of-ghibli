const deployURL = 'http://127.0.0.1:8000/';

// 스크롤을 내리면 navbar 흐리게 만들기
const navbar = document.querySelector('#navbar');
document.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('blurred');
  } else {
    navbar.classList.remove('blurred');
  }
})

// 스크롤을 내리면 맨 위로 갈 수 있는 화살표 버튼 활성화시키기
const arrowUp = document.querySelector('.arrow-up');
document.addEventListener('scroll', () => {
  if (window.scrollY > 400) {
    arrowUp.classList.add('visible')
  } else {
    arrowUp.classList.remove('visible');
  }
});

arrowUp.addEventListener('click', () => {
  document.body.scrollIntoView({ behavior:'smooth' });
})

const searchMark = document.querySelector('.fa-magnifying-glass');
const xMark = document.querySelector('.fa-xmark');
let menuItems = document.querySelectorAll('.menu__item');
const navbarMenu = document.querySelector('.navbar__menu');
const hiddenMenus = document.querySelectorAll('.menu__hidden');


searchMark.addEventListener('click', () => {
  menuItems.forEach((item) => {
    item.classList.add('menu-invisible');
    item.style.transform = 'translateY(-10px)';
  })
  
  hiddenMenus.forEach((itme) => {
    itme.style.opacity = '1';
    itme.style.display = 'block';
    itme.style.pointerEvents = 'all';
  })
  
  searchMark.style.transform = 'translate(-370px, 2px)';
  // createSearchInput();

  recommendWrap.style.display = 'block';
})

xMark.addEventListener('click', () => {
  menuItems.forEach((item) => {
    item.classList.remove('menu-invisible');
    item.style.transform = 'translateY(0px)';
  })

  hiddenMenus.forEach((itme) => {
    itme.style.opacity = '0';
    itme.style.display = 'absolute';
    itme.style.pointerEvents = 'none';
  })

  searchMark.style.transform = 'translate(0px, 0px)';
  recommendWrap.style.display = 'none';
})

// 메인 화면을 유저의 브라우저 크기에 맞추기
const mainWrap = document.querySelector('.main__wrap')
window.addEventListener('load', () => {
  mainWrap.style.height = `${window.innerHeight}px`;
  // mainImg.style.width = `${window.innerWidth}px`;
})


// 영화 검색 기능 구현
const searchInput = document.querySelector('.search__input');
const recommendWrap = document.querySelector('.recommend-search-wrap');
searchInput.addEventListener('keyup', (event) => {
  const movieCode = [
    '천공의 성 라퓨타',
    '바람계곡의 나우시카',
    '반딧불이의 묘',
    '이웃집 토토로',
    '마녀 배달부 키키',
    '추억은 방울방울',
    '붉은 돼지',
    '바다가 들린다',
    '폼포코 너구리 대작전',
    '귀를 기울이면',
    '모노노케 히메',
    '이웃집 야마다군',
    '센과 치히로의 행방불명',
    '하울의 움직이는 성',
    '고양이의 보은',
    '게드전기: 어스시의 전설',
    '벼랑 위의 포뇨',
    '마루 밑 아리에티',
    '코쿠리코 언덕에서',
    '가구야공주 이야기',
    '추억의 마니',
    '붉은 거북',
    '아야와 마녀'
  ]
  
  let searchItems = new Set;

  // 유저가 엔터를 눌렀을 때
  if (event.code === 'Enter' || event.code === 'NumpadEnter') {
    // 유저가 입력한 영화 제목의 지브리 영화가 있다면 그 영화의 디테일 페이지로 이동
    if (movieCode.includes(searchInput.value)) {
      window.location.href = `${deployURL}movies/${movieCode.indexOf(searchInput.value) + 1}/`
    // 유저가 입력한 영화 제목의 지브리 영화가 없다면 모달 실행
    } else {
      const cc = document.querySelector('.cc');
      const modalContent = document.querySelector('.modal-body');
      modalContent.innerText = `"${searchInput.value}" 은/는 지브리 영화가 아닙니다. 확인 부탁드립니다.`;
      cc.click();
    }

  // 백스페이스 키를 눌렀을 경우 추천 검색어를 위한 배열 초기화
  } else if (event.code === 'backspace') {
    searchItems = []
  // 그 외 다른 키를 입력했을 경우
  } else {
    // 만약 추천 검색어가 비어있다면
    if (!recommendWrap.firstElementChild) {
      // 유저가 2글자 이상 입력한 순간부터 지브리 영화를 순회하면서 유저가 입력한 지브리 영화가 있는지 확인
      movieCode.forEach((movie) => {
        for (let i=2; i<20; i++) {
          // 유저가 입력한 지브리 영화가 있다면 추천 검색어를 위한 집합에 추가
          if (movie.slice(0,i) === searchInput.value) {
            searchItems.add(movie)
          }
        }
      })
    }
  }

  // 만약 추천 검색어가 비어있지 않다면
  if (!recommendWrap.firstElementChild) {
    // 추천 검색어를 순회하면서 유저에게 보이게 하기
    searchItems.forEach((item) => {
      recommendWrap.innerHTML += `
      <p class="recommend-search">${item}</p>
      `;
      recommendWrap.style.padding = '4px 6px';

      const recommendSearch = document.querySelectorAll('.recommend-search');
      recommendSearch.forEach((item) => {
        item.addEventListener('click', (event) => {
          console.log(event.target);
          window.location.href = `${deployURL}movies/${movieCode.indexOf(event.target.innerText) + 1}/`
        })
      })
    })
  // 추천 검색어가 비어있다면 기존의 요소 제거
  } else {
    recommendWrap.style.padding = '0px';
    recommendWrap.innerHTML = '';
  }

})


// 프로필 사진이나 닉네임 누르면 프로필 정보와 변경하기 보이게 하기
const profileContainer = document.querySelector('.profile__container');
const profileInfoWrap = document.querySelector('.profile-info-wrap');
profileContainer.addEventListener('click', () => {
  profileInfoWrap.classList.toggle('invisible');
})