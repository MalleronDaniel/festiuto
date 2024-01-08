from .app import app, db
from flask import render_template, url_for, redirect
from .models import Favoris, get_books_by_user_id, get_favoris, get_moy_livre, get_sample, get_author, Author, get_book, insert_or_update_note

from flask_wtf import FlaskForm
from wtforms import RadioField, StringField , HiddenField
from wtforms.validators import DataRequired

from .models import Book
    
from flask_login import login_user, current_user
from flask import request

@app.route("/")
def home():
    return render_template (
        "home.html",
        books = get_sample())

@app.route("/homev2")
def homev2():
    return render_template (
        "homev2.html",
        titre_home_v2 = "On change de page",
        groupe = ["Daniel, Kevin, Adam, Yohan"])


@app.route("/livre")
def livre():
    return render_template(
        "livre.html",
        title = "Mes livres",
        books = get_sample())

@app.route("/detail/<id>")
def detail(id):
    if int(id) > 99:
        id = 0
    books = get_sample()
    book = books[int(id)]
    moyenne = get_moy_livre(book.id)
    est_favori = None
    if current_user.is_authenticated:
        est_favori = get_favoris(current_user.username, book.id)is not None
    return render_template(
        "detail.html",
        book=book, moyenne=moyenne, est_favori= est_favori)

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom', validators=[DataRequired()]) # Doit obligatoirement remplir le champs 

from flask_login import login_required
@app.route("/edit/author/<int:id>")
@login_required
def edit_author(id):
    a = get_author(id)
    f = AuthorForm(id = a.id, name = a.name)
    return render_template(
        "edit-author.html",
        author = a,
        form = f)

@app.route("/save/author/", methods=["POST",]) # Uniquement accessible par cette méthode POST
def save_author():
    a = None
    f = AuthorForm() # Formulaire
    if f.validate_on_submit(): # Vérifie si formulaire valide -> champs bien remplit, trouver token, etc ...
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(        # Rediriger l'utilisateur vers une page
            url_for("home"))
    a = get_author(int(f.id.data))
    return render_template(
        "edit-author.html",
        author=a,
        form=f)

from wtforms import PasswordField
from.models import User
from hashlib import sha256

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    next = HiddenField()

    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

    
@app.route("/login/", methods = ("GET","POST",))
def login():
    f = LoginForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f. validate_on_submit():
        user = f. get_authenticated_user()
        if user:
            login_user (user)
            next = f.next.data or url_for("livre")
            return redirect (next)
    return render_template (
        "login.html",
        form=f)


class AjouteNote(FlaskForm):
    notes = RadioField('Sélectionnez une note', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])

@app.route('/ajouteNoteLivre/<int:id>')
@login_required
def ajouteNoteLivre(id):
    f = AjouteNote()
    b = get_book(id)
    return render_template('ajouteNote.html', form=f, book=b)


@app.route("/SaveNoteLivre/<int:id>", methods=["POST",]) # Uniquement accessible par cette méthode POST
def save_note(id):
    f = AjouteNote() # Formulaire
    b= get_book(id)
    if f.validate_on_submit(): # Vérifie si formulaire valide -> champs bien remplit, trouver token, etc ...
        note = f.notes.data
        username = current_user.username
        insert_or_update_note(username,b,note)
        return redirect(url_for("detail", id=id-1))
    return render_template("ajouteNote.html", form=f, book=b)

@app.route('/ajouter_ou_supprimer_favoris/<int:book_id>', methods=['POST'])
def ajouter_ou_supprimer_favoris(book_id):
    # Vérifier si le livre est déjà en favori pour l'utilisateur
    est_favori = Favoris.query.filter_by(username=current_user.username, book_id=book_id).first()

    if est_favori:
        # Si le livre est déjà en favori, le supprimer
        db.session.delete(est_favori)
        db.session.commit()
    else:
        # Sinon, l'ajouter en favori
        favori = Favoris(username=current_user.username, book_id=book_id)
        db.session.add(favori)
        db.session.commit()

    return redirect(url_for('detail', id=book_id-1)) # Rediriger vers la page du livre


@app.route("/favoris/")
@login_required
def favoris():
    username = current_user.username
    liste_fav = get_books_by_user_id(username)
    return render_template("favoris.html", liste_fav = liste_fav)

from flask_login import logout_user

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('livre'))


@app.route("/categorie/")
def categorie():
    f = CategoryForm()
    return render_template("categorie.html", form=f, cat=None)

class CategoryForm(FlaskForm):
    category = RadioField('Sélectionnez une catégorie', choices=[('Fiction', 'Fiction'), ('Fantasy', 'Fantasy'), ('Action', 'Action'), ('Adventure', 'Adventure'), ('Detective Story', 'Detective Story')], validators=[DataRequired()])

@app.route("/maj_categorie/", methods=["POST"])
def maj_categorie():
    f = CategoryForm()
    books = []
    categorie = None

    if f.validate_on_submit():
        categorie = f.category.data
        books = Book.query.filter_by(category=categorie).all()

    return render_template("categorie.html", form = f, books=books, cat=categorie)
