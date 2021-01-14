/*globals $:false */
/*jshint esversion: 6 */

// profile icon selection. selected icon is previewed in #profile-pic
$("#select-pic li").click(function() {    
    let img = $(this).html();
    $(this).attr("class", "selected");
    $(this).siblings().removeAttr("class");
    document.getElementById("profile-pic").setAttribute("value", img);
    document.getElementById("current-icon").innerHTML = img;
});
$("#select-pic li").keypress(function(e) {
    if (e.keyCode === 13) {
        let img = $(this).html();
        $(this).attr("class", "selected");
        $(this).siblings().removeAttr("class");
        document.getElementById("profile-pic").setAttribute("value", img);
        document.getElementById("current-icon").innerHTML = img;
    }
});

// The users current profile icon is prepended to <ul> and highlighted with .select class
for (let i = 0; i < $("#select-pic").children().length; i++) {
    if ($("#select-pic").children()[i].innerHTML === document.getElementById("profile-pic").value) {
        $("#select-pic").children()[i].setAttribute("class", "selected");
        $("#select-pic").prepend($("#select-pic").children()[i]);
    }
}

// The users new username is previewed in #current-username
document.getElementById("username").addEventListener("input", function() {
    document.getElementById("current-username").innerText = document.getElementById("username").value;
});

// open #update-profile
$("#open-update-profile").click(function() {
    $("#modal, #update-profile").css({"display": "flex"});
    $("#select-pic").show();
    $("#update-password, #delete-account").hide();
});
$("#open-update-profile").keypress(function(e) {
    if (e.keyCode === 13) {
        $("#modal, #update-profile").css({"display": "flex"});
        $("#select-pic").show();
        $("#update-password, #delete-account").hide();
    }
});

// open #update-password
$("#open-update-password").click(function() {
    $("#modal, #update-password").css({"display": "flex"});
    $("#update-profile, #delete-account").hide();
});
$("#open-update-password").keypress(function(e) {
    if (e.keyCode === 13) {
        $("#modal, #update-password").css({"display": "flex"});
        $("#update-profile, #delete-account").hide();
    }
});

// open #delete-password
$("#open-delete-account").click(function() {
    $("#modal, #delete-account").css({"display": "flex"});
    $("#update-password, #update-profile").hide();
});
$("#open-delete-account").keypress(function(e) {
    if (e.keyCode === 13) {
        $("#modal, #delete-account").css({"display": "flex"});
        $("#update-password, #update-profile").hide();
    }
});

// close #modal and its children
$(".cancel").click(function() {
    $("#modal, #update-profile, #update-password, #delete-account").hide();
});
$(".cancel").keypress(function(e) {
    if (e.keyCode === 13) {
        $("#modal, #update-profile, #update-password, #delete-account").hide();
    }
});