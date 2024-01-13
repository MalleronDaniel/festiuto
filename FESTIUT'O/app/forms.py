from flask_wtf import FlaskForm
from wtforms import DateField, FileField, StringField, HiddenField, PasswordField, SelectField, RadioField, IntegerField, TextAreaField, EmailField, BooleanField, FloatField
from wtforms.validators import DataRequired, NumberRange, Length
from .models import Utilisateur

"Formulaires de l'application"

class BilletForm(FlaskForm):
    """Formulaire pour ajouter un billet"""
    typebillet = SelectField('Type Billet', validators=[DataRequired()], choices=[(1, 'Un jour Vendredi'), (2, 'Un jour Samedi'), (3, 'Un jour Dimanche'), (4, 'Totalité'), (5, 'Totalité + VIP')])
    prixbillet = FloatField('Prix Billet', validators=[DataRequired()], render_kw={'readonly': True})
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