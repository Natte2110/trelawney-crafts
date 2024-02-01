from flask import render_template, request, redirect, flash, url_for, jsonify
from trelawneycrafts import app, db
from trelawneycrafts.models import User, Category, Post, Reaction, Comment
import flask_login as fl
from hashlib import sha256
from datetime import datetime
from sqlalchemy import desc
import os

login_manager = fl.LoginManager(app)
login_manager.login_view = 'log_in'
PATH_TO_IMAGES = '/'.join(app.config['UPLOAD_FOLDER'].split("/")[-2:])


@login_manager.user_loader
def load_user(id):
    """Loads the current user and returns it as a query object.

    Arguments:
        id -- The id of the user, this will be used to search the USER database table for the corresponding entry.

    Returns:
        A User object returned from a query on the User table.
    """
    return User.query.get(int(id))


@app.route("/")
def home():
    """Provides routing for the website's home page

    Returns:
        The index.html page with the title of "Home"
    """
    return render_template("index.html", title="Home")


@app.route("/check_login")
def check_login():
    """Used to check whether the current users session is available.

    Returns:
        If the user is not logged in, they will be redirected to the log in page.
    """
    if fl.current_user.id is None:
        return redirect(url_for('log_in'))
    else:
        return False


@app.route("/gallery")
def gallery():
    """Runs a query to retrieve all user posts, and attributes to each one the poster ID, its reactions and the comment count.

    Returns:
        The gallery.html page with the attributed posts as objects.
    """
    categories = list(Category.query.order_by(Category.category_name).all())
    posts = list(Post.query.order_by(desc(Post.id)).all())
    for post in posts:
        post.user = User.query.filter_by(id=post.user_id).first().username
        count_likes = Reaction.query.filter_by(post_id=post.id).all()
        count_comments = Comment.query.filter_by(post_id=post.id).all()
        post.category = Category.query.filter_by(
            id=post.category_id).first().category_name
        user_ids = [
            user_id[0] for user_id in
            db.session.query(Reaction.user_id).filter_by(post_id=post.id).all()]
        if count_likes is not None:
            post.like_count = len(count_likes)
            post.liked_by = user_ids
        else:
            post.like_count = 0
            post.liked_by = 0
        if count_comments is not None:
            post.comment_count = len(count_comments)
        else:
            post.comment_count = 0
    return render_template(
        "gallery.html",
        title="Gallery",
        posts=posts,
        path=PATH_TO_IMAGES,
        categories=categories)


@app.route("/reaction_count/<int:post_id>", methods=["GET", "POST"])
def reaction_count(post_id):
    """Gets the number of reactions on a given post.

    Arguments:
        post_id -- The id of the post to be checked

    Returns:
        An integer pertaining to the number of Reaction entries attributed to that post ID
    """
    count = Reaction.query.filter_by(post_id=post_id).all()
    if count is not None:
        return str(len(count))
    else:
        return "0"


@app.route("/add_reaction/<int:post_id>", methods=["GET", "POST"])
@fl.login_required
def add_reaction(post_id):
    """Adds a reaction to the chosen post.

    Arguments:
        post_id -- The ID of the post to have a reaction added to it.

    Returns:
        The gallery.html page.
    """
    reaction = Reaction(
        date=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        user_id=fl.current_user.id,
        post_id=post_id)
    db.session.add(reaction)
    db.session.commit()
    return redirect(url_for('gallery'))


@app.route("/get_comments/<int:post_id>")
def get_comments(post_id):
    """Retrieves all comments that are related to a specific post.

    Arguments:
        post_id -- The ID of the post that will be queried to return comments.

    Returns:
        A JSON Object containing information about all comments on the post.
    """
    comments = Comment.query.filter_by(post_id=post_id).all()
    count_comments = Comment.query.filter_by(post_id=post_id).all()
    if fl.current_user.is_authenticated:
        current_user_id = fl.current_user.id
    else:
        current_user_id = None
    comments_list = [
        {"current_user":current_user_id},
        [
        {'id': comment.id,
         'content': comment.content,
         'user': User.query.filter_by(id=comment.user_id).first().username,
         'userid': comment.user_id,
         'date': comment.date,
         'count': len(count_comments)
         } for comment in comments]
    ]
    
    return jsonify(comments_list)


@app.route("/add_comment/<int:post_id>", methods=["GET", "POST"])
@fl.login_required
def add_comment(post_id):
    """Adds a comment entry into the comments database table

    Arguments:
        post_id -- The ID of the post which will be linked to the comment.

    Returns:
        The path to the gallery page.
    """
    data = request.json
    comment_content = data.get('commentContent')
    comment = Comment(
        date=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        user_id=fl.current_user.id,
        post_id=post_id,
        content=comment_content)
    db.session.add(comment)
    db.session.commit()
    return jsonify({"success":True })

