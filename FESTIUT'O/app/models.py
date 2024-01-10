"""Lien avec la bd"""

import datetime   
from sqlalchemy import func
from .app import db, login_manager #, login_manager
from flask_login import UserMixin

# pour login
@login_manager.user_loader
def load_user(user_id):
    return Utilisateur.query.get(int(user_id))

# TABLES
class ActiviteAnnexe(db.Model):
    __tablename__ = "ACTIVITE_ANNEXE"
    idact = db.Column(db.Integer)
    dateact = db.Column(db.DateTime, nullable=False)
    typeact = db.Column(db.String(42))
    dureeact = db.Column(db.Float)
    __table_args__ = (db.PrimaryKeyConstraint('idact', 'dateact'),)
    
    def __repr__(self):
        return f"<ActiviteAnnexe ({self.idact}) | {self.dateact} | {self.typeact}>"

    #GETTERS
    def get_activites():
        """  Retourne les activités  """
        return ActiviteAnnexe.query.all()    

    def get_activite(idact: int, dateact: datetime): 
        """Retourne l'activité avec l'id associé

        Args:
            idact : l'id associé
            dateact : la date associée
        """
        return ActiviteAnnexe.query.get((idact, dateact))


class Artiste(db.Model):
    __tablename__ = "ARTISTE"
    idartiste = db.Column(db.Integer, primary_key=True)
    nomartiste = db.Column(db.String(42))
    prenomartiste = db.Column(db.String(42))
    age = db.Column(db.Integer)
    descriptiona = db.Column(db.String(42))
    idgroupe = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'))
    groupe = db.relationship('Groupe', backref=db.backref("artistes", lazy="dynamic"))
    
    def __repr__(self):
        return f"<Artiste ({self.idartiste}) | {self.prenomartiste} {self.nomartiste}>"

    #GETTERS
    def get_artiste(idartiste: int): 
        """Retourne l'artiste avec l'id associé

        Args:
            idartiste : l'id associé
        """
        return Artiste.query.get(idartiste)

    def get_artistes():
        """  Retourne les artistes  """
        return Artiste.query.all()


class Billet(db.Model):
    __tablename__ = "BILLET"
    idbillet = db.Column(db.Integer, primary_key=True)
    typebillet = db.Column(db.String(42))
    prixbillet = db.Column(db.Float(6))
    nbjoursbillet = db.Column(db.Integer)
    
    def __repr__(self):
        return f"({self.idbillet}) {self.typebillet} - €{self.prixbillet}"
    
    def __repr__(self):
        return f"<Billet ({self.idbillet}) | {self.typebillet}>"


class Concert(db.Model):
    __tablename__ = "CONCERT"
    jour = db.Column(db.Enum('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'))
    datedebutc = db.Column(db.DateTime, nullable=False)
    idconcert = db.Column(db.Integer)
    duree = db.Column(db.Float)
    noml = db.Column(db.String(42), db.ForeignKey('LIEU.noml'))
    lieu = db.relationship('Lieu', backref=db.backref("concerts", lazy="dynamic"))
    __table_args__ = (db.PrimaryKeyConstraint('jour', 'datedebutc', 'idconcert'),)
    
    def __repr__(self):
        return f"<Concert ({self.idconcert}) | {self.datedebutc} | {self.jour}>"

    #GETTERS
    def get_groupe_concert(self):
        """Retourne l'id des groupe d'un concert"""
        groupes = (db.session.query(Contribuer.idgroupe)
            .join(Concert, Contribuer.idconcert == self.idconcert)
            .all())
        return groupes
    
class Groupe(db.Model):
    __tablename__ = 'GROUPE'
    idgroupe = db.Column(db.Integer, primary_key=True)
    nomgroupe = db.Column(db.String(42))
    description = db.Column(db.Text)
    lienvideo = db.Column(db.String(42))
    stylemusical = db.Column(db.String(42))

    
    def __repr__(self):
        return f"<Groupe ({self.idgroupe}) | {self.nomgroupe}>"


class Hebergement(db.Model):
    __tablename__ = "HEBERGEMENT"
    idh = db.Column(db.Integer, primary_key=True)
    adresse = db.Column(db.String(42))
    nbplace = db.Column(db.Integer)
    
    def __repr__(self):
        return f"<Hebergement ({self.idh}) | {self.adresse}>"
    
