from flask import render_template
from trelawneycrafts import app, db
from trelawneycrafts.models import User, Category, Post, Reaction, Comment

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", title="Gallery")