/**
* @file The file is used in order to create and manage the information within the "delete account" functionality.
* When deleting accounts, this script first checks that the users password they entered to confirm account deletion matches that in the database before continuing.
* @author Nathan Parsley
*/
document.getElementById("delete-account").addEventListener("click", () => {
    $("#delete-account-modal").modal("toggle")
})

$("#delete-form").submit(function (e) {
    e.preventDefault();
    fetch("/delete-account", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            password: $("#password-check").val()
        }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success == false) {
                $("#delete-error").html(`<p class="link-danger">Password does not match.</p>`)
            } else {
                location.replace("/")
            }
        })
        .catch((error) => {
            console.error("Error:", error);
        });
});