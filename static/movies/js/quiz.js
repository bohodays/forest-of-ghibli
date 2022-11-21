// 메인 화면을 유저의 브라우저 크기에 맞추기
const section = document.querySelector('section')
window.addEventListener('load', () => {
  section.style.height = `${window.innerHeight}px`;
})


const quizWrap = document.querySelector('.quiz-wrap'); 

// 장고의 quiz_result에 보낼 결과 array
let result = 0;

// 버튼을 클릭하면 백그라운드 컬러에 변화를 주어 유저가 선택한 것을 인지시키는 함수
const btnSelect = () => {
  const numberBtn = document.querySelectorAll('.number');
  numberBtn.forEach(btn => {
    btn.addEventListener('click', (event) => {
      const target = event.target
      // 선택된 버튼의 개수 확인
      const selectedCnt = document.getElementsByClassName('select').length;
      // 이미 선택된 버튼이 있다면
      if (selectedCnt === 1) {
        // 선택된 버튼을 변수로 지정
        const selectedBtn = document.querySelector('.select');
        // 선택된 버튼의 클래스 제거
        selectedBtn.classList.remove('select');
        // 클릭한 타겟에 클래스 추가
        target.classList.add('select');
      // 선택된 버튼이 없다면
      } else {
        // 클릭한 타겟에 클래스 추가
        target.classList.add('select');
      }})
    });
}


// 인트로에서 퀴즈 풀기 버튼을 누르면 인트로를 없애고 1단계 문제를 보여주는 코드
const moveTo1Btn = document.querySelector('.move-to-1');
const intro = document.querySelector('.intro');
moveTo1Btn.addEventListener('click', () => {
  section.style.height = '1300px';
  intro.remove()
  // 1단계 퀴즈 보여주기
  quizWrap.innerHTML += `
    <div class="no1">
      <h4 class="quiz__title no1__title">
        1. <하울의 움직이는 성>에서 하울은 소피가 청소한 욕실에서 목욕을 한 후 변한 무엇 때문에 소피에게 화를 냅니다.
        하울의 무엇이 변하여 소피에게 화를 냈을까요?
      </h4>
      <img class="quiz__img no1__img" src="https://w.namu.la/s/0603c54b54b7df773e079ed14448a130e63b0b07dc508a08a92c8ee079fefdb8fb0289c85bb1809c6f985dcfe0b8b386202f0d44b84f45d3eca7fc4f673f5ab40c6a7f5ce0b1779583f83c6588dc7212f08fda0de5ce31234e4ca975c612edaf" alt="">
      <div class="numbers">
        <div class="number-wrap d-flex">
          <button class="number" data-value="1">
            1
          </button>
          <p> 입술 색 </p>
        </div>
        <div class="number-wrap d-flex">
          <button class="number" data-value="2">
            2
          </button>
          <p> 머리카락 색 </p>
        </div>
        <div class="number-wrap d-flex">
          <button class="number" data-value="3">
            3
          </button>
          <p> 피부색 </p>
        </div>
        <div class="number-wrap d-flex">
          <button class="number" data-value="4">
            4
          </button>
          <p> 눈동자 색 </p>
        </div>
        <div class="number-wrap d-flex">
          <button class="number" data-value="5">
            5
          </button>
          <p> 손톱 색 </p>
        </div>
      </div>
      <p class="caution-message-mark"></p>
      <button class="next move-to-2">
        다음 문제
      </button>
    </div>
  `;
  btnSelect();
  moveTo2();

})


// 1단계에서 다음 문제 버튼을 누르면 1단계를 없애고 2단계 문제를 보여주는 함수
const moveTo2 = () => {
const moveTo2Btn = document.querySelector('.move-to-2');
const no1 = document.querySelector('.no1');
moveTo2Btn.addEventListener('click', () => {
  const selectedCnt = document.getElementsByClassName('select').length;
  if (selectedCnt === 0) {
    const cautionMessage = document.querySelector('.caution-message-mark');
    cautionMessage.innerText = '보기 중 하나를 선택하고 버튼을 눌러주세요.';
  } else {
    const selectNumber = document.querySelector('.select');
    if (Number(selectNumber.dataset.value) === 2) {
      result += 1;
    }
    console.log(result);
    no1.remove()
    // 2단계 퀴즈 보여주기
    quizWrap.innerHTML += `
      <div class="no2">
        <h4 class="quiz__title no2__title">
          2. <하울의 움직이는 성> 등장인물 중 황무지의 마녀는 하울의 무엇을 가지고 싶어 했나요?
        </h4>
        <img class="quiz__img no2__img" src="https://pbs.twimg.com/media/EEe7WfxU8AEdxRc.jpg" alt="">
        <div class="numbers">
          <div class="number-wrap d-flex">
            <button class="number" data-value="1">
              1
            </button>
            <p> 마음 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="2">
              2
            </button>
            <p> 심장 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="3">
              3
            </button>
            <p> 사랑 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="4">
              4
            </button>
            <p> 신장 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="5">
              5
            </button>
            <p> 옷 </p>
          </div>
        </div>
        <p class="caution-message-mark"></p>
        <button class="next move-to-3">
          다음 문제
        </button>
      </div>
    `;
    btnSelect();
    moveTo3();
  }
})
}


