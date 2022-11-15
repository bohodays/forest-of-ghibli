const exclamationImg = document.querySelector('.exclamation__img');
const exclamationComments = document.querySelector('.comments__visible');


exclamationImg.addEventListener('mouseenter', () => {
  exclamationComments.classList.remove('comments__visible');
})


exclamationImg.addEventListener('mouseout', () => {
  exclamationComments.classList.add('comments__visible');
})


const nickNameInput = document.querySelector('#id_nickName');
const nickNameLabel = document.querySelector('.nickname__label');
const nickNameLabelWrap = document.querySelector('.nickname__label > div');
nickNameInput.addEventListener('focus', () => {
  nickNameLabel.style.transform = 'translateY(-30px)';
  nickNameLabelWrap.style.color = 'rgb(146 96 58)';
})

nickNameInput.addEventListener('blur', () => {
  if (nickNameInput.value === '') {
    nickNameLabel.style.transform = 'translateY(0px)';
    nickNameLabelWrap.style.color = '#000000';
  }
})


const userNameInput = document.querySelector('#id_username');
const userNameLabel = document.querySelector('.username__label');
const userNameInputWrap = document.querySelector('.username__label > div');
userNameInput.addEventListener('focus', () => {
  userNameLabel.style.transform = 'translateY(-30px)';
  userNameInputWrap.style.color = 'rgb(146 96 58)';
})

userNameInput.addEventListener('blur', () => {
  if (userNameInput.value === '') {
    userNameLabel.style.transform = 'translateY(0px)';
    userNameInputWrap.style.color = '#000000';
  }
})

const passwordInput = document.querySelector('#id_password1');
const passwordLabel = document.querySelector('.password__label');
const passwordInputWrap = document.querySelector('.password__label > div');
passwordInput.addEventListener('focus', () => {
  passwordLabel.style.transform = 'translateY(-30px)';
  passwordInputWrap.style.color = 'rgb(146 96 58)';
})

passwordInput.addEventListener('blur', () => {
  if (passwordInput.value === '') {
    passwordLabel.style.transform = 'translateY(0px)';
    passwordInputWrap.style.color = '#000000';
  }
})

const password2Input = document.querySelector('#id_password2');
const password2Label = document.querySelector('.password2__label');
const password2InputWrap = document.querySelector('.password2__label > div');
password2Input.addEventListener('focus', () => {
  password2Label.style.transform = 'translateY(-30px)';
  password2InputWrap.style.color = 'rgb(146 96 58)';
})

password2Input.addEventListener('blur', () => {
  if (password2Input.value === '') {
    password2Label.style.transform = 'translateY(0px)';
    password2InputWrap.style.color = '#000000';
  }
})


const submitBtn = document.querySelector('.submit__button');
const inputs = [nickNameInput, userNameInput, passwordInput,  password2Input];
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
      // 라벨을 가리킴 (부모노드의 이전형제 요소)
      input.parentNode.previousElementSibling.style.transform = 'translateY(0px)';
      input.parentNode.previousElementSibling.style.color = '#000000';
    } else {
      input.parentNode.previousElementSibling.style.transform = 'translateY(-30px)';
      input.parentNode.previousElementSibling.style.color = 'rgb(146 96 58)';
    }
  })
})

userNameInput.addEventListener('keyup', (event) => {
  const styleColorCheck = userNameInput.parentNode.previousElementSibling.style.color;
  if (styleColorCheck === 'rgb(0, 0, 0)') {
    event.target.parentNode.previousElementSibling.style.transform = 'translateY(-30px)';
    event.target.parentNode.previousElementSibling.style.color = 'rgb(146 96 58)';
  }
})
