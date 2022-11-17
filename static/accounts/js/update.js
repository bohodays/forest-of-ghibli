const nickNameInput = document.querySelector('#id_nickName');
const nickNameLabel = document.querySelector('.nickname__label');
const nickNameLabelWrap = document.querySelector('.nickname__label > div');
nickNameInput.addEventListener('focus', () => {
  nickNameLabel.style.transform = 'translateY(-30px)';
  nickNameLabelWrap.style.color = '#f0b460';
})

nickNameInput.addEventListener('blur', () => {
  if (nickNameInput.value === '') {
    nickNameLabel.style.transform = 'translateY(0px)';
    nickNameLabelWrap.style.color = '#000000';
  }
})

const submitBtn = document.querySelector('.submit__button');
const inputs = [nickNameInput];
submitBtn.addEventListener('click', () => {
  inputs.forEach((input) => {
    if (input.value === '') {
      input.nextElementSibling.classList.remove('error__visible');
    } else {
      input.nextElementSibling.classList.add('error__visible');
    }
  })
})

window.addEventListener('load', () => {
  inputs.forEach((input) => {
    if (input.value === '') {
      // 라벨을 가리킴
      input.parentNode.previousElementSibling.style.transform = 'translateY(0px)';
      input.parentNode.previousElementSibling.style.color = '#000000';
    } else {
      input.parentNode.previousElementSibling.style.transform = 'translateY(-30px)';
      input.parentNode.previousElementSibling.style.color = '#f0b460';
    }
  })
})


nickNameInput.addEventListener('keyup', (event) => {
  const styleColorCheck = nickNameInput.parentNode.previousElementSibling.style.color;
  if (styleColorCheck === 'rgb(0, 0, 0)') {
    event.target.parentNode.previousElementSibling.style.transform = 'translateY(-30px)';
    event.target.parentNode.previousElementSibling.style.color = '#f0b460';
  }
})
