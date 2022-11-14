const userNameInput = document.querySelector('#id_username');
const userNameLabel = document.querySelector('.username__label');
const userNameInputWrap = document.querySelector('.username__label > div');
userNameInput.addEventListener('focus', () => {
  userNameLabel.style.transform = 'translateY(-30px)';
  userNameInputWrap.style.color = 'rgb(130 193 237)';
})

userNameInput.addEventListener('blur', () => {
  if (userNameInput.value === '') {
    userNameLabel.style.transform = 'translateY(0px)';
    userNameInputWrap.style.color = '#000000';
  }
})

const passwordInput = document.querySelector('#id_password');
const passwordLabel = document.querySelector('.password__label');
const passwordInputWrap = document.querySelector('.password__label > div');
passwordInput.addEventListener('focus', () => {
  passwordLabel.style.transform = 'translateY(-30px)';
  passwordInputWrap.style.color = 'rgb(130 193 237)';
})

passwordInput.addEventListener('blur', () => {
  if (passwordInput.value === '') {
    passwordLabel.style.transform = 'translateY(0px)';
    passwordInputWrap.style.color = '#000000';
  }
})

const submitBtn = document.querySelector('.submit__button');
const inputs = [userNameInput, passwordInput];
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
      input.parentNode.previousElementSibling.style.color = 'rgb(130 193 237)';
    }
  })
})


userNameInput.addEventListener('keyup', (event) => {
  const styleColorCheck = userNameInput.parentNode.previousElementSibling.style.color;
  if (styleColorCheck === 'rgb(0, 0, 0)') {
    event.target.parentNode.previousElementSibling.style.transform = 'translateY(-30px)';
    event.target.parentNode.previousElementSibling.style.color = 'rgb(130 193 237)';
  }
})