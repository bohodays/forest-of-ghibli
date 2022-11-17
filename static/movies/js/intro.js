let mouseCursor = document.querySelector('.cursor');

window.addEventListener('mousemove', cursor);

function cursor(event) {
  mouseCursor.style.top = event.pageY-40 + 'px';
  mouseCursor.style.left = event.pageX-40 + 'px';
}

document.addEventListener('DOMContentLoaded', () => {
  window.setTimeout(() => {
    document.body.classList.remove('fade');
  });
});


document.addEventListener('click', () => {
  document.body.classList.add('fade');
  window.setTimeout(() => {
    window.location.href = 'http://127.0.0.1:8000/movies/main';
  }, 1000)
})

document.addEventListener('keydown', () => {
  document.body.classList.add('fade');
  window.setTimeout(() => {
    window.location.href = 'http://127.0.0.1:8000/movies/main';
  }, 1000)
})



