from flask import render_template, request, redirect, url_for, session
from trelawneycrafts import app, db
from trelawneycrafts.models import User, Category, Post, Reaction, Comment

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", title="Gallery")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        usernames = User.query.with_entities(User.username).all()
        emails = User.query.with_entities(User.email).all()
        print(f"Current Users: {usernames[0][0]}")
        print(f"Current Users: {emails[0][0]}")
        if request.form.get("username") not in usernames[0]:
            if request.form.get("email") not in emails[0]:
                user = User(username=request.form.get("username"), password=request.form.get("username"), email=request.form.get("email"))
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("log_in"))
            else:
                return render_template("register.html", title="Register", error="email")
        else:
            return render_template("register.html", title="Register", error="username")
    else:
        return render_template("register.html", title="Register")

@app.route("/log-in")
def log_in():
    return render_template("login.html", title="Log In")