// 2단계에서 다음 문제 버튼을 누르면 2단계를 없애고 3단계 문제를 보여주는 함수
const moveTo3 = () => {
  const moveTo3Btn = document.querySelector('.move-to-3');
  const no2 = document.querySelector('.no2');
  moveTo3Btn.addEventListener('click', () => {
  const selectedCnt = document.getElementsByClassName('select').length;
  if (selectedCnt === 0) {
    const cautionMessage = document.querySelector('.caution-message-mark');
    cautionMessage.innerText = '보기 중 하나를 선택하고 버튼을 눌러주세요.';
  } else {
    const selectNumber = document.querySelector('.select');
    if (Number(selectNumber.dataset.value) === 2) {
      result += 1;
    }
    console.log(result);
    no2.remove()
    // 3단계 퀴즈 보여주기
    quizWrap.innerHTML += `
      <div class="no3">
        <h4 class="quiz__title no3__title">
          3. <하울의 움직이는 성> 등장인물 중 얼굴이 무로 만들어진 허수아비가 등장하는데, 그의 정체는 무엇인가요?
        </h4>
        <img class="quiz__img no3__img" src="https://w.namu.la/s/6fe26432f51d7d28de8f6fb678d4e83ceea30cd0594a8f0491615eab9016ba383c45363bd834d2356676245f871bdbacd42f6719c29883eac69cf167f0232a794e44ff674b940454ee6822491d9f8417431a7985e82285408c0e40ef687ef714" alt="">
        <div class="numbers">
          <div class="number-wrap d-flex">
            <button class="number" data-value="1">
              1
            </button>
            <p> 이웃나라 임금님 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="2">
              2
            </button>
            <p> 이웃나라 공주님 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="3">
              3
            </button>
            <p> 이웃나라 왕자님 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="4">
              4
            </button>
            <p> 이웃나라 귀족 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="5">
              5
            </button>
            <p> 이웃나라 거지 </p>
          </div>
        </div>
        <p class="caution-message-mark"></p>
        <button class="next move-to-4">
          다음 문제
        </button>
      </div>
    `;
    btnSelect();
    moveTo4();
  }
  })
}


// 3단계에서 다음 문제 버튼을 누르면 3단계를 없애고 4단계 문제를 보여주는 함수
const moveTo4 = () => {
  const moveTo4Btn = document.querySelector('.move-to-4');
  const no3 = document.querySelector('.no3');
  moveTo4Btn.addEventListener('click', () => {
  const selectedCnt = document.getElementsByClassName('select').length;
  if (selectedCnt === 0) {
    const cautionMessage = document.querySelector('.caution-message-mark');
    cautionMessage.innerText = '보기 중 하나를 선택하고 버튼을 눌러주세요.';
  } else {
    const selectNumber = document.querySelector('.select');
    if (Number(selectNumber.dataset.value) === 3) {
      result += 1;
    }
    console.log(result);
    no3.remove()
    // 4단계 퀴즈 보여주기
    quizWrap.innerHTML += `
    <div class="no4">
      <h4 class="quiz__title no4__title">
        4. 토토로는 어떤 나무의 요정이며, 비를 맞는 토토로에게 우산을 빌려주자 토토로는 답례로 사츠키와 메이에게 무엇을 줬나요?
      </h4>
      <img class="quiz__img no4__img" src="https://cdn.univ20.com/wp-content/uploads/2015/09/6dc71e74e42f102d4c361f570eaec985.jpg" alt="">
      <div class="numbers">
        <div class="number-wrap d-flex">
          <button class="number" data-value="1">
            1
          </button>
          <p> 도토리 나무 / 도토리 씨앗 </p>
        </div>
        <div class="number-wrap d-flex">
          <button class="number" data-value="2">
            2
          </button>
          <p> 복숭아 나무 / 복숭아 씨앗 </p>
        </div>
        <div class="number-wrap d-flex">
          <button class="number" data-value="3">
            3
          </button>
          <p> 보리수 나무 / 보리수 씨앗 </p>
        </div>
        <div class="number-wrap d-flex">
          <button class="number" data-value="4">
            4
          </button>
          <p> 야자수 나무 / 야자수 씨앗 </p>
        </div>
        <div class="number-wrap d-flex">
          <button class="number" data-value="5">
            5
          </button>
          <p> 개다래나무 / 개다래 씨앗 </p>
        </div>
      </div>
      <p class="caution-message-mark"></p>
      <button class="next move-to-5">
        다음 문제
      </button>
    </div>
    `;
    btnSelect();
    moveTo5();
  }
  })
}


