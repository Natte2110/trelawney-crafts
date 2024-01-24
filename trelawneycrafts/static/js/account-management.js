document.getElementById("delete-account").addEventListener("click", () => {
    $('#delete-account-modal').modal('toggle')
})

$("#delete-form").submit(function (e) {
    e.preventDefault();
    fetch("/delete-account", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            password: $('#password-check').val()
        }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.success == false) {
                $("#delete-error").html(`<p class="link-danger">Password does not match.</p>`)
            } else {
                location.replace("/")
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});