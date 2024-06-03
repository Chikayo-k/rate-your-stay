const editBtns = document.getElementsByClassName("edit-btn");
const reviewText = document.getElementById("id_comment_area");
const reviewForm = document.getElementById("reviewForm");
const submitBtn = document.getElementById("submitBtn");
let editMessage = document.getElementsByClassName("review-leadmessage")[0];

for(let btn of editBtns){
    btn.addEventListener("click",(e)=>{
        let reviewId =  e.target.getAttribute("review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).textContent;
        editMessage.innerHTML= "<p class='fw-bold fs-3'>Edit this meassage!</p>"
        reviewText.value = reviewContent;
        submitBtn.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
        console.log(reviewContent);
    })
}

