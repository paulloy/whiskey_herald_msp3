import os
from flask import (
    Flask, render_template, flash, redirect, request, session, url_for, json
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# get collections
coll = mongo.db


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/add_whiskey", methods=["GET", "POST"])
def add_whiskey():
    if request.method == "POST":
        existing_drink = coll.drinks.find_one(
            {"drink": request.form.get("whiskey-name").lower()}
        )

        if existing_drink:
            flash("This drink already exists", "error")
            return redirect(url_for("add_whiskey"))

        formSubmission = {
            "drink": request.form.get("whiskey-name"),
            "image_location": "img/w4.png",
            "type": request.form.get("whiskey-type"),
            "description": request.form.get("description"),
            "average_score": "number"
        }

        coll.drinks.insert_one(formSubmission)
        flash("This drink has been added to Whiskey Herald", "success")

    return render_template("add-whiskey.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_username = coll.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        existing_email = coll.users.find_one(
            {"email": request.form.get("email").lower()}
        )

        if existing_username:
            flash("This username is unavailable, please try another.", "error")
            return redirect(url_for("register"))
        elif existing_email:
            flash("This email is unavailable, please try another.", "error")
            return redirect(url_for("register"))

        # dictionary for inserting a new user to users collection
        newUser = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password")),
            "bio": "Tell us more about yourself :)",
            "profile_pic": "DEFAULT"
        }

        coll.users.insert_one(newUser)

        flash("Registration successful, thanks for joining! \
            You can now login.", "success")

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = coll.users.find_one(
            {"email": request.form.get("email")}
        )

        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                current_user = mongo.db.users.find_one(
                    {"email": request.form.get("email")}
                )

                session["email"] = current_user["email"]
                session["username"] = current_user["username"]

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
    user = coll.users.find_one(
        {"username": username}
    )

    userDetails = {
        "username": user["username"],
        "bio": user["bio"],
        "profile_pic": user["profile_pic"]
    }

    user_reviews = coll.reviews.find({"username": username})

    return render_template("profile.html", username=username, userDetails=userDetails, user_reviews=user_reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search")
    results = list(coll.drinks.find({"$text": {"$search": query}}))

    searched_value = request.form.get("search")

    return render_template("search.html", results=results, searched_value=searched_value)


@app.route("/whiskey/<whiskey_name>")
def whiskey(whiskey_name):
    find_whiskey = coll.drinks.find_one({"drink": whiskey_name})
    find_reviews = coll.reviews.find({"drink": whiskey_name})
    find_average_score = coll.reviews.find({"drink": whiskey_name})

    average_score = 0
    if find_average_score.count() != 0:
        for doc in find_average_score:
            average_score = average_score + int(doc["score"])
        average_score = int(round(average_score / find_average_score.count()))

    whiskeyDetails = {
        "_id": find_whiskey["_id"],
        "drink": find_whiskey["drink"],
        "image_location": find_whiskey["image_location"],
        "type": find_whiskey["type"],
        "description": find_whiskey["description"]
    }

    return render_template("whiskey.html", whiskeyDetails=whiskeyDetails, find_reviews=find_reviews, average_score=average_score)


@app.route("/review/<whiskey_name>", methods=["GET", "POST"])
def review(whiskey_name):
    existing_review = coll.reviews.find_one({"username": session["username"], "drink": whiskey_name})

    if request.method == "POST":
        if existing_review:
            reviewUpdate = {
                "username": session["username"],
                "drink": whiskey_name,
                "title": request.form.get("review-title"),
                "review": request.form.get("review"),
                "score": request.form.get("score")
            }

            coll.reviews.update({"username": session["username"], "drink": whiskey_name}, reviewUpdate)
            flash("Your review has been updated", "success")

        else:
            newReview = {
                "username": session["username"],
                "drink": whiskey_name,
                "title": request.form.get("review-title"),
                "review": request.form.get("review"),
                "score": request.form.get("score")
            }

            coll.reviews.insert_one(newReview)
            flash("Your review has been submitted", "success")

    return redirect(url_for("whiskey", whiskey_name=whiskey_name))


@app.route("/delete_review/<whiskey_name>")
def delete_review(whiskey_name):
    mongo.db.reviews.remove({"username": session["username"], "drink": whiskey_name})
    flash("Your review has been deleted", "success")
    return redirect(url_for("whiskey", whiskey_name=whiskey_name))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
