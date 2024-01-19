from flask import current_app
from flask_wtf import FlaskForm

from wtforms import DateField, FileField, StringField, HiddenField, PasswordField, SelectField,\
RadioField, IntegerField, TextAreaField, EmailField, BooleanField, FloatField, DateField, TimeField
from wtforms.validators import DataRequired, NumberRange, Length
from .models import Utilisateur, Groupe, Concert, Lieu, SousStyle, Artiste


"Formulaires de l'application"

class BilletForm(FlaskForm):
    """Formulaire pour ajouter un billet"""
    typebillet = SelectField('Type Billet', validators=[DataRequired()], choices=[(1, 'Un jour Vendredi'), (2, 'Un jour Samedi'), (3, 'Un jour Dimanche'), (4, 'Totalité'), (5, 'Totalité + VIP')])
    prixbillet = FloatField('Prix Billet', validators=[DataRequired()], render_kw={'readonly': True})
    # jours = SelectField('Type Billet', validators=[DataRequired()], choices=[(1, 'Samedi'), (2, 'Dimanche'), (3, 'Lundi')])
    
class TypeBilletForm(FlaskForm):
    """Formulaire pour ajouter un billet"""
    typebillet = HiddenField('id')
    descbillet = StringField('Description Billet')
    prixbillet = IntegerField('Prix Billet')
    # jours = SelectField('Type Billet', validators=[DataRequired()], choices=[(1, 'Samedi'), (2, 'Dimanche'), (3, 'Lundi')])


class UtilisateurForm(FlaskForm):
    """Formulaire pour ajouter un UTILISATEUR"""
    iduser = HiddenField('id')
    nomuser = StringField('Nom', validators=[DataRequired()])
    ddn = DateField('Date de Naissance', validators=[DataRequired()])
    email = EmailField('Adresse Mail', validators=[DataRequired()])
    mdp = PasswordField('Mot de Passe', validators=[DataRequired()])
    admin = BooleanField('Admin')

class LoginForm(FlaskForm):
    """Formulaire pour se connecter"""
    email = StringField('Email', validators=[DataRequired()])
    mdp = PasswordField('Password')
    mdp_incorrect = ""
    next = HiddenField()

    def get_authenticated_user(self):
        user = Utilisateur.query.filter_by(email=self.email.data).first()
        if user and user.mdp == self.mdp.data:
            return user
    
    def has_content(self):
        return self.mdp.data != "" or self.email.data != ""
    
    def show_password_incorrect(self):
        self.mdp_incorrect = "Email ou mot de passe incorrect"


class StyleMusiqueForm(FlaskForm):
    recherche_groupe = StringField('Rechercher un groupe')
    choix_style_musical = SelectField('Style musical')

    def __init__(self, *args, **kwargs):
        super(StyleMusiqueForm, self).__init__(*args, **kwargs)

        # Récupérez tous les styles musicaux distincts de la base de données
        with current_app.app_context():
            styles_uniques = Groupe.query.with_entities(Groupe.stylemusical).distinct().all()

        # Ajoutez une option "Tous" à la liste des choix
        choix_styles = [('Tous', 'Tous')] + [(style[0], style[0]) for style in styles_uniques]

        # Créez le champ de formulaire avec les choix dynamiques
        self.choix_style_musical.choices = choix_styles
        

class ConcertForm(FlaskForm):
    jour = SelectField('Choisissez un jour', choices=[('Vendredi', 'Vendredi'), ('Samedi', 'Samedi'), ('Dimanche', 'Dimanche')])
    datec = DateField('Date Début', format='%Y-%m-%d', validators=[DataRequired()])
    timec = TimeField('Time Début', format='%H:%M:%S', validators=[DataRequired()])
    duree = FloatField('Durée (minutes)', validators=[DataRequired()])
    noml = SelectField('Choisir un lieu')
    
    def set_lieu_choices(self):
        self.noml.choices = [(row[0], row[0]) for row in Lieu.query.with_entities(Lieu.noml).all()]
        
class ArtisteForm(FlaskForm):
    idartiste = HiddenField('id')
    nomartiste = StringField('Nom', validators=[DataRequired()])
    prenomartiste = StringField('Prénom', validators=[DataRequired()])
    ddn = DateField('Date de Naissance', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    groupe = SelectField('Choisir un groupe')
    
    def set_groupe_choices(self):
        self.groupe.choices = [(g.idgroupe, g.nomgroupe) for g in Groupe.query.all()]
    
    
class GroupeForm(FlaskForm):
    idgroupe = HiddenField('id')
    nomgroupe = StringField('Nom de Groupe', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    lienvideo = StringField('Lien Vidéo', validators=[DataRequired()])
    stylemusical = SelectField('Choisir un style')
    
    def set_stylemusical_choices(self):
        self.stylemusical.choices = [(s.nomstyle, s.nomstyle) for s in SousStyle.query.all()]


class LieuForm(FlaskForm):
    noml = StringField('Nom de Lieu', validators=[DataRequired()])
    capacite = IntegerField('Capacité', validators=[DataRequired()])
    scene = BooleanField('Scene ?')
    
    
class ActiviteAnnexeForm(FlaskForm):
    idact = HiddenField('id')
    dateact = DateField('Date', validators=[DataRequired()])
    timeact = TimeField('Heure', validators=[DataRequired()])
    typeact = StringField('Type d\'activité', validators=[DataRequired()])
    dureeact = FloatField('Durée', validators=[DataRequired()])
    noml = SelectField('Lieu')
    
    def set_noml_choices(self):
        self.noml.choices = [(l.noml, l.noml) for l in Lieu.query.all()]