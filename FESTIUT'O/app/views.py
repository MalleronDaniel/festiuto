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
    s = Utilisateur.query.all()
    a = Artiste.query.all()
    return render_template("accueil.html", spectateurs=s, artistes=a)

@app.route("/admin/")
def admin_home():
    return render_template("admin.html")

@app.route("/accueil/")
def accueil():
    return render_template("accueil.html")

@app.route("/burger/")
def burger():
    return render_template("burger.html")

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

@app.route('/inscription/')
def inscription():
    f = UtilisateurForm()
    return render_template("inscription.html", form=f)
    
@app.route("/save/util/", methods=("POST",))
def save_inscription():
    f = UtilisateurForm()
    u = Utilisateur(
        iduser = 1 + db.session.query(db.func.max(Utilisateur.iduser)).scalar(),
        nomuser = f.nomuser.data,
        ddn = f.ddn.data,
        email = f.email.data,
        mdp = f.mdp.data,
        admin = f.admin.data
    )
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('login'))

@app.route("/admin/ajout-billet/")
def ajout_billet():
    f = BilletForm()
    return render_template("ajout-billet.html", form=f)

@app.route("/admin/ajout-UTILISATEUR/")
def ajout_spectateur():
    f = UtilisateurForm()
    return render_template("ajout-billet.html", form=f)

@app.route("/programme/")
def programme():
    c = Concert.query.all()
    jourConcerts = Concert.query.with_entities(Concert.jour).distinct().all();
    jourConcertsDistinct = [jour[0] for jour in jourConcerts];
    concerts_vendredi = Concert.query.filter(Concert.jour == "Vendredi").order_by(Concert.datedebutc).all();
    concerts_samedi = Concert.query.filter((Concert.jour) == "Samedi").order_by(Concert.datedebutc).all();
    concerts_dimanche = Concert.query.filter((Concert.jour) == "Dimanche").order_by(Concert.datedebutc).all();
    
    return render_template("programme/base_programme.html", joursConcerts = jourConcertsDistinct, concerts_vendredi=concerts_vendredi, concerts_samedi=concerts_samedi, concerts_dimanche=concerts_dimanche, c = c)

@app.route("/programme/Vendredi")
def programme_vendredi():
    c = Concert.query.all()
    jourConcerts = Concert.query.with_entities(Concert.jour).distinct().all();
    jourConcertsDistinct = [jour[0] for jour in jourConcerts];
    concerts_vendredi = Concert.query.filter(Concert.jour == "Vendredi").order_by(Concert.datedebutc).all();
    
    return render_template("programme/programme_vendredi.html", joursConcerts = jourConcertsDistinct, concerts_vendredi= concerts_vendredi, c = c)

@app.route("/programme/Samedi")
def programme_samedi():
    c = Concert.query.all()
    jourConcerts = Concert.query.with_entities(Concert.jour).distinct().all();
    jourConcertsDistinct = [jour[0] for jour in jourConcerts];
    concerts_samedi = Concert.query.filter((Concert.jour) == "Samedi").order_by(Concert.datedebutc).all();
    
    return render_template("programme/programme_samedi.html", joursConcerts = jourConcertsDistinct, concerts_samedi= concerts_samedi, c = c)

@app.route("/programme/Dimanche")
def programme_dimanche():
    c = Concert.query.all()
    jourConcerts = Concert.query.with_entities(Concert.jour).distinct().all();
    jourConcertsDistinct = [jour[0] for jour in jourConcerts];
    concerts_dimanche = Concert.query.filter((Concert.jour) == "Dimanche").order_by(Concert.datedebutc).all();
    
    return render_template("programme/programme_samedi.html", joursConcerts = jourConcertsDistinct, concerts_dimanche = concerts_dimanche, c = c)