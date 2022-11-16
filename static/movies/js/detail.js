
// 좋아요
const forms = document.querySelectorAll('.like-forms')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
console.log(forms)
console.log(csrftoken)

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
      console.log(response, 333333333)
      // console.log(response.data)
      const isLiked = response.data.is_liked
      const likeBtn = document.querySelector(`#like-${commentId}`)
      if (isLiked === true) {
        likeBtn.value = '좋아요 취소'
      } else {
        likeBtn.value = '좋아요'
      }
      // likeBtn.value = isLiked ? '좋아요 취소' : '좋아요'
    })
    .catch((error) => {
      console.log('??',error.response)
    })
  })
})

// // 댓글 삭제
const deleteForms = document.querySelector('.delete-forms')
if (deleteForms){

    deleteForms.addEventListener('submit', function (event) {
      event.preventDefault()
      console.log('delete eventTargetDataset',event.target.dataset)
      
      const movieId = event.target.dataset.movieId
      // 이름만 delete고 지울 댓글의 아이디를 가져옴
      const deleteId = event.target.dataset.deleteId
    
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${movieId}/comments/${deleteId}/delete/`,
        headers: {'X-CSRFToken': csrftoken,},
      })
      .then((response) => {
        console.log(response.data, 'delete axios then function')
        
        // url 요청을 가져오는걸 성공 했을 경우 여기서 
        const isDeleted = response.data.is_deleted
        console.log('thenthenthenthen',isDeleted);
        
        // return window.location.reload()
        // likeBtn.value = isLiked ? '좋아요 취소' : '좋아요'
      })
      .catch((error) => {
        console.log('??',error.response)
      })
    })
  }
  




// 유튭 예고편
const URL = 'https://www.googleapis.com/youtube/v3/search';
const API_KEY = 'AIzaSyBzR_HnOKtGGjgBZ8XYwFI8gbA4MuDONWU';
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
      console.log(error);
    })
}

window.addEventListener('load', () => {
  if (title.innerText === '바람계곡의 나우시카') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/6zhLBe319KE');
  }  else if (title.innerText === '반딧불이의 묘') {
    iframe.setAttribute('src', 'https://www.youtube.com/embed/_wlptzigQn0');
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
