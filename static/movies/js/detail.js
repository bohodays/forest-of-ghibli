
// 전역 변수 토큰
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
// console.log(csrftoken)


// 좋아요
const forms = document.querySelectorAll('.like-forms')
forms.forEach((form) => {
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    // console.log('111111111',event.target.dataset)
    
    const movieId = event.target.dataset.movieId
    const commentId = event.target.dataset.commentId
    
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/${movieId}/comments/${commentId}/likes/`,
      headers: {'X-CSRFToken': csrftoken,},
    })
    .then((response) => {
      console.log(response.data.like_count);
      // response 값을 html의 태그 하나 가져와서 그 값에 넣어 줘야함.
      const likeCount = document.querySelector(`#like_${commentId}`)
      likeCount.innerHTML=response.data.like_count      
      console.log(likeCount);
      const isLiked = response.data.is_liked
      const likeBtn = document.querySelector(`#like-${commentId}`)
      if (isLiked === true) {
        likeBtn.innerHTML = `<i class="fa-sharp fa-solid fa-heart"></i>`;
      } else {
        likeBtn.innerHTML = `<i class="fa-regular fa-heart"></i>`;
      }
      // likeBtn.value = isLiked ? '좋아요 취소' : '좋아요'
    })
    .catch((error) => {
      console.log('??',error.response)
    })
  })
})


// 댓글 삭제
const deleteForms = document.querySelectorAll('.delete-forms')
deleteForms.forEach((deleteForm) => {
  deleteForm.addEventListener('submit', (event) => {
    event.preventDefault()
    const movieId = event.target.dataset.movieId
    const deleteId = event.target.dataset.deleteId

axios({
  method: 'post',
  url: `http://127.0.0.1:8000/movies/${movieId}/comments/${deleteId}/delete/`,
  headers: {'X-CSRFToken': csrftoken,},
})
  .then((response) => {
    // 버튼을 누른 댓글
    const userForm = event.target.parentNode.parentNode.parentNode.parentNode;
    userForm.remove();
  })
    .catch((error) => {
      console.log('??',error.response)
    })
  })
})
  
  
 // 댓글 생성
const createForms = document.querySelectorAll('.form-comment')
createForms.forEach((createForm)=>{
  createForm.addEventListener('submit',event =>{
    event.preventDefault()
    // 해당 영화의 pk 값 저장
    const movieId = event.target.dataset.movieId
  // 보내줄 데이터 가져오기
  const content = document.getElementsByName('content')[0].value
  const movieRate = document.getElementsByName('movie_rate')[0].value
  const user = document.querySelector('.nickname-wrap');
  const userNickName = user.innerText

  let data = new FormData()
  data.append("content", content)
  data.append("movie_rate",movieRate)

  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/movies/${movieId}/comments/`,
    headers: {'X-CSRFToken': csrftoken,},
    data: data,
    }).then((response)=>{
    // 댓글 id
    const responseCommentId = response.data.comment_id
    // 댓글 내용
    const responseContent = response.data.comment_content
    // 댓글 평점
    const responseRate = response.data.comment_movie_rate
    // 영화 id
    const responseMovieId = response.data.movie_id

    const reviewContent = document.createElement('p')
    reviewContent.innerText=responseContent
    const commentList = document.querySelector('.user-comments__wrap')
    commentList.innerHTML += `
      <div class="user-comments">
        <div class="comment-nickname-wrap">
          <i class="fas fa-user"></i>
          ${userNickName}
        </div>
        <div class="comment-wrap">
          <p class="comment_full hidden">${responseContent}</p>
          <p class="comment__content summary">${responseContent}</p>
        </div>

        <div class='all-wrap d-flex flex-column'>
          <p>평점 ${responseRate}</p>
          
            <div class="delete_edit-wrap">
                <form class="async-delete-forms"  data-delete-id="${responseCommentId}" data-movie-id="${responseMovieId}">
                  
                  <button class="btn-wrap delete-btn" type="submit" value="삭제" id="delete-${responseCommentId}">
                    <i class="fa-solid fa-trash-can"></i>
                  </button>
                </form>
                <a class="btn-wrap edit-btn" href="{% url 'movies:comments_update' %}">
                  <i class="fa-solid fa-pen-to-square"></i>
                </a>
            </div>
          </div>
        </div>
      </div>
    `;
      const asyncDeleteComments = document.querySelectorAll('.async-delete-forms')
      // console.log(asyncDeleteComments);
      asyncDeleteComments.forEach(asyncDeleteComment =>{
        asyncDeleteComment.addEventListener('submit',event =>{
          event.preventDefault()
          
          axios({
            method: 'post',
            url: `http://127.0.0.1:8000/movies/${responseMovieId}/comments/${responseCommentId}/delete/`,
            headers: {'X-CSRFToken': csrftoken,},
          })
            .then((response) => {
            // 버튼을 누른 댓글
            const userForm = event.target.parentNode.parentNode.parentNode;
            console.log(userForm);
            userForm.remove();
          })
          .catch((error) => {
            console.log('삭제 오류',error.response)
          })
        })
      })
    }).catch(error=>{
      console.log('??',error);
      })
  })
})

