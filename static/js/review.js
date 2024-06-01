const editBtns = document.getElementsByClassName("edit-btn");
const reviewText = document.getElementById("id_comment_area");
const reviewForm = document.getElementById("reviewForm");
const submitBtn = document.getElementById("submitBtn");

for(let btn of editBtns){
    btn.addEventListener("click",(e)=>{
        let reviewId =  e.target.getAttribute("review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        reviewText.value = reviewContent;
        submitBtn.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
        console.log(reviewContent);
    })
}

