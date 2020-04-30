import os
from flask import Flask, redirect, url_for, flash, render_template
from flask_login import login_required, logout_user
from .config import Config
from .models import db, login_manager
from .oauth import blueprint, google_logged_in
from .cli import create_db

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
        if google_logged_in:
            return render_template("dashboard.html")
        else:
            return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

