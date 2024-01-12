from flask import render_template, request, redirect, flash, url_for
from trelawneycrafts import app, db
from trelawneycrafts.models import User, Category, Post, Reaction, Comment
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from hashlib import sha256

login_manager = LoginManager(app)
login_manager.login_view = 'log_in'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", title="Gallery")

@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    return render_template("upload.html", title="Create Post")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST": 
        new_username = request.form.get("username")
        new_email = request.form.get("email")
        hashed_password = sha256(request.form.get("password").encode("utf-8")).hexdigest()
        if User.query.filter_by(username=new_username).first() is None:
            if User.query.filter_by(email=new_email).first() is None:
                user = User(username=new_username, password=hashed_password, email=new_email)
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
    if request.method == "POST": 
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and (user.password == sha256(password.encode("utf-8")).hexdigest()):
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and password', 'danger')
            return render_template("login.html", title="Log In")
    else:
        return render_template("login.html", title="Log In")
    
@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    user = {
        "username": current_user.username,
        "email": current_user.email
    }
    if request.method == "GET": 
        
        return render_template("account.html", title=current_user.username, user=user)
    if request.method == "POST": 
        updated_username = request.form.get("username")
        updated_email = request.form.get("email")
        account = User.query.filter_by(id=current_user.id).first()
        
        if User.query.filter_by(username=updated_username).first() is None or updated_username == current_user.username:
            if User.query.filter_by(email=updated_email).first() is None or updated_email == current_user.email:
                if updated_username != user["username"]:
                    account.username = updated_username
                    user["username"] = updated_username
                if updated_email != user["email"]:
                    account.email = updated_email
                    user["email"] = updated_email
                login_user(account)
                db.session.commit()
                return render_template("account.html", title=current_user.username, user=user, error="f", message="Account updated successfully.")
            else:
                return render_template("account.html", title=current_user.username, user=user, error="t", message="That email is already in use.")
        else:
            return render_template("account.html", title=current_user.username, user=user, error="t", message="Username already taken. Please try a different one.")
    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))