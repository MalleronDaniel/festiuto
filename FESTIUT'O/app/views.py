"""Toute les routes et les Formulaires"""
import os
from .app import app, db
from .models import *
from .forms import *

from flask import jsonify, render_template, send_from_directory, url_for, redirect, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from datetime import datetime, time
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
# from fpdf import FPDF

@app.route("/")
def home():
    return redirect(url_for('accueil'))

@app.route("/admin/")
def admin_home():
    return render_template("admin.html")

@app.route("/accueil/")
def accueil():
    b=[db.session.query(Billet).first(),db.session.query(Billet).get(2)]
    c = db.session.query(Concert).first()
    return render_template("accueil.html", current_user=current_user, billets=b, concert=c)

@app.route("/burger/")
def burger():
    return render_template("burger.html")

@app.route("/festiut'o/")
def festival():
    return render_template("festival.html")

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


@app.route("/billetterie/")
@login_required
def billetterie():
    types_billets = Billet.get_types_billets()
    billets = Billet.query.filter(Billet.iduser.is_(None)).all()
    return render_template("billetterie/billetterie.html", types_billets=types_billets, billets=billets)

@app.route("/achatbillet/<int:type>")
@login_required
def achatbillet(type):
    billet = Billet.query.filter(Billet.typebillet == type).first()
    f = BilletForm()
    return render_template("billetterie/achat_billet.html", form=f, billet=billet)

@login_required
@app.route("/confirm-achatbillet/<int:type>")
def confirm_achatbillet(type):
    if(current_user.is_authenticated == False):
        return redirect(url_for('login'))
    user = current_user
    billet = Billet.query.filter(Billet.typebillet == type).first()
    b = Billet(
        typebillet = billet.typebillet,
        descbillet = billet.descbillet,
        prixbillet = billet.prixbillet,
        iduser = user.iduser
    )
    db.session.add(b)
    db.session.commit()
    return render_template("profil.html", user=current_user)

@app.route("/admin/ajout-billet/")
def ajout_billet():
    f = TypeBilletForm()
    b = db.session.query(Billet).all()
    return render_template("admin/ajout_billet.html", form=f, billets=b)

@app.route("/admin/ajout-billet/save/",  methods=["POST"])
def save_billet():
    f = TypeBilletForm()
    b = Billet(
        typebillet = db.session.query(func.max(Billet.typebillet)).scalar()+1,
        descbillet = f.descbillet.data,
        prixbillet = f.prixbillet.data
    )
    db.session.add(b)
    db.session.commit()
    flash(f'Félicitations ! L\'ajout de billet "<Billet ({b.typebillet}) | {b.typebillet}>" a été effectué avec succès.')
    return redirect(url_for('ajout_billet'))

@app.route("/admin/delete-billet/<int:typebillet>")
def delete_billet(typebillet):
    b = db.session.query(Billet).filter_by(typebillet=typebillet).first()
    if b:
        db.session.delete(b)
        db.session.commit()
    flash(f'Le type billet "f"<Billet ({b.typebillet}) | {b.typebillet}>"" a été supprimé.')
    return redirect(url_for('ajout_billet'))

@app.route("/admin/ajout-utilisateur/")
def ajout_utilisateur():
    f = UtilisateurForm()
    u = db.session.query(Utilisateur).all()
    return render_template("admin/ajout_utilisateur.html", form=f, utilisateurs=u)

@app.route("/admin/ajout-utilisateur/save/",  methods=("POST",))
def save_utilisateur():
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
    flash(f'Félicitations ! L\'ajout d\'utilisateur "<Utilisateur ({u.iduser}) | {u.nomuser}>" a été effectué avec succès.')
    return redirect(url_for('ajout_utilisateur'))

@app.route("/admin/delete-utilisateur/<int:iduser>")
def delete_utilisateur(iduser):
    u = db.session.query(Utilisateur).filter_by(iduser=iduser).first()
    if u:
        db.session.delete(u)
        db.session.commit()
    flash(f'L\'utilisateur "<Utilisateur ({u.iduser}) | {u.nomuser}>" a été supprimé.')
    return redirect(url_for('ajout_utilisateur'))

