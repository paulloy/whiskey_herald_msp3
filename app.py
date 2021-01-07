import os
from flask import (
    Flask, render_template, flash, redirect, request, session, url_for, json, abort
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_moment import Moment
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
moment = Moment(app)

# get collections
data = mongo.db


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/add_whiskey", methods=["GET", "POST"])
def add_whiskey():
    if not session:
        flash("You must register an account if you want to add a whiskey", "error")

    if request.method == "POST":
        existing_drink = data.drinks.find_one(
            {"drink": request.form.get("whiskey-name").lower()}
        )

        if existing_drink:
            flash("This drink already exists", "error")
            return redirect(url_for("add_whiskey"))

        allow_exten = ["jpg", "jpeg", "png"]
        form_url = str(request.form.get("image-url"))
        x = form_url.split(".")
        y = x[-1]

        if y == allow_exten[0] or y == allow_exten[1] or y == allow_exten[2]:
            formSubmission = {
                "drink": request.form.get("whiskey-name"),
                "image_location": str(request.form.get("image-url")),
                "type": request.form.get("whiskey-type"),
                "description": request.form.get("description"),
                "average_score": "number"
            }

            data.drinks.insert_one(formSubmission)
            flash("This drink has been added to Whiskey Herald", "success")

        else:
            flash("Url must end with .jpg, .jpeg, or .png", "error")
            return redirect(url_for("add_whiskey"))

        return redirect(url_for("whiskey", whiskey_name=formSubmission["drink"]))

    return render_template("add-whiskey.html")


@app.route("/edit_whiskey/<whiskey_name>", methods=["GET", "POST"])
def edit_whiskey(whiskey_name):
    find_drink = data.drinks.find_one({"drink": whiskey_name})

    if not session:
        flash("You must be logged in to update a whiskey", "error")
        return redirect(url_for("login"))

    if request.method == "POST":
        allow_exten = ["jpg", "jpeg", "png"]
        form_url = str(request.form.get("image-url"))
        x = form_url.split(".")
        y = x[-1]

        if y == allow_exten[0] or y == allow_exten[1] or y == allow_exten[2]:
            whiskeyUpdate = {
                "drink": request.form.get("whiskey-name"),
                "image_location": str(request.form.get("image-url")),
                "type": request.form.get("whiskey-type"),
                "description": request.form.get("description")
            }

            find_reviews = data.reviews.find({"drink": whiskey_name})
            for doc in find_reviews:
                reviewUpdate = {
                    "username": doc["username"],
                    "drink": whiskeyUpdate["drink"],
                    "title": doc["title"],
                    "review": doc["review"],
                    "score": doc["score"]
                }

                data.reviews.update({"drink": whiskey_name}, reviewUpdate)

        else:
            flash("Url must end with .jpg, .jpeg, or .png", "error")
            return redirect(url_for("edit_whiskey", whiskey_name=whiskey_name))

        data.drinks.update({"drink": whiskey_name}, whiskeyUpdate)
        flash("Whiskey has been updated", "success")
        return redirect(url_for("whiskey", whiskey_name=whiskeyUpdate["drink"]))

    return render_template("edit-whiskey.html", whiskey_name=whiskey_name, find_drink=find_drink)


@app.route("/delete_whiskey/<whiskey_name>")
def delete_whiskey(whiskey_name):
    if session:
        if session["username"] == "admin":
            data.drinks.remove({"drink": whiskey_name})
            data.reviews.remove({"drink": whiskey_name})
            flash("Whiskey has been removed from the database", "success")
        else:
            return abort(403)
    else:
        return abort(403)

    return redirect(url_for("add_whiskey"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_username = data.users.find_one(
            {"username_lower": request.form.get("username").lower()}
        )
        existing_email = data.users.find_one(
            {"email": request.form.get("email").lower()}
        )

        if existing_username:
            flash("This username is unavailable, please try another.", "error")
            return redirect(url_for("register"))
        elif existing_email:
            flash("This email is unavailable, please try another.", "error")
            return redirect(url_for("register"))

        password = generate_password_hash(request.form.get("password"))
        password_repeat = check_password_hash(password, request.form.get("repeat-password"))

        if password_repeat:
            # dictionary for inserting a new user to users collection
            newUser = {
                "email": str(request.form.get("email")).lower(),
                "username": str(request.form.get("username")),
                "username_lower": str(request.form.get("username")).lower(),
                "password": generate_password_hash(request.form.get("password")),
                "bio": "Tell us more about yourself :)",
                "profile_pic": "DEFAULT"
            }

            data.users.insert_one(newUser)

            flash("Registration successful, thanks for joining! \
                You can now login.", "success")
        else:
            flash("Passwords do not match. Please try again.", "error")
            return redirect(url_for("register"))

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = data.users.find_one(
            {"email": request.form.get("email")}
        )

        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                current_user = mongo.db.users.find_one(
                    {"email": request.form.get("email")}
                )

                session["email"] = current_user["email"]
                session["username"] = current_user["username"]
                session["profile_pic"] = current_user["profile_pic"]

                flash("You have logged in. Welcome " + session["username"], "success")
                return redirect(url_for("profile", username=session["username"]))
            else:
                flash("Incorrect Email/Password", "error")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Email/Password", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out", "success")
    return redirect(url_for("login"))


@app.route("/profile/<username>")
def profile(username):
    user = data.users.find_one(
        {"username": username}
    )

    userDetails = {
        "username": user["username"],
        "bio": user["bio"],
        "profile_pic": user["profile_pic"]
    }

    user_reviews = data.reviews.find({"username": username})

    return render_template("profile.html", username=username, userDetails=userDetails, user_reviews=user_reviews)


@app.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):
    if not session or session["username"] != username:
        return abort(403)

    if request.method == "POST":
        user_record = data.users.find_one({"username": username})
        user_reviews = data.reviews.find({"username": username})
        existing_username = data.users.find_one({"username_lower": str(request.form.get("username")).lower()})

        if (existing_username is None) or (existing_username["username_lower"] == session["username"].lower()):
            user = {
                "email": user_record["email"],
                "username": str(request.form.get("username")),
                "username_lower": str(request.form.get("username")).lower(),
                "password": user_record["password"],
                "bio": request.form.get("biography"),
                "profile_pic": request.form.get("profile-pic"),
            }

            if user_reviews is not None:
                for doc in user_reviews:
                    updateReviews = {
                        "username": user["username"],
                        "profile_pic": user["profile_pic"],
                        "drink": doc["drink"],
                        "title": doc["title"],
                        "review": doc["review"],
                        "score": doc["score"],
                        "time": doc["time"]
                    }
                    data.reviews.update({"username": username, "drink": updateReviews["drink"]}, updateReviews)
        else:
            flash("This username already exists. Please try another", "error")
            return redirect(url_for("profile", username=username))

        data.users.update({"username": username}, user)

        session["username"] = user["username"]

        flash("profile successfully updated", "success")

        return redirect(url_for("profile", username=user["username"]))


@app.route("/update_password/<username>", methods=["GET", "POST"])
def update_password(username):
    if not session or session["username"] != username:
        return abort(403)

    if request.method == "POST":
        find_user = data.users.find_one({"username_lower": session["username"].lower()})

        password = generate_password_hash(request.form.get("password"))
        password_repeat = check_password_hash(password, request.form.get("repeat-password"))

        if password_repeat:
            user = {
                    "email": find_user["email"],
                    "username": find_user["username"],
                    "username_lower": find_user["username_lower"],
                    "password": generate_password_hash(request.form.get("password")),
                    "bio": find_user["bio"],
                    "profile_pic": find_user["profile_pic"],
                }

            data.users.update({"username": session["username"]}, user)
            flash("Your password has been updated", "success")
        else:
            flash("Your passwords do not match. Please try again.", "error")



    return redirect(url_for("profile", username=username))


@app.route("/delete_account/<username>", methods=["GET", "POST"])
def delete_account(username):
    if not session or session["username"] != username:
        return abort(403)

    data.users.remove({"username": session["username"]})
    data.reviews.remove({"username": session["username"]})
    flash("Your account has been successfully deleted", "success")

    return redirect(url_for("register"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search")
    results = list(data.drinks.find({"$text": {"$search": query}}))

    searched_value = request.form.get("search")

    return render_template("search.html", results=results, searched_value=searched_value)


@app.route("/whiskey/<whiskey_name>")
def whiskey(whiskey_name):
    find_whiskey = data.drinks.find_one({"drink": whiskey_name})
    find_reviews = data.reviews.find({"drink": whiskey_name})
    find_average_score = data.reviews.find({"drink": whiskey_name})

    if find_whiskey is None:
        return abort(404)

    average_score = 0
    if find_average_score.count() != 0:
        for doc in find_average_score:
            average_score = average_score + int(doc["score"])
        average_score = int(round(average_score / find_average_score.count()))

    whiskeyDetails = {
        "drink": find_whiskey["drink"],
        "image_location": find_whiskey["image_location"],
        "type": find_whiskey["type"],
        "description": find_whiskey["description"]
    }

    return render_template("whiskey.html", whiskeyDetails=whiskeyDetails, find_reviews=find_reviews, average_score=average_score)


@app.route("/review/<whiskey_name>", methods=["GET", "POST"])
def review(whiskey_name):
    if not session:
        return abort(403)

    existing_review = data.reviews.find_one({"username": session["username"], "drink": whiskey_name})
    current_time = datetime.utcnow()

    if request.method == "POST":
        if existing_review:
            reviewUpdate = {
                "username": session["username"],
                "profile_pic": data.users.find_one({"username": session["username"]})["profile_pic"],
                "drink": whiskey_name,
                "title": request.form.get("review-title"),
                "review": request.form.get("review"),
                "score": int(request.form.get("score")),
                "time": current_time
            }

            data.reviews.update({"username": session["username"], "drink": whiskey_name}, reviewUpdate)
            flash("Your review has been updated", "success")

        else:
            newReview = {
                "username": session["username"],
                "profile_pic": data.users.find_one({"username": session["username"]})["profile_pic"],
                "drink": whiskey_name,
                "title": request.form.get("review-title"),
                "review": request.form.get("review"),
                "score": int(request.form.get("score")),
                "time": current_time
            }

            data.reviews.insert_one(newReview)
            flash("Your review has been submitted", "success")

    return redirect(url_for("whiskey", whiskey_name=whiskey_name))


@app.route("/delete_review/<whiskey_name>")
def delete_review(whiskey_name):
    if not session:
        return abort(403)

    data.reviews.remove({"username": session["username"], "drink": whiskey_name})
    flash("Your review has been deleted", "success")
    return redirect(url_for("whiskey", whiskey_name=whiskey_name))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
