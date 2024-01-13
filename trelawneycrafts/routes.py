from flask import render_template, request, redirect, flash, url_for
from trelawneycrafts import app, db
from trelawneycrafts.models import User, Category, Post, Reaction, Comment
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from hashlib import sha256
from datetime import datetime
import os

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
    posts = list(Post.query.order_by(Post.date).all())
    for post in posts:
        post.user = User.query.filter_by(id=post.user_id).first().username
    for post in posts:
        count = Reaction.query.filter_by(post_id=post.id).all()
        user_ids = [user_id[0] for user_id in db.session.query(Reaction.user_id).filter_by(post_id=post.id).all()]
        if count is not None:
            post.like_count = len(count)
            post.liked_by = user_ids
        else:
            post.like_count = 0
            post.liked_by = 0
    path_to_images = '/'.join(app.config['UPLOAD_FOLDER'].split("/")[-2:])
    return render_template("gallery.html", title="Gallery", posts=posts, path=path_to_images)

@app.route("/reaction_count/<int:post_id>", methods=["GET", "POST"])
def reaction_count(post_id):
    print(post_id, current_user.id)
    count = Reaction.query.filter_by(post_id=post_id).all()
    if count is not None:
        return str(len(count))
    else:
        return "0"

@app.route("/add_reaction/<int:post_id>", methods=["GET", "POST"])
@login_required
def add_reaction(post_id):
    print(post_id, current_user.id)
    reaction = Reaction(
        date=datetime.today().strftime('%Y-%m-%d %H:%M:%S'), 
        user_id=current_user.id, 
        post_id=post_id)
    db.session.add(reaction)
    db.session.commit()
    return redirect(url_for('gallery'))

@app.route("/remove_reaction/<int:post_id>", methods=["GET", "POST"])
@login_required
def remove_reaction(post_id):
    reaction = Reaction.query.filter_by(post_id=post_id, user_id=current_user.id).first()
    db.session.delete(reaction)
    db.session.commit()
    return redirect(url_for('gallery'))

@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST": 
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        image = request.files['image'] 
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        post = Post(
            date=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            user_id = current_user.id,
            image_url = image.filename,
            category_id = request.form.get("category"),
            content = request.form.get("content"),
            title = request.form.get("title")
            )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('gallery'))
    else:
        categories = list(Category.query.order_by(Category.category_name).all())
        return render_template("upload.html", title="Create Post", categories=categories)

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