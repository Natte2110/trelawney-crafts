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
            let comments = ``
            commentsArray.forEach((comment) => {
                comments += `<div class="comment"><p><b>${comment.user}:</b> ${comment.content}</p></div>`;
            });
            $('#comments').html(comments);
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
        let title = post.childNodes[1].innerText;
        $('#comment-title').text(title);
    })
})

$('#comment-add').click(() => {
    let commentContent = $('#comment-content').val();
    console.log($('#comment-modal').attr("class").split(" ")[2])
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