const postLikeDiv = document.querySelectorAll(".post-like");
const postDeleteDiv = document.querySelectorAll(".post-delete-icon");
const postCommentDiv = document.querySelectorAll(".post-comment");

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

postDeleteDiv.forEach(function (element) {
    element.addEventListener("click", () => {
        fetch(`/delete_post/${element.classList[0]}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json" // Set the content type based on your API requirements
                // Add any additional headers if needed
            } // Convert the data to JSON format
        }).then(setTimeout(() => {
            location.reload();
        }, 100))
    })
})