class Heberger(db.Model):
    __tablename__ = "HEBERGER"
    idh = db.Column(db.Integer, db.ForeignKey('HEBERGEMENT.idh'), primary_key=True)
    idgroupe = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'), primary_key=True)
    jourDebut = db.Column(db.Enum('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'))
    dureeH = db.Column(db.Integer)

    def __repr__(self) :
        return f"<Heberger ({self.idh}) | ({self.idgroupe}) | ({self.jourDebut}) | ({self.dureeH})>"



class Instruments(db.Model):
    __tablename__ = "INSTRUMENTS"
    idinstrument = db.Column(db.Integer, primary_key=True)
    nominstrument = db.Column(db.String(42))
    
    def __repr__(self):
        return f"<Instruments ({self.idinstrument}) | {self.nominstrument}>"


class Lieu(db.Model):
    __tablename__ = "LIEU"
    noml = db.Column(db.String(42), primary_key=True)
    capacite = db.Column(db.Integer)
    scene = db.Column(db.Boolean)
    
    def __repr__(self):
        return f"<Lieu ({self.noml}) | {self.capacite}>"


class Photos(db.Model):
    __tablename__ = "PHOTOS"
    idphoto = db.Column(db.Integer, primary_key=True)
    nomphoto = db.Column(db.String(42))
    photo = db.Column(db.String(42))
    
    def __repr__(self):
        return f"<Photos ({self.idphoto}) | {self.nomphoto}>"


class Reseaux(db.Model):
    __tablename__ = "RESEAUX"
    idreseau = db.Column(db.Integer, primary_key=True)
    lienreseau = db.Column(db.String(42))
    nomreseau = db.Column(db.String(42))
    
    def __repr__(self):
        return f"<Reseaux ({self.idreseau}) | {self.nomreseau}>"


class SousStyle(db.Model):
    __tablename__ = 'SOUS_STYLE'
    ids = db.Column(db.Integer, primary_key=True)
    nomstyle = db.Column(db.String(42))
    
    def __repr__(self):
        return f"<SousStyle ({self.ids}) | {self.nomstyle}>"


class Utilisateur(db.Model, UserMixin):
    __tablename__ = "UTILISATEUR"
    iduser = db.Column(db.Integer, primary_key=True)
    nomuser = db.Column(db.String(42))

    age = db.Column(db.Integer)
    email = db.Column(db.String(42), unique=True)
    idbillet = db.Column(db.Integer, db.ForeignKey('BILLET.idbillet'))
    billet = db.relationship('Billet', backref=db.backref("utilisateur", lazy="dynamic"))
    mdp = db.Column(db.String(42))
    admin = db.Column(db.Boolean)
    
    def __repr__(self):
        return f"<Utilisateur ({self.iduser}) | {self.nomuser}>"
    
    def get_id(self):
        return self.iduser


class Acceder(db.Model):
    __tablename__ = "ACCEDER"
    jour = db.Column(db.Enum('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'))
    datedebutc = db.Column(db.DateTime, nullable=False)
    idconcert = db.Column(db.Integer, db.ForeignKey('CONCERT.idconcert'))
    concert = db.relationship('Concert', backref=db.backref("acces", lazy="dynamic"))
    idbillet = db.Column(db.Integer, db.ForeignKey('BILLET.idbillet'))
    preinscription = db.Column(db.Boolean)
    billet = db.relationship('Billet', backref=db.backref("acces", lazy="dynamic"))
    __table_args__ = (db.PrimaryKeyConstraint('jour', 'datedebutc', 'idconcert','idbillet'),)


class Apprecier(db.Model):
    __tablename__ = "APPRECIER"
    idgroupe = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'))
    iduser = db.Column(db.Integer, db.ForeignKey('UTILISATEUR.iduser'))
    utilisateur = db.relationship('Utilisateur', backref=db.backref("appreciations", lazy="dynamic"))
    groupe = db.relationship('Groupe', backref=db.backref("appreciations", lazy="dynamic"))
    __table_args__ = (db.PrimaryKeyConstraint('idgroupe', 'iduser'),)



