"""Toute les routes et les Formulaires"""
import os
from .app import app, db
from .models import *
from .forms import *

from flask import jsonify, render_template, send_from_directory, url_for, redirect, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import jsonify
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

@app.route("/festiut'o/")
def festival():
    return render_template("festival.html")

@app.route("/billetterie/")
def billetterie():
    c = Concert.query.all()
    jourConcerts = Concert.query.with_entities(Concert.jour).distinct().all();
    jourConcertsDistinct = [jour[0] for jour in jourConcerts];
    concerts_vendredi = Concert.query.filter(Concert.jour == "Vendredi").order_by(Concert.datedebutc).all();
    concerts_samedi = Concert.query.filter((Concert.jour) == "Samedi").order_by(Concert.datedebutc).all();
    concerts_dimanche = Concert.query.filter((Concert.jour) == "Dimanche").order_by(Concert.datedebutc).all();
    
    return render_template("billetterie/base_billetterie.html", joursConcerts = jourConcertsDistinct, concerts_vendredi=concerts_vendredi, concerts_samedi=concerts_samedi, concerts_dimanche=concerts_dimanche, c = c)

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
    
@app.route("/save/inscription/", methods=("POST",))
def save_inscription():
    f = UtilisateurForm()
    if(Utilisateur.query.filter_by(email=f.email.data).all()):
        flash(f'Erreur ! Un utilisateur avec cette adresse mail existe déjà.')
        return redirect(url_for('inscription'))
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

@login_required
@app.route("/billeterie/")
def billeterie():
    f = BilletForm()
    return render_template("billeterie.html", form=f)

@app.route("/admin/ajout_billet/")
def ajout_billet():
    f = BilletForm()
    return render_template("ajout_billet.html", form=f)

@app.route("/admin/ajout-UTILISATEUR/")
def ajout_spectateur():
    f = UtilisateurForm()
    return render_template("admin/ajout_utilisateur.html", form=f)

@app.route("/admin/ajout-concert/")
def ajout_concert():
    return render_template("admin/ajout_concert.html")

@app.route("/admin/ajout-groupe/")
def ajout_groupe():
    return render_template("admin/ajout_groupe.html")

@app.route("/admin/ajout-artiste/")
def ajout_artiste():
    return render_template("admin/ajout_artiste.html")

@app.route("/save/billeterie/",  methods=("POST",))
def save_billeterie():
    f = BilletForm()
    p = Posseder(
        typebillet = f.typebillet.data[0],
        iduser = current_user.iduser
    )
    db.session.add(p)
    db.session.commit()
    flash(f'Félicitations ! Votre achat de billet "{Billet.query.get(f.typebillet.data).descbillet}" a été effectué avec succès.')
    return redirect(url_for('billeterie'))

@app.route("/programme/")
def programme():
    c = Concert.query.all()
    jourConcerts = Concert.query.with_entities(Concert.jour).distinct().all();
    jourConcertsDistinct = [jour[0] for jour in jourConcerts];
    concerts_vendredi = Concert.query.filter(Concert.jour == "Vendredi").order_by(Concert.datedebutc).all();
    concerts_samedi = Concert.query.filter((Concert.jour) == "Samedi").order_by(Concert.datedebutc).all();
    concerts_dimanche = Concert.query.filter((Concert.jour) == "Dimanche").order_by(Concert.datedebutc).all();
    
    return render_template("programme/base_programme.html", joursConcerts = jourConcertsDistinct, 
                           concerts_vendredi=concerts_vendredi,
                           concerts_samedi=concerts_samedi,
                           concerts_dimanche=concerts_dimanche,
                           c=c)

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
    groupe = Groupe.query.get(a.idgroupe)
    return render_template("details-artiste.html", 
    artiste=a,
    groupe=groupe)

@login_required
@app.route("/inputFavoris/<int:id_groupe>", methods=["POST"])
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

@app.route("/groupes/", methods=["GET", "POST"])
def groupes():
    form = StyleMusiqueForm()

    if form.validate_on_submit():
        style_selectionne = request.form.get("choix_style_musical")
        terme_recherche = form.recherche_groupe.data

        if style_selectionne and style_selectionne != 'Tous':
            groupes_filtres = Groupe.query.filter_by(stylemusical=style_selectionne).all()
        else:
            groupes_filtres = Groupe.query.all()

        if terme_recherche:
            groupes_filtres = [groupe for groupe in groupes_filtres if terme_recherche.lower() in groupe.nomgroupe.lower()]

        if request.method == "POST":
            noms_groupes = [groupe.nomgroupe for groupe in groupes_filtres]
            return jsonify({"groupes": noms_groupes})

    groupes = Groupe.query.all()

    return render_template("groupes.html", groupes=groupes, form=form)

@login_required
@app.route("/profil")
def profil():
    if(current_user.is_authenticated == False):
        return redirect(url_for('login'))
    user = current_user
    groupesFavoris = db.session.query(Groupe).join(Apprecier).filter(Apprecier.iduser == user.iduser).all()
    billets = db.session.query(Billet).join(Posseder).filter(Posseder.iduser == user.iduser).all()
    return render_template("profil.html", user=user, 
                           groupesFavoris=groupesFavoris,
                           billets=billets)

#Fonction utile



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