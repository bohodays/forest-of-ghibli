const oldPasswordInput = document.querySelector('#id_old_password');
const oldPasswordLabel = document.querySelector('.old_password__label');
const oldPasswordInputWrap = document.querySelector('.old_password__label > div');
oldPasswordInput.addEventListener('focus', () => {
  oldPasswordLabel.style.transform = 'translateY(-30px)';
  oldPasswordInputWrap.style.color = '#3566b8';
})

oldPasswordInput.addEventListener('blur', () => {
  if (oldPasswordInput.value === '') {
    oldPasswordLabel.style.transform = 'translateY(0px)';
    oldPasswordInputWrap.style.color = '#000000';
  }
})

const newPasswordInput = document.querySelector('#id_new_password1');
const newPasswordLabel = document.querySelector('.new_password1__label');
const newPasswordInputWrap = document.querySelector('.new_password1__label > div');
newPasswordInput.addEventListener('focus', () => {
  newPasswordLabel.style.transform = 'translateY(-30px)';
  newPasswordInputWrap.style.color = '#3566b8';
})

newPasswordInput.addEventListener('blur', () => {
  if (newPasswordInput.value === '') {
    newPasswordLabel.style.transform = 'translateY(0px)';
    newPasswordInputWrap.style.color = '#000000';
  }
})

const newPassword2Input = document.querySelector('#id_new_password2');
const newPassword2Label = document.querySelector('.new_password2__label');
const newPassword2InputWrap = document.querySelector('.new_password2__label > div');
newPassword2Input.addEventListener('focus', () => {
  newPassword2Label.style.transform = 'translateY(-30px)';
  newPassword2InputWrap.style.color = '#3566b8';
})

newPassword2Input.addEventListener('blur', () => {
  if (newPassword2Input.value === '') {
    newPassword2Label.style.transform = 'translateY(0px)';
    newPassword2InputWrap.style.color = '#000000';
  }
})

const submitBtn = document.querySelector('.submit__button');
const inputs = [oldPasswordInput, newPasswordInput, newPassword2Input];
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
      input.parentNode.previousElementSibling.style.color = '#3566b8';
    }
  })
})


oldPasswordInput.addEventListener('keyup', (event) => {
  const styleColorCheck = oldPasswordInput.parentNode.previousElementSibling.style.color;
  if (styleColorCheck === 'rgb(0, 0, 0)') {
    event.target.parentNode.previousElementSibling.style.transform = 'translateY(-30px)';
    event.target.parentNode.previousElementSibling.style.color = '#3566b8';
  }
})

// 비밀번호 확인이 비밀번호와 일치하지 않으면 메세지 보여주는 함수
const passwordSameMessage = document.querySelector('.password__same');
newPassword2Input.addEventListener('keyup', () => {
  if (newPassword2Input.value !== '') {
    if (newPasswordInput.value !== newPassword2Input.value) {
      passwordSameMessage.innerText = '비밀번호가 일치하지 않습니다.';
    } else {
      passwordSameMessage.innerText = '';
    }
  }
})