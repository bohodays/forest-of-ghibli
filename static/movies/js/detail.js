const forms = document.querySelectorAll('.like-forms')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
console.log(forms)
console.log(csrftoken)

forms.forEach((form) => {
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    console.log('111111111',event.target.dataset)

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