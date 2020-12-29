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
}

starRating(1);
starRating(2);
starRating(3);
starRating(4);
starRating(5);
