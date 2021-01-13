/*globals $:false */
/*jshint esversion: 6 */

// This function is responsible for creating an interactive 5 star rating system
function starRating(num) {
    $('#rating >:nth-of-type(' + num + ')').click(function() {
        document.getElementById('score').value = num;
        for (let i = num; i > 0; i--) {
            $('#rating >:nth-of-type(' + i + ')').attr("class", "fas fa-star");
        }
        for (let i = num + 1; i < 6; i++) {
            $('#rating >:nth-of-type(' + i + ')').attr("class", "far fa-star");
        }
    });
    $('#rating >:nth-of-type(' + num + ')').keypress(function(e) {
        if (e.keyCode === 13) {
            document.getElementById('score').value = num;
            for (let i = num; i > 0; i--) {
                $('#rating >:nth-of-type(' + i + ')').attr("class", "fas fa-star");
            }
            for (let i = num + 1; i < 6; i++) {
                $('#rating >:nth-of-type(' + i + ')').attr("class", "far fa-star");
            }
        }
    });
}

starRating(1);starRating(2);starRating(3);starRating(4);starRating(5);

function updateReview() {
    // userReview and its edit method are defined in whiskey.html with jinja importing values
    userReview.edit();
    starRating(1);starRating(2);starRating(3);starRating(4);starRating(5);
    for (let item of document.getElementById("rating").children) {
        item.setAttribute("tabindex", "0");
    }
}

document.getElementById("edit-review").addEventListener("click", updateReview);
document.getElementById("edit-review").addEventListener("keypress", function (e) {
    if (e.keyCode === 13) {
        updateReview();
    }
});

// display #delete-review
$("#delete").click(function() {
    $("#delete-review").show();
});
$("#delete").keypress(function(e) {
    if (e.keyCode === 13) {
        $("#delete-review").show();
    }
});

// hide #delete-review and #delete-whiskey for admin
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

// display #delete-whiskey for admin
$("#admin-delete-whiskey").click(function() {
    $("#delete-whiskey").show();
});
$("#admin-delete-whiskey").keypress(function(e) {
    if (e.keyCode === 13) {
        $("#delete-whiskey").show();
    }
});