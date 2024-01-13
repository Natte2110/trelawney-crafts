imageInput = document.getElementById("image");
imagePreview = document.getElementById("image-preview");
imageInput.onchange = (evt) => {
    const [file] = imageInput.files;
    if (file) {
        imagePreview.src = URL.createObjectURL(file);
    }
};