const editBtn = document.getElementsByClassName("edit-btn");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitBtn = document.getElementById("submitBtn");

for(let btn of editBtn){
    btn.addEventListener("click",(e)=>{
        let reviewId = e.target.getAttribute("review_id");
        let reviewContent = document.getElementById('review${reviewId}').innerText;
        reviewText.value = reviewContent;
        submitBtn.innerText = "Update";
        commentForm.setAttribute("action", `edit_review/${reviewId}`);
    })
}