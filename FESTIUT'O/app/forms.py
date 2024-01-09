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

