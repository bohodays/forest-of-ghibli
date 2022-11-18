const selectItem = (item, select) => {
  item.addEventListener('click', (event) => {
    const target = event.target;
    // 선택된 버튼의 개수 확인
    const selectedCnt = document.getElementsByClassName(select).length;
    // 이미 선택된 버튼이 있다면
    if (selectedCnt === 1) {
      // 이미 선택된 버튼을 변수로 지정
      const selectedBtn = document.querySelector(`.${select}`);
      // 지정된 변수의 클래스 제거
      selectedBtn.classList.remove(select);
      selectedBtn.style.backgroundColor = 'rgba(124, 135, 152, 0.2)';
      // 클릭한 타겟에 클래스 추가
      target.classList.add(select);
      if (target.classList.contains('agree')) {
        target.style.backgroundColor = '#94bbe9';
      } else if (target.classList.contains('disagree')) {
        target.style.backgroundColor = '#eeaeca';
      }
      // 선택된 버튼이 없다면
    } else {
    // 클릭한 타겟에 클래스 추가
      target.classList.add(select);
      if (target.classList.contains('agree')) {
        target.style.backgroundColor = '#94bbe9';
      } else if (target.classList.contains('disagree')) {
        target.style.backgroundColor = '#eeaeca';
      }
    }
})
}


const hoverBackground = (item, select) => {
  item.addEventListener('mouseover', () => {
    if (item.classList.contains('agree') && !item.classList.contains(select)) {
      item.style.backgroundColor = '#94bbe9';
    } else if (item.classList.contains('disagree') && !item.classList.contains(select)) {
      item.style.backgroundColor = '#eeaeca';
    }
  })
  item.addEventListener('mouseout', () => {
    if (item.classList.contains('agree') && !item.classList.contains(select)) {
      item.style.backgroundColor = 'rgba(124, 135, 152, 0.2)';
    } else if (item.classList.contains('disagree') && !item.classList.contains(select)) {
      item.style.backgroundColor = 'rgba(124, 135, 152, 0.2)';
    }
  })
}


for (let i = 1; i < 17; i++) {
  let number = document.querySelectorAll(`.numbers${i}__number`)

  number.forEach((item) => {
    selectItem(item, `select${i}`)
  })

  number.forEach((item) => {
    hoverBackground(item, `select${i}`)
  })
}





