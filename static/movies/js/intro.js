let mouseCursor = document.querySelector('.cursor');

window.addEventListener('mousemove', cursor);

function cursor(event) {
  mouseCursor.style.top = event.pageY-40 + 'px';
  mouseCursor.style.left = event.pageX-40 + 'px';
}