// 4단계에서 다음 문제 버튼을 누르면 4단계를 없애고 5단계 문제를 보여주는 함수
const moveTo5 = () => {
  const moveTo5Btn = document.querySelector('.move-to-5');
  const no4 = document.querySelector('.no4');
  moveTo5Btn.addEventListener('click', () => {
  const selectedCnt = document.getElementsByClassName('select').length;
  if (selectedCnt === 0) {
    const cautionMessage = document.querySelector('.caution-message-mark');
    cautionMessage.innerText = '보기 중 하나를 선택하고 버튼을 눌러주세요.';
  } else {
    const selectNumber = document.querySelector('.select');
    if (Number(selectNumber.dataset.value) === 1) {
      result += 1;
    }
    console.log(result);
    no4.remove()
    // 5단계 퀴즈 보여주기
    quizWrap.innerHTML += `
      <div class="no5">
        <h4 class="quiz__title no5__title">
          5. <센과 치히로의 행방불명>에서 치히로 부모님은 터널을 지나 마을로 들어와 어느 음식점에 차려진 음식들을 먹고 무엇이 되었나요?
        </h4>
        <img class="quiz__img no5__img" src="https://mblogthumb-phinf.pstatic.net/MjAxOTA2MTRfMjMy/MDAxNTYwNDQxOTE3ODIz.ExE7N4-TxDyMas1BbbHsjZkgvqKhXKn4ddfR9DMibJYg.IZZpZCJtibAFR4SVpWleYRLLCAvSqUR6j6XSkJjxJf4g.JPEG.paperpeer/%EC%8B%9D%EC%82%AC.jpg?type=w800" alt="">
        <div class="numbers">
          <div class="number-wrap d-flex">
            <button class="number" data-value="1">
              1
            </button>
            <p> 사슴 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="2">
              2
            </button>
            <p> 소 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="3">
              3
            </button>
            <p> 용 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="4">
              4
            </button>
            <p> 쥐 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="5">
              5
            </button>
            <p> 돼지 </p>
          </div>
        </div>
        <p class="caution-message-mark"></p>
        <button class="next move-to-6">
          다음 문제
        </button>
      </div>
    `;
    btnSelect();
    moveTo6();
  }
  })
}


// 5단계에서 다음 문제 버튼을 누르면 5단계를 없애고 6단계 문제를 보여주는 함수
const moveTo6 = () => {
  const moveTo6Btn = document.querySelector('.move-to-6');
  const no5 = document.querySelector('.no5');
  moveTo6Btn.addEventListener('click', () => {
  const selectedCnt = document.getElementsByClassName('select').length;
  if (selectedCnt === 0) {
    const cautionMessage = document.querySelector('.caution-message-mark');
    cautionMessage.innerText = '보기 중 하나를 선택하고 버튼을 눌러주세요.';
  } else {
    const selectNumber = document.querySelector('.select');
    if (Number(selectNumber.dataset.value) === 5) {
      result += 1;
    }
    console.log(result);
    no5.remove()
    // 6단계 퀴즈 보여주기
    quizWrap.innerHTML += `
      <div class="no6">
        <h4 class="quiz__title no6__title">
          6. '가마 할아버지' 밑에서 석탄을 옮기는 검댕이들의 밥(주식)은 무엇일까요?
        </h4>
        <img class="quiz__img no6__img" src="https://mblogthumb-phinf.pstatic.net/MjAxOTA3MDJfNDcg/MDAxNTYyMDQ0NzcyNDE3.kfITg78Cw_oI9GYoZ04wt_sj9V2_34rkp0_frPW_x-4g.Yy76QSoajYNMg4DWrG7ixmyWXFpg5TxvLFdKmIG_8tEg.JPEG.cine_play/61551047_707913612976062_6756110340273601266_n.jpg?type=w800" alt="">
        <div class="numbers">
          <div class="number-wrap d-flex">
            <button class="number" data-value="1">
              1
            </button>
            <p> 솜사탕 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="2">
              2
            </button>
            <p> 별설탕 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="3">
              3
            </button>
            <p> 각사탕 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="4">
              4
            </button>
            <p> 가루설탕 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="5">
              5
            </button>
            <p> 알사탕 </p>
          </div>
        </div>
        <p class="caution-message-mark"></p>
        <button class="next move-to-7">
          다음 문제
        </button>
      </div>
    `;
    btnSelect();
    moveTo7();
  }
  })
}