// {{ comment.content|truncatechars:100 }}
  
  // 유튭 예고편
  const URL = 'https://www.googleapis.com/youtube/v3/search';
const API_KEY = 'AIzaSyBzR_HnOKtGGjgBZ8XYwFI8gbA4MuDONWU';
// 서브키
// AIzaSyCN4Qzq5muVRcWFdtszQlpJOKVytuYOumI
const title = document.querySelector('.info__title');
const iframe = document.querySelector('iframe');

const getYoutubeVideo = () => {
  axios.get(URL, {
    params: {
      key: API_KEY,
      type: 'video',
      part: 'snippet',
      q: `${title.innerText} Official Trailer`
    }
  })
    .then((response) => {
      const selectedVideo = response.data.items[0];
      const vedioSrc = `https://youtube.com/embed/${selectedVideo.id.videoId}`;
      iframe.setAttribute('src', vedioSrc)
    })
    .catch((error) => {
      if (title.innerText === '이웃집 토토로') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/8LLmvVSnYiw');
      } else if (title.innerText === '마녀 배달부 키키') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/zbvx7pqw5Gg');
      } else if (title.innerText === '모노노케 히메') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/4OiMOHRDs14');
      } else if (title.innerText === '이웃집 야마다군') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/1C9ujuCPlnY');
      } else if (title.innerText === '센과 치히로의 행방불명') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/lwrG3HQXTFw');
      } else if (title.innerText === '고양이의 보은') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/Gp-H_YOcYTM');
      } else if (title.innerText === '벼랑 위의 포뇨') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/lSYGyrlFoeA');
      } else if (title.innerText === '추억의 마니') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/7F3LdDJmEgM');
      } else if (title.innerText === '붉은 거북') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/lGGrlUiVTpY');
      } else if (title.innerText === '아야와 마녀') {
        iframe.setAttribute('src', 'https://www.youtube.com/embed/fe3r-hOOxAE');
      } 
      console.log(error);
    })
}

window.addEventListener('load', () => {
  if (title.innerText === '천공의 성 라퓨타') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/8ykEy-yPBFc');
  } else if (title.innerText === '바람계곡의 나우시카') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/6zhLBe319KE');
  }  else if (title.innerText === '반딧불이의 묘') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/4vPeTSRd580');
  } else if (title.innerText === '추억은 방울방울') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/qu7Dw4NJmY4');
  } else if (title.innerText === '붉은 돼지') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/awEC-aLDzjs');
  } else if (title.innerText === '바다가 들린다') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/tfkHiHjrqa8');
  } else if (title.innerText === '폼포코 너구리 대작전') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/_7cowIHjCD4');
  } else if (title.innerText === '귀를 기울이면') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/0pVkiod6V0U');
  } else if (title.innerText === '게드전기: 어스시의 전설') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/8hxYx3Jq3kI');
  } else if (title.innerText === '마루 밑 아리에티') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/-BVG41qJaQY');
  } else if (title.innerText === '코쿠리코 언덕에서') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/9nzpk_Br6yo');
  } else if (title.innerText === '가구야공주 이야기') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/r6RsS4poOok');
  } else {
    getYoutubeVideo();
  }
})

