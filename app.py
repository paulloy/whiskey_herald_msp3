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


@app.route("/add_whiskey")
def add_whiskey():
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
            "username": request.form.get("username").lower(),
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


@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/whiskey")
def whiskey():
    return render_template("whiskey.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
