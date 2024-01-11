"""Toute les routes et les Formulaires"""
import os
from .app import app, db
from .models import *
from .forms import *

from flask import jsonify, render_template, send_from_directory, url_for, redirect, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from datetime import datetime
# from fpdf import FPDF

@app.route("/")
def home():
    s = Spectateur.query.all()
    a = Artiste.query.all()
    return render_template("accueil.html", spectateurs=s, artistes=a)

@app.route("/admin/")
def admin_home():
    return render_template("admin.html")

@app.route("/accueil/")
def accueil():
    return render_template("accueil.html")

@app.route("/login/", methods = ("GET","POST",))
def login():
    f = LoginForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            if user.admin:
                next = f.next.data or url_for("admin_home")
            else:
                next = f.next.data or url_for("home")
            return redirect(next)
    return render_template (
        "login.html",
        form=f)

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/admin/ajout-billet/")
def ajout_billet():
    f = BilletForm()
    return render_template("ajout-billet.html", form=f)

@app.route("/admin/ajout-spectateur/")
def ajout_spectateur():
    f = SpectateurForm()
    return render_template("ajout-billet.html", form=f)