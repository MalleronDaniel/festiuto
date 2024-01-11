from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Float, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class GROUPE(Base):
    __tablename__ = 'GROUPE'

    idgroupe = Column(Integer, primary_key=True)
    nomgroupe = Column(String(42))
    description = Column(Text)
    lienvideo = Column(String(42))
    stylemusical = Column(String(42))
    idh = Column(Integer, ForeignKey('HEBERGEMENT.idh'))
    heberger = relationship('HEBERGER', back_populates='groupe')
    artistes = relationship('ARTISTE', back_populates='groupe')
    avoir_styles = relationship('AVOIR', back_populates='groupe')
    contribuer = relationship('CONTRIBUER', back_populates='groupe')
    contenir_photos = relationship('CONTENIR', back_populates='groupe')
    appreciations = relationship('APPRECIER', back_populates='groupe')
    partages = relationship('PARTAGER', back_populates='groupe')
    participations = relationship('PARTICIPER', back_populates='groupe')
    similaire_groupes = relationship('SIMILAIRE', back_populates='groupe')
    similaire_groupes_1 = relationship('SIMILAIRE', back_populates='groupe_1')
    hebergement = relationship('HEBERGEMENT', back_populates='groupes')

class HEBERGER(Base):
    __tablename__ = 'HEBERGER'

    idh = Column(Integer, primary_key=True)
    idgroupe = Column(Integer, ForeignKey('GROUPE.idgroupe'))
    jourDebut = Column(Enum('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'))
    dureeH = Column(Integer)
    groupe = relationship('GROUPE', back_populates='heberger')

class ARTISTE(Base):
    __tablename__ = 'ARTISTE'

    idartiste = Column(Integer, primary_key=True)
    nomartiste = Column(String(42))
    prenomartiste = Column(String(42))
    age = Column(Integer)
    descriptiona = Column(String(42))
    idgroupe = Column(Integer, ForeignKey('GROUPE.idgroupe'))
    groupe = relationship('GROUPE', back_populates='artistes')

class BILLET(Base):
    __tablename__ = 'BILLET'

    idbillet = Column(Integer, primary_key=True)
    typebillet = Column(String(42))
    prixbillet = Column(Float(6))
    nbjoursbillet = Column(Integer)
    spectateurs = relationship('UTILISATEUR', back_populates='billet')
    acceder = relationship('ACCEDER', back_populates='billet')
    regarder = relationship('REGARDER', back_populates='billet')

class CONCERT(Base):
    __tablename__ = 'CONCERT'

    jour = Column(Enum('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'), primary_key=True)
    datedebutc = Column(DateTime, primary_key=True)
    idconcert = Column(Integer, primary_key=True)
    duree = Column(Float)
    noml = Column(String(42), ForeignKey('LIEU.noml'))
    lieu = relationship('LIEU', back_populates='concerts')
    acceder = relationship('ACCEDER', back_populates='concert')
    contribuer = relationship('CONTRIBUER', back_populates='concert')

class PHOTOS(Base):
    __tablename__ = 'PHOTOS'

    idphoto = Column(Integer, primary_key=True)
    nomphoto = Column(String(42))
    photo = Column(String(42))
    contenir = relationship('CONTENIR', back_populates='photo')

class RESEAUX(Base):
    __tablename__ = 'RESEAUX'

    idreseau = Column(Integer, primary_key=True)
    lienreseau = Column(String(42))
    nomreseau = Column(String(42))
    partager = relationship('PARTAGER', back_populates='reseau')

class SOUS_STYLE(Base):
    __tablename__ = 'SOUS_STYLE'

    ids = Column(Integer, primary_key=True)
    nomstyle = Column(String(42))
    avoir = relationship('AVOIR', back_populates='sous_style')

class UTILISATEUR(Base):
    __tablename__ = 'UTILISATEUR'


    iduser = Column(Integer, primary_key=True)
    nomuser = Column(String(42))
    age = Column(Integer)
    email = Column(String(42))
    idbillet = Column(Integer, ForeignKey('BILLET.idbillet'))
    billet = relationship('BILLET', back_populates='spectateurs')
    appreciations = relationship('APPRECIER', back_populates='UTILISATEUR')

class ACTIVITE_ANNEXE(Base):
    __tablename__ = 'ACTIVITE_ANNEXE'

    idact = Column(Integer, primary_key=True)
    dateact = Column(DateTime)
    typeact = Column(String(42))
    dureeact = Column(Float)
    participer = relationship('PARTICIPER', back_populates='activite_annexe')
    regarder = relationship('REGARDER', back_populates='activite_annexe')
    contribuer = relationship('CONTRIBUER', back_populates='activite_annexe')
    geolocaliser = relationship('GEOLOCALISER', back_populates='activite_annexe')

class INSTRUMENTS(Base):
    __tablename__ = 'INSTRUMENTS'

    idinstrument = Column(Integer, primary_key=True)
    nominstrument = Column(String(42))
    jouer = relationship('JOUER', back_populates='instrument')

class LIEU(Base):
    __tablename__ = 'LIEU'

    noml = Column(String(42), primary_key=True)
    capacite = Column(Integer)
    scene = Column(Boolean)
    concerts = relationship('CONCERT', back_populates='lieu')
    geolocaliser = relationship('GEOLOCALISER', back_populates='lieu')

class PARTAGER(Base):
    __tablename__ = 'PARTAGER'

    idreseau = Column(Integer, ForeignKey('RESEAUX.idreseau'), primary_key=True)
    idgroupe = Column(Integer, ForeignKey('GROUPE.idgroupe'), primary_key=True)
    reseau = relationship('RESEAUX', back_populates='partager')
    groupe = relationship('GROUPE', back_populates='partages')

class PARTICIPER(Base):
    __tablename__ = 'PARTICIPER'

    idgroupe = Column(Integer, ForeignKey('GROUPE.idgroupe'), primary_key=True)
    idact = Column(Integer, ForeignKey('ACTIVITE_ANNEXE.idact'), primary_key=True)
    dateact = Column(DateTime, primary_key=True)
    groupe = relationship('GROUPE', back_populates='participations')
    activite_annexe = relationship('ACTIVITE_ANNEXE', back_populates='participer')

class REGARDER(Base):
    __tablename__ = 'REGARDER'

    idact = Column(Integer, ForeignKey('ACTIVITE_ANNEXE.idact'), primary_key=True)
    dateact = Column(DateTime, ForeignKey('ACTIVITE_ANNEXE.dateact'), primary_key=True)
    idbillet = Column(Integer, ForeignKey('BILLET.idbillet'), primary_key=True)
    activite_annexe = relationship('ACTIVITE_ANNEXE', back_populates='regarder')
    billet = relationship('BILLET', back_populates='regarder')

class SIMILAIRE(Base):
    __tablename__ = 'SIMILAIRE'

    idgroupe = Column(Integer, ForeignKey('GROUPE.idgroupe'), primary_key=True)
    idgroupe_1 = Column(Integer, ForeignKey('GROUPE.idgroupe'), primary_key=True)
    groupe = relationship('GROUPE', back_populates='similaire_groupes', foreign_keys=[idgroupe])
    groupe_1 = relationship('GROUPE', back_populates='similaire_groupes_1', foreign_keys=[idgroupe_1])


engine = create_engine('bd.db')
Base.metadata.create_all(engine)
