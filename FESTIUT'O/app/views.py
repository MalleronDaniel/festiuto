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
    return render_template("home.html", spectateurs=s, artistes=a)

@app.route("/admin/ajout-billet/")
def ajout_billet():
    f = BilletForm()
    return render_template("ajout-billet.html", form=f)

@app.route("/admin/ajout-spectateur/")
def ajout_spectateur():
    f = SpectateurForm()
    return render_template("ajout-billet.html", form=f)