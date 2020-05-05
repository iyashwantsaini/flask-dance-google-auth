import os
from flask import Flask, redirect, url_for, flash, render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from .config import Config
from .models import db, login_manager
from .oauth import blueprint, google_logged_in
from .cli import create_db

# old app imports

# from flask import request
# from flask_ngrok import run_with_ngrok
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# from tika import parser
# from nlppreprocess import NLP
# from werkzeug.utils import secure_filename
# import arxiv
# import pandas as pd
# from gensim.summarization.summarizer import summarize
# import re
# # pip install pdfminer.six==20181108
# import io
# from transformers import pipeline
# nlp = pipeline('question-answering')
# app = Flask(__name__)
# obj = NLP()
# #summarizer = pipeline(task='summarization', model="t5-small")
# #
# run_with_ngrok(app)

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(blueprint, url_prefix="/login")
app.cli.add_command(create_db)
db.init_app(app)
login_manager.init_app(app)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/")
def index():
        # if google_logged_in:
        #     return render_template("dashboard.html")
        # else:
        return render_template("login.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/search_engine")
def search_engine():
    return render_template("search_engine.html")

@app.route("/wordcloud")
def wordcloud():
    return render_template("wordcloud.html")

@app.route("/summarization")
def summarization():
    return render_template("summarization.html")

@app.route("/qna")
def qna():
    return render_template("qna.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")
