function starRating(num) {
    $('#rating >:nth-of-type(' + num + ')').click(function() {
        document.getElementById('score').value = num;
        for (i = num; i > 0; i--) {
            $('#rating >:nth-of-type(' + i + ')').attr("class", "fas fa-star");
        }
        for (i = num + 1; i < 6; i++) {
            $('#rating >:nth-of-type(' + i + ')').attr("class", "far fa-star");
        }
    });
    $('#rating >:nth-of-type(' + num + ')').keypress(function(e) {
        if (e.keyCode === 13) {
            document.getElementById('score').value = num;
            for (i = num; i > 0; i--) {
                $('#rating >:nth-of-type(' + i + ')').attr("class", "fas fa-star");
            }
            for (i = num + 1; i < 6; i++) {
                $('#rating >:nth-of-type(' + i + ')').attr("class", "far fa-star");
            }
        }
    });
}

starRating(1);
starRating(2);
starRating(3);
starRating(4);
starRating(5);


$("#delete").click(function() {
    $("#delete-review").show();
});
$("#delete").keypress(function(e) {
    if (e.keyCode === 13) {
        $("#delete-review").show();
    }
});

$(".cancel").click(function() {
    $("#delete-review").hide();
    $("#delete-whiskey").hide();
});
$(".cancel").keypress(function(e) {
    if (e.keyCode === 13) {
        $("#delete-review").hide();
        $("#delete-whiskey").hide();
    }
});

$("#admin-delete-whiskey").click(function() {
    $("#delete-whiskey").show();
});
$("#admin-delete-whiskey").keypress(function(e) {
    if (e.keyCode === 13) {
        $("#delete-whiskey").show();
    }
});