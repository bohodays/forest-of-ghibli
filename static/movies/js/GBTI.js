// 전체 질문 길이 ( 추후에 질문 개수 변화가 생길 수도 있어서)
const qLength = 17
const ENERGY = 5  //(I,E)
const PERCEPTION = 9 //(S,N)
const DECISION = 13  // (T,F)
const LIFESTYLE = 17 //(J,P)

// 길이가 16인 배열 만들기 
let answerList = [0]

// MBTI 결과를 저장하는 함수
const getMBTI = () => {
  let energy=0
  let perception = 0
  let decision = 0
  let lifestyle = 0

  for (let j = 1; j <qLength; j++){
    if ( j>0 && j < ENERGY){
      energy +=  answerList[j]
    }else if( j>= ENERGY && j < PERCEPTION){
      perception += answerList[j]
    }else if( j>= PERCEPTION && j < DECISION){
      decision += answerList[j]
    }else if( j>= DECISION){
      lifestyle += answerList[j]
    }
  }
  let gbti = ''
  if (energy <= 10){
    gbti += 'I'
  }else{
    gbti += 'E'
  }

  if (perception <= 10){
    gbti += 'S'
  }else{
    gbti += 'N'
  }

  if (decision <= 10){
    gbti += 'T'
  }else{
    gbti += 'F'
  }

  if (lifestyle <= 10){
    gbti += 'P'
  }else{
    gbti += 'J'
  }

  console.log(gbti);

  const formInput = document.querySelector('#id_GBTI');
  formInput.innerText = `${gbti}`
}

const selectItem = (item, select,i) => {
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
    let ansBtn = document.getElementsByClassName(select)
    // 클릭한 버튼의 value 저장하기
    let ans = ansBtn[0].dataset.value
    console.log(ans);
    // 선택한 버튼의 인덱스에 값 넣기
    answerList[i] = parseInt(ans)
    console.log('list:', answerList);
    
    const submitBtn = document.querySelector('.submit');
    const cautionMessage = document.querySelector('.caution-message');
    for (let i = 1; i < 17; i++) {
      if (answerList[i] === undefined) {
        submitBtn.classList.add('block')
        submitBtn.style.backgroundColor = '#ced4da';
        cautionMessage.innerText = '모든 질문에 응답해주시기 바랍니다.'
        cautionMessage.style.color = '#dc3545';
        
        console.log(11);
        break
      } else {
        console.log(22);
        submitBtn.classList.remove('block');
        submitBtn.style.backgroundColor = '#212529';
        cautionMessage.innerText = '결과를 확인해보세요.';
        cautionMessage.style.color = '#198754';
      }
    }
    if(answerList.length === 17){
      getMBTI();
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

for (let i = 1; i < qLength; i++) {
  let number = document.querySelectorAll(`.numbers${i}__number`)
  number.forEach((item) => {
    selectItem(item, `select${i}`,i)
    
  })

  number.forEach((item) => {
    hoverBackground(item, `select${i}`)
  })
}

window.addEventListener('load', () => {
  const submitBtn = document.querySelector('.submit');
  const cautionMessage = document.querySelector('.caution-message');
  cautionMessage.style.opacity = '1';
  submitBtn.classList.add('block')
})