class Avoir(db.Model):
    __tablename__ = 'AVOIR'
    ids = db.Column(db.Integer, db.ForeignKey('SOUS_STYLE.ids'), primary_key=True)
    idgroupe = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'), primary_key=True)
    sous_style = db.relationship('SousStyle', backref=db.backref("avoir", lazy="dynamic"))
    groupe = db.relationship('Groupe', backref=db.backref("avoir", lazy="dynamic"))
    __table_args__ = (db.PrimaryKeyConstraint('ids', 'idgroupe'),)


class Contenir(db.Model):
    __tablename__ = "CONTENIR"
    idphoto = db.Column(db.Integer, db.ForeignKey('PHOTOS.idphoto'), primary_key=True)
    photo = db.relationship('Photos', backref=db.backref("contenu", lazy="dynamic"))
    idgroupe = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'), primary_key=True)
    groupe = db.relationship('Groupe', backref=db.backref("contenu", lazy="dynamic"))
    __table_args__ = (db.PrimaryKeyConstraint('idphoto', 'idgroupe'),)


class Contribuer(db.Model):
    __tablename__ = "CONTRIBUER"
    idgroupe = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'), primary_key=True)
    groupe = db.relationship('Groupe', backref=db.backref("contribution", lazy="dynamic"))
    jour = db.Column(db.Enum('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'), primary_key=True)
    datedebutc = db.Column(db.DateTime, nullable=False, primary_key=True)
    idconcert = db.Column(db.Integer, db.ForeignKey('CONCERT.idconcert'), primary_key=True)
    concert = db.relationship('Concert', backref=db.backref("contribution", lazy="dynamic"))
    tempsdemontage = db.Column(db.Float)
    tempsmontage = db.Column(db.Float)
    __table_args__ = (db.PrimaryKeyConstraint('idgroupe', 'jour', 'datedebutc', 'idconcert'),)


class Geolocaliser(db.Model):
    __tablename__ = "GEOLOCALISER"
    idact = db.Column(db.Integer, db.ForeignKey('ACTIVITE_ANNEXE.idact'), primary_key=True)
    act = db.relationship('ActiviteAnnexe', foreign_keys=[idact], backref=db.backref("geolocalisation", lazy="dynamic"))
    dateact = db.Column(db.DateTime, db.ForeignKey('ACTIVITE_ANNEXE.dateact'), primary_key=True)
    dact = db.relationship('ActiviteAnnexe', foreign_keys=[dateact], back_populates='geolocalisation')
    noml = db.Column(db.String(42), db.ForeignKey('LIEU.noml'), primary_key=True)
    l = db.relationship('Lieu', backref=db.backref("geolocalisation", lazy="dynamic"))
    __table_args__ = (db.PrimaryKeyConstraint('idact', 'dateact', 'noml'),)


class Jouer(db.Model):
    __tablename__ = "JOUER"
    idinstrument = db.Column(db.Integer, db.ForeignKey('INSTRUMENTS.idinstrument'), primary_key=True)
    instrument = db.relationship('Instruments', backref=db.backref("joue", lazy="dynamic"))
    idartiste = db.Column(db.Integer, db.ForeignKey('ARTISTE.idartiste'), primary_key=True)
    artiste = db.relationship('Artiste', backref=db.backref("joue", lazy="dynamic"))
    __table_args__ = (db.PrimaryKeyConstraint('idinstrument', 'idartiste'),)


class Partager(db.Model):
    __tablename__ = "PARTAGER"
    idreseau = db.Column(db.Integer, db.ForeignKey('RESEAUX.idreseau'), primary_key=True)
    reseau = db.relationship('Reseaux', backref=db.backref("partage", lazy="dynamic"))
    idgroupe = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'), primary_key=True)
    groupe = db.relationship('Groupe', backref=db.backref("partage", lazy="dynamic"))
    __table_args__ = (db.PrimaryKeyConstraint('idreseau', 'idgroupe'),)


class Participer(db.Model):
    __tablename__ = "PARTICIPER"
    idgroupe = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'), primary_key=True)
    groupe = db.relationship('Groupe', backref=db.backref("participation", lazy="dynamic"))
    idact = db.Column(db.Integer, db.ForeignKey('ACTIVITE_ANNEXE.idact'), primary_key=True)
    act = db.relationship('ActiviteAnnexe', foreign_keys=[idact], backref=db.backref("participation", lazy="dynamic"))
    dateact = db.Column(db.DateTime, db.ForeignKey('ACTIVITE_ANNEXE.dateact'), primary_key=True)
    dact = db.relationship('ActiviteAnnexe', foreign_keys=[dateact], back_populates='participation')
    __table_args__ = (db.PrimaryKeyConstraint('idgroupe', 'idact', 'dateact'),)

