let imageInput = document.getElementById("image");
let imagePreview = document.getElementById("image-preview");
imageInput.onchange = function () {
    const [file] = imageInput.files;
    if (file) {
        imagePreview.src = URL.createObjectURL(file);
    }
};