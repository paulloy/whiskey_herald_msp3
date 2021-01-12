/*globals $:false */
/*jshint esversion: 6 */

// Sidenav

let i = 0;
let openNav = '<i class="fas fa-bars"></i>';
let closeNav = '<i class="fas fa-times"></i>';
let button = document.getElementById('navbar-toggle');

function navbar() {
    i++;
    let j = i % 2;
    if (j === 1) {
        button.innerHTML = closeNav;
        $('#navbar-background').show();
        $('#sidenav').show().animate({
        right: "0"
        }, 300);
    } else {
        button.innerHTML = openNav;
        $('#navbar-background').hide();
        $('#sidenav').animate({
            right: '-600px'
        }, 300, function() {
            $('#sidenav').hide();
        });
    }
}

$('#navbar-toggle, #navbar-background').click(navbar);
$('#navbar-toggle, #navbar-background').keypress(function(e) {
    if (e.keyCode === 13) {
        navbar();
    }
});


// close flashed messages
$('#close-flash').click(function () {
    $("#flash").remove();
});