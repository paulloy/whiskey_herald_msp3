/*jshint esversion: 6 */

// Allowed extensions to image address
let allow_exten = ["jpg", "jpeg", "png"];

// If the image address is valid, update src attr of #img
document.getElementById("image-url").addEventListener("input", function() {
    let arr = document.getElementById("image-url").value.split(".");
    let pop = arr.pop().toLowerCase();
    if (pop === allow_exten[0] || pop === allow_exten[1] || pop === allow_exten[2]) {
        console.log(pop);
        document.getElementById("img").setAttribute("src", document.getElementById("image-url").value);
        document.getElementById("img").setAttribute("alt", `Image of ${document.getElementById("whiskey-name").value} Whiskey`);
    }
});