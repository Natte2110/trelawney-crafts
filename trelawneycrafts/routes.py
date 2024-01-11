from flask import render_template, request, redirect, flash, url_for
from trelawneycrafts import app, db
from trelawneycrafts.models import User, Category, Post, Reaction, Comment
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(User.id))

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", title="Gallery")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST": 
        usernames = [t[0] for t in list(User.query.with_entities(User.username).all())]
        emails = [t[0] for t in list(User.query.with_entities(User.email).all())]
        print(f"Current Users: {usernames}")
        print(f"Current Users: {emails}")
        if request.form.get("username") not in usernames:
            if request.form.get("email") not in emails:
                user = User(username=request.form.get("username"), password=request.form.get("password"), email=request.form.get("email"))
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("log_in"))
            else:
                return render_template("register.html", title="Register", error="email")
        else:
            return render_template("register.html", title="Register", error="username")
    else:
        return render_template("register.html", title="Register")

@app.route("/log-in", methods=["GET", "POST"])
def log_in():
   
    return render_template("login.html", title="Log In")