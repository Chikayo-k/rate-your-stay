const editBtns = document.getElementsByClassName("edit-btn");
const reviewTitle = document.getElementById("id_review_title");
const reviewText = document.getElementById("id_comment_area");
const reviewRating = document.getElementById("id_rate");
const reviewForm = document.getElementById("reviewForm");
const submitBtn = document.getElementById("submitBtn");
let message = document.getElementsByClassName("review-lead-message")[0];
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const writeReviewBtn = document.getElementsByClassName("write-review")[0];
const form = document.getElementsByClassName('form-hide')[0];


for(let btn of editBtns){
    btn.addEventListener("click",(e)=>{
        let reviewId =  e.target.getAttribute("data-review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        let reviewTitleText = document.getElementById(`review${reviewId}_title`).innerText;
        let reviewRatingText = document.getElementById(`review${reviewId}_rating`).innerText;
        message.innerHTML= "<p class='fw-bold fs-3'>Edit this message!</p>"
        form.style.display="block";
        reviewText.value = reviewContent;
        reviewTitle.value= reviewTitleText;
        reviewRating.value = reviewRatingText;
        submitBtn.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
        writeReviewBtn.style.display="none"
    })
}



for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("data-review_id");
      deleteConfirm.href = `review_delete/${reviewId}`;
      deleteModal.show();
    });
  }


/** 
 Display or hide a review form when the user is logged in
*/
function userLoggedIn(){
// Display a review form 
writeReviewBtn.addEventListener("click",() =>{
  form.style.display="block";
});

//Hide a review form
submitBtn.addEventListener("click",() =>{
  form.style.display="none";
});
}

//Error handling when there is no user logged in
try{
  userLoggedIn();
}catch(error){
  //Not logged in
}