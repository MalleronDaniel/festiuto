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
    concerts_vendredi = Concert.query.filter(Concert.jour == "Vendredi").order_by(Concert.datedebutc).all();
    concerts_samedi = Concert.query.filter((Concert.jour) == "Samedi").order_by(Concert.datedebutc).all();
    concerts_dimanche = Concert.query.filter((Concert.jour) == "Dimanche").order_by(Concert.datedebutc).all();
    
    return render_template("programme.html", 
                           concerts_vendredi=concerts_vendredi,
                           concerts_samedi=concerts_samedi,
                           concerts_dimanche=concerts_dimanche)

@app.route("/details-concert/<int:id>")
def details_concert(id):
    c = Concert.query.get(id)
    return render_template("details-concert.html", 
    concert=c)

@app.route("/details-groupe/<int:id>")
def details_groupe(id):
    g = Groupe.query.get(id)
    return render_template("details-groupe.html", 
    groupe=g)

@app.route("/details-artiste/<int:id>")
def details_artiste(id):
    a = Artiste.query.get(id)
    groupe = Groupe.query.get(a.groupe_id)
    return render_template("details-artiste.html", 
    artiste=a,
    groupe=groupe)

@app.route("/inputFavoris/<int:id_groupe>", methods=["POST"])
@login_required
def inputFavoris(id_groupe):
    # Vérifie si le groupe est déjà en favori pour l'utilisateur
    est_favori = Apprecier.query.filter_by(iduser=current_user.username, idgroupe=id_groupe).first()
    
    if est_favori:
        # Si le groupe est déjà en favori, le supprimer
        db.session.delete(est_favori)
        db.session.commit()
    else:
        # Sinon, l'ajouter en favori
        favori = Apprecier(iduser=current_user.username, idgroupe=id_groupe)
        db.session.add(favori)
        db.session.commit()

    #Permet de récupérer la page précédente
    page_precedente = request.referrer if request.referrer else url_for('accueil')
    return redirect(page_precedente)



#Fonction utile

