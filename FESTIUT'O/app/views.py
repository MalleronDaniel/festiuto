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
    s = UTILISATEUR.query.all()
    a = Artiste.query.all()
    return render_template("home.html", spectateurs=s, artistes=a)

@app.route("/admin/ajout-billet/")
def ajout_billet():
    f = BilletForm()
    return render_template("ajout-billet.html", form=f)

@app.route("/admin/ajout-UTILISATEUR/")
def ajout_spectateur():
    f = SpectateurForm()
    return render_template("ajout-billet.html", form=f)

@app.route("/programme/")
def programme():
    c = Concert.query.all()
    concerts_vendredi = Concert.query.filter(Concert.jour == "Vendredi").order_by(Concert.datedebutc).all();
    concerts_samedi = Concert.query.filter((Concert.jour) == "Samedi").order_by(Concert.datedebutc).all();
    concerts_dimanche = Concert.query.filter((Concert.jour) == "Dimanche").order_by(Concert.datedebutc).all();
    
    return render_template("programme.html", concerts_vendredi=concerts_vendredi, concerts_samedi=concerts_samedi, concerts_dimanche=concerts_dimanche, c = c)