@app.route("/remove_comment/<int:comment_id>", methods=["GET", "POST"])
@fl.login_required
def remove_comment(comment_id):
    """Deletes a comment from a post

    Arguments:
        comment_id -- The ID of the comment which will be removed.

    Returns:
        The path to the gallery page.
    """
    comment = Comment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"success":True })


@app.route("/remove_reaction/<int:post_id>", methods=["GET", "POST"])
@fl.login_required
def remove_reaction(post_id):
    """Removes a reaction from a given post.

    Arguments:
        post_id -- The ID of the post that will have the reaction removed.

    Returns:
        The gallery page
    """
    reaction = Reaction.query.filter_by(post_id=post_id, user_id=fl.current_user.id).first()
    db.session.delete(reaction)
    db.session.commit()
    return redirect(url_for('gallery'))


@app.route("/upload", methods=["GET", "POST"])
@fl.login_required
def upload():
    """Allows a user to upload a picture and information regarding their own post. Stores the uploaded picture locally.

    Returns:
        The upload page if GET, or the gallery page if the user submits a post.
    """
    if request.method == "POST":
        if 'image' not in request.files:
            return redirect(request.url)
        image = request.files['image']
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        post = Post(
            date=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            user_id=fl.current_user.id,
            image_url=image.filename,
            category_id=request.form.get("category"),
            content=request.form.get("content"),
            title=request.form.get("title")
            )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('gallery'))
    else:
        categories = list(Category.query.order_by(Category.category_name).all())
        return render_template("upload.html", title="Create Post", categories=categories)


@app.route("/delete_post/<int:post_id>", methods=["GET", "POST"])
def delete_post(post_id):
    """Deletes a post with the chosen post ID

    Arguments:
        post_id -- The ID of the post that will be deleted.

    Returns:
        The gallery page.
    """
    post = Post.query.filter_by(id=post_id).first()
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], post.image_url)):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], post.image_url))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('gallery'))


@app.route("/register", methods=["GET", "POST"])
def register():
    """Allows a new user to register for an account on the site 
    and stores their information within the 'user' table.

    Returns:
        The login page upon successfil registration
    """
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
    """Handles user logins by checking if the details are within the the user table.

    Returns:
        The home page upon successful login.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and (user.password == sha256(password.encode("utf-8")).hexdigest()):
            fl.login_user(user)
            return redirect(url_for('home'))
        else:
            return render_template("login.html", title="Log In", error="t")
    else:
        return render_template("login.html", title="Log In")


@app.route("/account", methods=["GET", "POST"])
@fl.login_required
def account():
    """Handles user account updating by changing their database entry.

    Returns:
        An updated account page.
    """
    user = {
        "username": fl.current_user.username,
        "email": fl.current_user.email
    }
    if request.method == "GET":
        return render_template("account.html", title=fl.current_user.username, user=user)
    if request.method == "POST":
        updated_username = request.form.get("username")
        updated_email = request.form.get("email")
        account = User.query.filter_by(id=fl.current_user.id).first()

        if User.query.filter_by(username=updated_username).first() is None or updated_username == fl.current_user.username:
            if User.query.filter_by(email=updated_email).first() is None or updated_email == fl.current_user.email:
                if updated_username != user["username"]:
                    account.username = updated_username
                    user["username"] = updated_username
                if updated_email != user["email"]:
                    account.email = updated_email
                    user["email"] = updated_email
                fl.login_user(account)
                db.session.commit()
                return render_template(
                    "account.html",
                    title=fl.current_user.username,
                    user=user,
                    error="f",
                    message="Account updated successfully.")
            else:
                return render_template(
                    "account.html",
                    title=fl.current_user.username,
                    user=user, error="t",
                    message="That email is already in use.")
        else:
            return render_template(
                "account.html",
                title=fl.current_user.username,
                user=user,
                error="t",
                message="Username already taken. Please try a different one.")

@app.route("/delete-account", methods=["POST"])
@fl.login_required
def delete_account():
    
    posts = Post.query.filter_by(user_id=fl.current_user.id).all()
    for post in posts:
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], post.image_url)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], post.image_url))
    data = request.json
    password = data.get('password')
    user = User.query.filter_by(id=fl.current_user.id).first()
    if sha256(password.encode("utf-8")).hexdigest() == user.password:
        fl.logout_user()
        db.session.delete(user)
        db.session.commit()
        return {"success":True}
    else:
        return {"success":False}

@app.route("/logout")
@fl.login_required
def logout():
    """Logs the user out of their account

    Returns:
        The home page.
    """
    fl.logout_user()
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500