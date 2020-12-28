function passwordMatch(input) {
    document.getElementById(input).addEventListener('input', function () {
        let password = document.getElementById('password').value;
        let confirmPassword = document.getElementById('repeat-password').value;
        if (password === confirmPassword) {
            $('#submit').removeAttr("disabled");
        } else {
            $('#submit').attr("disabled", "disabled");
        }
    });
}

passwordMatch("password");
passwordMatch("repeat-password");