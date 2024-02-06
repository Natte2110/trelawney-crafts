/**
* @file This script is used in order to create a preview
* image on the "Create Post"/"upload" page
* @author Nathan Parsley
*/
let imageInput = document.getElementById("image");
let imagePreview = document.getElementById("image-preview");
imageInput.onchange = function () {
    const [file] = imageInput.files;
    if (file) {
        imagePreview.src = URL.createObjectURL(file);
    }
};