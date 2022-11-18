const commentUpdateWrap = document.querySelector('.comment-update-wrap');
window.addEventListener('load', () => {
  commentUpdateWrap.style.height = `${window.innerHeight - 40}px`;
})

// 유저가 입력한 글자수를 보여주는 함수
const commentTextarea = document.querySelector('#id_content');
const contentCount = document.querySelector('.content__count');
contentCount.innerText = `${commentTextarea.value.length} / 500`
commentTextarea.addEventListener('keyup', () => {
  contentCount.innerText = `${commentTextarea.value.length} / 500`
  
})