class Regarder(db.Model):
    __tablename__ = "REGARDER"
    idact = db.Column(db.Integer, db.ForeignKey('ACTIVITE_ANNEXE.idact'), primary_key=True)
    act = db.relationship('ActiviteAnnexe', foreign_keys=[idact], backref=db.backref("regard", lazy="dynamic"))
    dateact = db.Column(db.DateTime, db.ForeignKey('ACTIVITE_ANNEXE.dateact'), primary_key=True)
    dact = db.relationship('ActiviteAnnexe', foreign_keys=[dateact], back_populates='regard')
    idbillet = db.Column(db.Integer, db.ForeignKey('BILLET.idbillet'), primary_key=True)
    billet = db.relationship('Billet', backref=db.backref("regard", lazy="dynamic"))
    __table_args__ = (db.PrimaryKeyConstraint('idact', 'dateact', 'idbillet'),)


class Similaire(db.Model):
    __tablename__ = "SIMILAIRE"
    idgroupe = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'), primary_key=True)
    idgroupe_1 = db.Column(db.Integer, db.ForeignKey('GROUPE.idgroupe'), primary_key=True)
    __table_args__ = (db.PrimaryKeyConstraint('idgroupe', 'idgroupe_1'),)

class Posseder(db.Model):
    __tablename__ = "POSSEDER"
    idbillet = db.Column(db.Integer, db.ForeignKey('BILLET.idbillet'), primary_key=True)
    iduser = db.Column(db.Integer, db.ForeignKey('UTILISATEUR.iduser'), primary_key=True)

# Define foreign key relationships
db.ForeignKeyConstraint(['idgroupe', 'jour', 'datedebutc', 'idconcert'], ['CONTRIBUER.idgroupe', 'CONTRIBUER.jour', 'CONTRIBUER.datedebutc', 'CONTRIBUER.idconcert'])
db.ForeignKeyConstraint(['idact', 'dateact'], ['ACTIVITE_ANNEXE.idact', 'ACTIVITE_ANNEXE.dateact'])
db.ForeignKeyConstraint(['idbillet'], ['BILLET.idbillet'])
db.ForeignKeyConstraint(['idphoto'], ['PHOTOS.idphoto'])
db.ForeignKeyConstraint(['idreseau'], ['RESEAUX.idreseau'])
db.ForeignKeyConstraint(['iduser'], ['UTILISATEUR.iduser'])
db.ForeignKeyConstraint(['idgroupe'], ['GROUPE.idgroupe'])
db.ForeignKeyConstraint(['idinstrument'], ['INSTRUMENTS.idinstrument'])
db.ForeignKeyConstraint(['idartiste'], ['ARTISTE.idartiste'])
db.ForeignKeyConstraint(['idh'], ['HEBERGEMENT.idh'])
db.ForeignKeyConstraint(['noml'], ['LIEU.noml'])
db.ForeignKeyConstraint(['idbillet', 'idact', 'dateact'], ['ACTIVITE_ANNEXE.idact', 'ACTIVITE_ANNEXE.dateact', 'ACTIVITE_ANNEXE.idbillet'])
db.ForeignKeyConstraint(['idreseau', 'idgroupe'], ['GROUPE.idgroupe', 'PARTAGER.idreseau'])
db.ForeignKeyConstraint(['idact', 'dateact'], ['ACTIVITE_ANNEXE.idact', 'ACTIVITE_ANNEXE.dateact'])
db.ForeignKeyConstraint(['idgroupe', 'idact', 'dateact'], ['GROUPE.idgroupe', 'ACTIVITE_ANNEXE.idact', 'ACTIVITE_ANNEXE.dateact'])
db.ForeignKeyConstraint(['idbillet', 'idact', 'dateact'], ['REGARDER.idbillet', 'ACTIVITE_ANNEXE.idact', 'ACTIVITE_ANNEXE.dateact'])
db.ForeignKeyConstraint(['idgroupe_1'], ['GROUPE.idgroupe'])


if __name__ == '__main__':
    db.create_all()







