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