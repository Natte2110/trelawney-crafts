const postLikeDiv = document.querySelectorAll(".post-like");
const postDeleteDiv = document.querySelectorAll(".post-delete-icon");
const postCommentDiv = document.querySelectorAll(".post-comment");
let openPost;

/** 
* Requests an array of comments on the selected post from the Backend and displays them in the 
* @summary If the description is long, write your summary here. Otherwise, feel free to remove this.
* @param {Number} post_id - The id of the post to be searched for in the DB
*/
const getComments = (post_id) => {
    fetch(`/get_comments/${post_id}`)
        .then((response) => response.json())
        .then((commentsArray) => {
            const currentUserID = commentsArray[0].current_user;
            if (currentUserID == null) {
                $('#comment-content').attr('disabled', 'disabled');
                $('#comment-content').attr('placeholder', 'Please log in to comment.');
                $('#comment-add').attr('disabled', 'disabled');
            } else {
                $('#comment-content').removeAttr("disabled");
                $('#comment-content').attr('placeholder', 'Type your comment here...');
                $('#comment-add').removeAttr("disabled");
            }
            let comments = ``
            commentsArray[1].forEach((comment) => {
                if (currentUserID == comment.userid) {
                    comments += `<div class="comment"><a class="comment-delete ${comment.id}"><i class="bi bi-trash"></i></a><p><b>${comment.user}:</b> ${comment.content} </p></div>`
                } else {comments += `<div class="comment"><p><b>${comment.user}:</b> ${comment.content}</p></div>`}
                
            });
            $('#comments').html(comments);
            postCommentDiv.forEach(element => {
                if (element.classList[0] == post_id) {
                    element.innerHTML = `<i class="bi bi-chat-right-dots"></i> ${commentsArray[1].length}`
                }
            })
            const commentDelete = document.querySelectorAll(".comment-delete");
            commentDelete.forEach(function (element) {
                element.addEventListener("click", () => {
                    fetch(`/remove_comment/${element.classList[1]}`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        }
                    }).then(setTimeout(() => {
                        getComments(post_id)
                    }, 100))
                })
            })
        })
        .catch((error) => console.warn(error))
}

postLikeDiv.forEach(function (element) {
    element.addEventListener("click", function () {
        if (element.classList[2] == "disabled") {
            location.replace("/log-in")
        }
        else if (element.classList[2] == "liked") {
            element.classList.remove("liked");
            fetch(`/remove_reaction/${element.classList[0]}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json" // Set the content type based on your API requirements
                    // Add any additional headers if needed
                } // Convert the data to JSON format
            }).then(setTimeout(() => {
                fetch(`/reaction_count/${element.classList[0]}`)
                    .then((response) => response.json())
                    .then((responseData) => {
                        element.childNodes[1].innerHTML = responseData;
                    })
                    .catch((error) => console.warn(error))
            }, 100
            )
            )

        } else {
            element.classList.add("liked");
            fetch(`/add_reaction/${element.classList[0]}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json" // Set the content type based on your API requirements
                    // Add any additional headers if needed
                } // Convert the data to JSON format
            }).then(setTimeout(() => {
                fetch(`/reaction_count/${element.classList[0]}`)
                    .then((response) => response.json())
                    .then((responseData) => {
                        element.childNodes[1].innerHTML = responseData;
                    })
                    .catch((error) => console.warn(error))
            }, 100
            )
            )
        }
    });
});

postCommentDiv.forEach(function (element) {
    element.addEventListener("click", () => {
        openPost = element.classList[0];
        getComments(openPost);
        $('#comment-modal').modal('toggle')
        let post = document.getElementById(element.classList[0]);
        $('#comment-modal').addClass(element.classList[0]);
        $('#comment-content').val("");
        let imgLink = document.getElementById(`${element.classList[0]}-img`).src;
        $("#modal-image").css('background-image', `url("${imgLink}")`);
        let title = post.childNodes[1].innerText;
        $('#comment-title').text(title);
    })
})

$('#comment-add').click(() => {
    let commentContent = $('#comment-content').val();
    let postId = $('#comment-modal').attr("class").split(" ")[2];
    fetch(`/add_comment/${postId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            commentContent: commentContent
        }),
    })
        .then(() => {
            getComments(openPost);
            $('#comment-content').val("")
        })
        .catch(error => {
            console.error('Error:', error);
        });
})

$('#comment-close').click(() => {
    $('#comment-modal').modal('toggle');
})

$('#comment-exit').click(() => {
    $('#comment-modal').modal('toggle');
})

postDeleteDiv.forEach(function (element) {
    element.addEventListener("click", () => {
        fetch(`/delete_post/${element.classList[0]}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            }
        }).then(setTimeout(() => {
            location.reload();
        }, 100))
    })
})