@app.route("/admin/ajout-concert/")
def ajout_concert():
    f = ConcertForm()
    f.set_lieu_choices()
    c = db.session.query(Concert).all()
    return render_template("admin/ajout_concert.html", form=f, concerts=c)

@app.route("/admin/ajout-concert/save/",  methods=("POST",))
def save_concert():
    f = ConcertForm()
    f.timec.data = time(12,0,0)
    datedebutc = datetime.combine(f.datec.data, f.timec.data)
    c = Concert(
        jour = f.jour.data,
        datedebutc = datedebutc,
        duree = f.duree.data,
        noml = f.noml.data,
        idconcert = db.session.query(func.max(Concert.idconcert)).scalar()+1
    )
    db.session.add(c)
    db.session.commit()
    flash(f'Félicitations ! L\'ajout de concert "<Concert ({c.idconcert}) | {c.datedebutc} | {c.jour}>" a été effectué avec succès.')
    return redirect(url_for('ajout_concert'))

@app.route("/admin/delete-concert/<int:idconcert>")
def delete_concert(idconcert):
    c = db.session.query(Concert).filter_by(idconcert=idconcert).first()
    if c:
        db.session.delete(c)
        db.session.commit()
    flash(f'Le concert "f"<Concert ({c.idconcert}) | {c.noml}>"" a été supprimé.')
    return redirect(url_for('ajout_concert'))

@app.route("/admin/ajout-groupe/")
def ajout_groupe():
    f = GroupeForm()
    f.set_stylemusical_choices()
    g = db.session.query(Groupe).all()
    return render_template("admin/ajout_groupe.html", form=f, groupes=g)

@app.route("/admin/ajout-groupe/save/",  methods=("POST",))
def save_groupe():
    f = GroupeForm()
    new_id = db.session.query(func.max(Groupe.idgroupe)).scalar()+1
    g = Groupe(
        nomgroupe = f.nomgroupe.data,
        description = f.description.data,
        lienvideo = f.lienvideo.data,
        stylemusical = f.stylemusical.data,
        idgroupe = new_id
    )
    db.session.add(g)
    
    db.session.commit()
    flash(f'Félicitations ! L\'ajout du groupe "f"<Groupe ({g.idgroupe}) | {g.nomgroupe}>"" a été effectué avec succès.')
    return redirect(url_for('ajout_groupe'))

@app.route("/admin/delete-groupe/<int:idgroupe>")
def delete_groupe(idgroupe):
    g = db.session.query(Groupe).filter_by(idgroupe=idgroupe).first()
    if g:
        db.session.delete(db.session.query(Contenir).filter_by(idgroupe=idgroupe).first())
        db.session.delete(g)
        db.session.commit()
    flash(f'Le groupe "f"<Groupe ({g.idgroupe}) | {g.nomgroupe}>"" a été supprimé.')
    return redirect(url_for('ajout_groupe'))
    

@app.route("/admin/ajout-artiste/")
def ajout_artiste():
    f = ArtisteForm()
    f.set_groupe_choices()
    a = db.session.query(Artiste).all()
    return render_template("admin/ajout_artiste.html", form=f, artistes=a)

@app.route("/admin/ajout-artiste/save/",  methods=("POST",))
def save_artiste():
    f = ArtisteForm()
    a = Artiste(
        nomartiste = f.nomartiste.data,
        prenomartiste = f.prenomartiste.data,
        ddn = f.ddn.data,
        descriptiona = f.description.data,
        idartiste = db.session.query(func.max(Artiste.idartiste)).scalar()+1,
        idgroupe = f.groupe.data
    )
    db.session.add(a)
    db.session.commit()
    flash(f'Félicitations ! L\'ajout de l\'artiste "f"<Artiste ({a.idartiste}) | {a.prenomartiste} {a.nomartiste}>"" a été effectué avec succès.')
    return redirect(url_for('ajout_artiste'))

@app.route("/admin/delete-artiste/<int:idartiste>")
def delete_artiste(idartiste):
    a = db.session.query(Artiste).filter_by(idartiste=idartiste).first()
    if a:
        db.session.delete(a)
        db.session.commit()
    flash(f'L\'artiste "f"<Artiste ({a.idartiste}) | {a.prenomartiste} {a.prenomartiste}>"" a été supprimé.')
    return redirect(url_for('ajout_artiste'))

