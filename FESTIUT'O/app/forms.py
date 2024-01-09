from flask_wtf import FlaskForm
from wtforms import DateField, FileField, StringField, HiddenField, PasswordField, SelectField, RadioField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from .models import Spectateur

"Formulaires de l'application"

class BilletForm(FlaskForm):
    """Formulaire pour ajouter un billet"""
    pass

class SpectateurForm(FlaskForm):
    """Formulaire pour ajouter un spectateur"""
    pass

class LoginForm(FlaskForm):
    email = StringField('Email')
    mdp = PasswordField('Password')
    mdp_incorrect = ""
    next = HiddenField()

    def get_authenticated_user(self):
        user = Spectateur.query.filter_by(email=self.email.data).first()
        if user and user.mdp == self.mdp.data:
            return user
    
    def has_content(self):
        return self.mdp.data != "" or self.email.data != ""
    
    def show_password_incorrect(self):
        self.mdp_incorrect = "Email ou mot de passe incorrect"