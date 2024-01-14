from flask import current_app
from flask_wtf import FlaskForm
from wtforms import DateField, FileField, StringField, HiddenField, PasswordField, SelectField, RadioField, IntegerField, TextAreaField, EmailField, BooleanField
from wtforms.validators import DataRequired, NumberRange
from .models import Utilisateur, Groupe

"Formulaires de l'application"

class BilletForm(FlaskForm):
    """Formulaire pour ajouter un billet"""
    pass

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
    email = StringField('Email')
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