@app.route("/admin/ajout-lieu/")
def ajout_lieu():
    f = LieuForm()
    l = db.session.query(Lieu).all()
    return render_template("admin/ajout_lieu.html", form=f, lieux=l)

@app.route("/admin/ajout-lieu/save/",  methods=("POST",))
def save_lieu():
    f = LieuForm()
    l = Lieu(
        noml = f.noml.data,
        capacite = f.capacite.data,
        scene = f.scene.data
    )
    db.session.add(l)
    db.session.commit()
    flash(f'Félicitations ! L\'ajout de lieu "f"<Lieu ({l.capacite}) | {l.noml}>"" a été effectué avec succès.')
    return redirect(url_for('ajout_lieu'))

@app.route("/admin/delete-lieu/<string:noml>")
def delete_lieu(noml):
    l = db.session.query(Lieu).filter_by(noml=noml).first()
    if l:
        db.session.delete(l)
        db.session.commit()
    flash(f'Le lieu "<Lieu ({l.capacite}) | {l.noml}>"" a été supprimé.')
    return redirect(url_for('ajout_lieu'))

@app.route("/admin/ajout-activite-annexe/")
def ajout_activite_annexe():
    f = ActiviteAnnexeForm()
    f.set_noml_choices()
    aa = db.session.query(ActiviteAnnexe).all()
    return render_template("admin/ajout_activite_annexe.html", form=f, activites=aa)

@app.route("/admin/ajout-activite-annexe/save/",  methods=("POST",))
def save_activite_annexe():
    f = ActiviteAnnexeForm()
    dateact = datetime.combine(f.dateact.data, f.timeact.data)
    aa = ActiviteAnnexe(
        idact = db.session.query(func.max(ActiviteAnnexe.idact)).scalar()+1,
        dateact = dateact,
        typeact = f.typeact.data,
        dureeact = f.dureeact.data,
        noml = f.noml.data
    )
    db.session.add(aa)
    db.session.commit()
    flash(f'Félicitations ! L\'ajout de l\'activité annexe "f"<ActiviteAnnexe ({aa.idact}) | {aa.dateact} {aa.noml}>"" a été effectué avec succès.')
    return redirect(url_for('ajout_activite_annexe'))

@app.route("/admin/delete-activite-annexe/<int:idact>")
def delete_activite_annexe(idact):
    aa = db.session.query(ActiviteAnnexe).filter_by(idact=idact).first()
    if aa:
        db.session.delete(aa)
        db.session.commit()
    flash(f'L\'activité annexe "f"<ActiviteAnnexe ({aa.idact}) | {aa.dateact} {aa.noml}>"" a été supprimé.')
    return redirect(url_for('ajout_activite_annexe'))

@app.route("/save/billeterie/",  methods=("POST",))
def save_billeterie():
    f = BilletForm()
    p = Billet(
        typebillet = f.typebillet.data[0],
        descbillet = f.typebillet.data[1],
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
    return render_template("details/details-concert.html", 
    concert=c)

@app.route("/details-groupe/<int:id>")
def details_groupe(id):
    g = Groupe.query.get(id)
    return render_template("details/details-groupe.html", 
    groupe=g)

@app.route("/details-artiste/<int:id>")
def details_artiste(id):
    a = Artiste.query.get(id)
    groupe = Groupe.query.get(a.idgroupe)
    return render_template("details/details-artiste.html", 
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
    style_selectionne = None
    terme_recherche = None

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
        return render_template("groupes.html", groupes=groupes_filtres, form=form)

    groupes = Groupe.query.all()

    return render_template("groupes.html", groupes=groupes, form=form)
@login_required
@app.route("/profil")
def profil():
    if(current_user.is_authenticated == False):
        return redirect(url_for('login'))
    user = current_user
    groupesFavoris = db.session.query(Groupe).join(Apprecier).filter(Apprecier.iduser == user.iduser).all()
    billets = db.session.query(Billet).filter(Billet.iduser == user.iduser).all()
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
