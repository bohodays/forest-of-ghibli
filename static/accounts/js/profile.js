const section = document.querySelector('section');
const profileInfo = document.querySelector('.profile__info');
window.addEventListener('load', () => {
  if (section.getBoundingClientRect().height < window.innerHeight) {
    // section.style.height = `${window.innerHeight}px`;
    profileInfo.style.paddingBottom = `${window.innerHeight / 2}px`;
  }
})