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
        user = User(username=request.form.get("username"), password=request.form.get("username"), email=request.form.get("email"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("log_in"))
    else:
        return render_template("register.html", title="Register")

@app.route("/log-in")
def log_in():
    return render_template("login.html", title="Log In")