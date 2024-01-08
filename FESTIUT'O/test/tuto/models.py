from sqlalchemy import func
from .app import db
from flask_login import UserMixin

class Author(db.Model):
    """Représentation de la table Author dans la base de données

    Args:
        db : la base de données associée
    """
    id = db.Column(db.Integer, primary_key=True) # Indique la clé primaire de la table
    name = db.Column(db.String(100))

    def __repr__(self):
        """  Redéfinit l'équivalent du toString en java  """
        return "%s" % self.name

class Book(db.Model):
    """Représentation de la table Book dans la base de données

    Args:
        db : la base de données associée
    """
    id = db.Column(db.Integer, primary_key =True) # Indique la clé primaire de la table
    price = db.Column(db.Float)
    category = db.Column(db.String(100))
    title = db.Column(db.String(100))
    url = db.Column(db.String(250))
    img = db.Column(db.String(200))

    # Partie foreign key 
    author_id = db.Column(db.Integer, db.ForeignKey("author.id")) # Indique la foreign key dans la table associée
    author = db.relationship("Author", backref=db.backref("books", lazy="dynamic"))
    


    def __repr__(self):
        """  Redéfinit l'équivalent du toString en java  """
        return "%s" % self.title
    
def get_book(id: int): 
    """Retourne le livre avec l'id associé

    Args:
        id : l'id associé
    """
    return Book.query.get(id)

def get_sample():
    """  Retourne les livres  """
    return Book.query.all() # S'apparente au "select * from Book"


def get_author(id: int): 
    """Retourne l'auteur avec l'id associé

    Args:
        id : l'id associé
    """
    return Author.query.get(id)


class User(db.Model,UserMixin):
    username = db.Column(db.String(50), primary_key =True)
    password = db.Column(db.String(64))

    def get_id(self):
        return self.username
    
from .app import login_manager
@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

class Note(db.Model):
    """Représente une note donné par un utilisateur sur un livre

    Args:
        db : la base de données
    """
    username = db.Column(db.String(50), db.ForeignKey('user.username'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    noteLivre = db.Column(db.Integer)

    def get_noteLivre(self):
        return self.noteLivre
    
    def get_idBook(self):
        return self.idBook
    
    def get_username(self):
        return self.username
    
def get_moy_livre(idBook):
    """Retourne la moyenne des notes a partir d'un id d'un livre

    Args:
        idBook (int): id du livre
    """
    notes = Note.query.filter_by(book_id=idBook).all()
    if not notes:
        return "Il n'y a pas de note"
    else:
        moyenne = sum(note.noteLivre for note in notes) / len(notes)
        return moyenne
    
def insert_or_update_note(username, book, note_livre):
    """Insère une nouvelle note dans la base de données.

    Args:
        username : le nom d'utilisateur de l'auteur de la note
        id_book : l'identifiant du livre
        note_livre : la note du livre

    Returns:
        La note nouvellement insérée.
    """
    print(username,book,note_livre)
    id = book.id
    note = Note(username=username, book_id=id, noteLivre=note_livre)
    db.session.merge(note)
    db.session.commit()
    return note


class Favoris(db.Model):
    username = db.Column(db.String(50), db.ForeignKey('user.username'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)

    def get_username(self):
        return self.username
    
    def get_book(self):
        return Book.query.get(self.book_id)

def get_books_by_user_id(user_id):
    favoris = Favoris.query.filter_by(username=user_id).all()
    return favoris

def get_favoris(username,id):
    return Favoris.query.filter_by(username=username, book_id = id).first()


from .app import login_manager
@login_manager.user_loader
def load_user(username):
    return User.query.get(username)
