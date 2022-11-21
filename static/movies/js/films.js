const newestBtn = document.querySelector('.newest-btn');
const newestContainer = document.querySelector('.container-newest');
const oldestContainer = document.querySelector('.container-oldest');
let flag = false;
newestBtn.addEventListener('click', () => {
  if (flag === false) {
    newestBtn.style.backgroundColor = '#77aaff';
    newestContainer.style.display = 'flex';
    oldestContainer.style.display = 'none';
    flag = true;
  } else {
    newestBtn.style.backgroundColor = '#ced4da';
    newestContainer.style.display = 'none';
    oldestContainer.style.display = 'flex';
    flag = false;
  }
})