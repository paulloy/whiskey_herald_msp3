$('#navbar-toggle').click(function () {
    $('#navbar-background').show();
    $('#sidenav').show().animate({
        right: "0"
    }, 300);
});

$('#navbar-background, #close-navbar').click(function () {
    $('#navbar-background').hide();
    $('#sidenav').animate({
        right: '-20rem'
    }, 300, function() {
        $('#sidenav').hide();
    });
});