// 6단계에서 다음 문제 버튼을 누르면 6단계를 없애고 7단계 문제를 보여주는 함수
const moveTo7 = () => {
  const moveTo7Btn = document.querySelector('.move-to-7');
  const no6 = document.querySelector('.no6');
  moveTo7Btn.addEventListener('click', () => {
  const selectedCnt = document.getElementsByClassName('select').length;
  if (selectedCnt === 0) {
    const cautionMessage = document.querySelector('.caution-message-mark');
    cautionMessage.innerText = '보기 중 하나를 선택하고 버튼을 눌러주세요.';
  } else {
    const selectNumber = document.querySelector('.select');
    if (Number(selectNumber.dataset.value) === 2) {
      result += 1;
    }
    console.log(result);
    no6.remove()
    // 7단계 퀴즈 보여주기
    quizWrap.innerHTML += `
      <div class="no7">
        <h4 class="quiz__title no7__title">
          7. <센과 치히로의 행방불명>에서 '하쿠'는 '유바바'의 명령으로 '유바바 쌍둥이 언니'의 무엇을 훔쳤나요?
        </h4>
        <img class="quiz__img no7__img" src="https://t1.daumcdn.net/cfile/tistory/9980CF4F5E0C93CC1C" alt="">
        <div class="numbers">
          <div class="number-wrap d-flex">
            <button class="number" data-value="1">
              1
            </button>
            <p> 안경 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="2">
              2
            </button>
            <p> 사금 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="3">
              3
            </button>
            <p> 아기 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="4">
              4
            </button>
            <p> 도장 </p>
          </div>
          <div class="number-wrap d-flex">
            <button class="number" data-value="5">
              5
            </button>
            <p> 쿠키 </p>
          </div>
        </div>
        <p class="caution-message-mark"></p>
        <button class="next move-to-8">
          다음 문제
        </button>
      </div>
    `;
    btnSelect();
    moveTo8();

  }
  })
}


// 7단계에서 다음 문제 버튼을 누르면 7단계를 없애고 8단계 문제를 보여주는 함수
const moveTo8 = () => {
  const moveTo8Btn = document.querySelector('.move-to-8');
  const no7 = document.querySelector('.no7');
  moveTo8Btn.addEventListener('click', () => {
  const selectedCnt = document.getElementsByClassName('select').length;
  if (selectedCnt === 0) {
    const cautionMessage = document.querySelector('.caution-message-mark');
    cautionMessage.innerText = '보기 중 하나를 선택하고 버튼을 눌러주세요.';
  } else {
    const selectNumber = document.querySelector('.select');
    if (Number(selectNumber.dataset.value) === 4) {
      result += 1;
    }
    console.log(result);
    no7.remove()
    // 8단계 퀴즈 보여주기
    const no8 = document.querySelector('.no8');
    no8.style.display = 'block';
    btnSelect();
    activeOnResult();
    setResult();
  }
  })
}


// 8단계에서 보기를 선택하면 결과창으로 가는 버튼 활성화하는 함수
const activeOnResult = () => {
  const numbers = document.querySelectorAll('.last');
  const quizResultForm = document.querySelector('#id_quiz_rank');
  let flag = false;
  numbers.forEach((number) => {
    number.addEventListener('click', (event) => {
      if (Number(event.target.dataset.value) === 4) {
        result += 1;
        quizResultForm.innerText = `${result}`
        flag = true;
      } else {
        if (flag === true) {
          result -= 1;
          flag = false;
        }
        quizResultForm.innerText = `${result}`
      }
      console.log(result);
    })
  })
}

// 8단계 문제 보기 선택했는지 확인하는 함수
const setResult = () => {
  const moveToResultBtn = document.querySelector('.submit');
  moveToResultBtn.addEventListener('click', (event) => {
  const selectedCnt = document.getElementsByClassName('select').length;
  if (selectedCnt === 0) {
    event.preventDefault();
    const cautionMessage = document.querySelector('.caution-message');
    cautionMessage.innerText = '보기 중 하나를 선택하고 버튼을 눌러주세요.';
  }})
}


