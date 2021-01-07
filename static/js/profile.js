$("#select-pic li").click(function() {
    let img = $(this).html();
    document.getElementById("profile-pic").value = img;
});

$("#open-update-profile").click(function() {
    $("#modal, #update-profile").css({"display": "flex"});
    $("#update-password, #delete-account").hide();
});
$("#open-update-password").click(function() {
    $("#modal, #update-password").css({"display": "flex"});
    $("#update-profile, #delete-account").hide();
});
$("#open-delete-account").click(function() {
    $("#modal, #delete-account").css({"display": "flex"});
    $("#update-password, #update-profile").hide();
});
$(".cancel").click(function() {
    $("#modal, #update-profile, #update-password, #delete-account").hide();
});