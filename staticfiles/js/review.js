const editBtns = document.getElementsByClassName("edit-btn");
const reviewTitle = document.getElementById("id_review_title");
const reviewText = document.getElementById("id_comment_area");
const reviewRating = document.getElementById("id_rate");
const reviewForm = document.getElementById("reviewForm");
const submitBtn = document.getElementById("submitBtn");
let editMessage = document.getElementsByClassName("review-leadmessage")[0];


for(let btn of editBtns){
    btn.addEventListener("click",(e)=>{
        let reviewId =  e.target.getAttribute("review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        let reviewTitleText = document.getElementById(`review${reviewId}_title`).innerText;
        let reviewRatingText = document.getElementById(`review${reviewId}_rating`).innerText;
        editMessage.innerHTML= "<p class='fw-bold fs-3'>Edit this meassage!</p>"
        reviewText.value = reviewContent;
        reviewTitle.value= reviewTitleText;
        reviewRating.value = reviewRatingText;
        submitBtn.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
        console.log(reviewContent);
        console.log(reviewRatingText);
    })
}

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      deleteConfirm.href = `review_delete/${reviewId}`;
      deleteModal.show();
    });
  }