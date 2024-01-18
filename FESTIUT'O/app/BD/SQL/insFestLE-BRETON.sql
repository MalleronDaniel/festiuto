
-- insertion des activités annexes

insert into ACTIVITE_ANNEXE (idact, dateact, typeact, dureeact)
values
(1, '2023-09-20 15:00:00', 'Séance photo avec les artiste', 2),
(2, '2023-09-21 14:30:00', 'spectateurs qui monte sur scène', 1),
(3, '2023-09-22 16:45:00', 'tir à la corde', 1.5),
(4, '2023-09-21 13:45:00', 'dégustation de fromages', 1),
(5, '2023-09-22 17:00:00', 'dégustation de vins', 1.5);

-------

-- insertion des types de billets

insert into BILLET (typebillet, descbillet, prixbillet)
values
(1, 'Billet Un Jour Vendredi', 50.00),
(2, 'Billet Un Jour Samedi', 50.00),
(3, 'Billet Un Jour Dimanche', 50.00),
(4, 'Billet Totalité', 129.00),
(5, 'Billet Totalité + VIP', 199.00);


-------

-- insertion des lieux

insert into LIEU (noml, capacite, scene)
values
('Main Stage', 5000, true),
('Outdoor Arena', 10000, true),
('Intimate Hall', 100, false),
('Club Venue', 500, false),
('Open Air Park', 8000, true);



-------

-- insertion des concerts

insert into CONCERT (idconcert, jour, datedebutc, duree, noml)
values
(1, 'Vendredi', '2023-09-22 18:00:00', 120, 'Main Stage'),
(2, 'Vendredi', '2023-09-22 19:30:00', 150, 'Outdoor Arena'),
(3, 'Vendredi', '2023-09-22 20:15:00', 105, 'Intimate Hall'),
(4, 'Vendredi', '2023-09-22 21:00:00', 120, 'Club Venue'),
(5, 'Vendredi', '2023-09-22 22:45:00', 135, 'Open Air Park');


------

-- insertion pour la table HEBERGEMENT

insert into HEBERGEMENT (idh, adresse, nbplace)
values
(1, "123 Rue de l'Hôtel", 200),
(2, '456 Avenue des Auberges', 150),
(3, '789 Rue de la Pension', 100),
(4, '1010 Rue des Hôtes', 80),
(5, '1212 Avenue des Voyageurs', 120);


------

-- insertion des groupes de musique

-- groupe de rock
insert into GROUPE (idgroupe, nomgroupe, description, lienvideo, stylemusical)
values
(1, 'The Beathles', 'Un groupe de rock un peu vieux', 'youtube.com/Beathles', 'Rock'),
(2, 'Rolling Stones', 'sympa à écouter', 'youtube.com/RollingStones', 'Rock'),
(3, 'ACDC', 'ca fait un peu mal au oreille', 'youtube.com/ACDC', 'Rock'),
(4, 'Queen', "c'est pas mal", 'youtube.com/Queen', 'Rock'),
(5, 'Nirvana', 'vraiment cool', 'youtube.com/Nirvana', 'Rock');

-- groupe de rap

insert into GROUPE (idgroupe, nomgroupe, description, lienvideo, stylemusical)
values
(6, 'PNL', 'deux frères', 'youtube.com/PNL', 'Rap'),
(7, 'Arsenic', 'Un groupe de rap menbre de collectif Secteur 1', 'youtube.com/Arsenic', 'Rap'),
(8, 'Foncky Family', 'groupe de rap originaire de marseille', 'youtube.com/FonckyFamily', 'Rap'),
(9, 'Casseurs Flwoters', 'Orelsan et des gens', 'youtube.com/CasseursFlwoters', 'Rap'),
(10, 'S-Crew', 'groupe de pote qui rap', 'youtube.com/S-Crew', 'Rap');


-------

-- insertion des artistes

insert into ARTISTE (idartiste, nomartiste, prenomartiste, ddn, descriptiona, idgroupe)
values
(1, 'Smith', 'John', '1999-12-22', 'Guitare', 1),
(2, 'Doe', 'Jane', '1969-01-02', 'Batterie', 2),
(3, 'Johnson', 'Mike', '1988-11-24', 'Basse', 3),
(4, 'Brown', 'Lisa', '1975-09-13', 'Chanteur', 4),
(5, 'Wilson', 'David', '1977-09-26', 'Piano', 5),
(6, 'Jackson', 'Chris', '1998-09-13' ,'Chanteur', 6),
(7, 'White', 'Emily', '1976-09-12', 'Chanteur', 7),
(8, 'Davis', 'Alex', '1976-09-04', 'Guitare', 8),
(9, 'Green', 'Sophia', '1989-09-06', 'Piano', 9),
(10, 'Lee', 'Daniel', '1950-09-19', 'Chanteur', 10);


------

-- insertion des INSTRUMENTS

insert into INSTRUMENTS (idinstrument, nominstrument)
values
(1, 'Guitare'),
(2, 'Basse'),
(3, 'Baterie'),
(4, 'Piano'),
(5, 'Micro');




-------

-- insertion des photos

insert into PHOTOS (idphoto, nomphoto, photo)
values
(1, 'photo du groupe Beathles', 'Beathles.jpg'),
(2, 'photo du groupe Rolling Stones', 'RollingStones.jpg'),
(3, 'photo du groupe ACDC', 'ACDC.jpg'),
(4, 'photo du groupe Queen', 'Queen.jpg'),
(5, 'photo du groupe Nirvana', 'Nirvana.jpg'),
(6, 'photo du groupe PNL', 'PNL.jpg'),
(7, 'photo du groupe Arsenic', 'Arsenic.jpg'),
(8, 'photo du groupe Foncky Family', 'FonckyFamily.jpg'),
(9, 'photo du groupe Casseurs', 'Casseurs.jpg'),
(10, 'photo du groupe S-Crew', 'SCrew.jpg');


-------

-- insertion des réseaux

insert into RESEAUX (idreseau, lienreseau, nomreseau, idgroupe)
values
(1, 'instagram/Beathles.com', 'Instagram', 1),
(2, 'instagram/RollingStones.com', 'Instagram', 2),
(3, 'instagram/ACDC.com', 'Instagram', 3),
(4, 'facebook/Queen.com', 'Facebook', 4),
(5, 'facebook/Nirvana.com', 'Facebook', 5),
(6, 'facebook/PNL.com', 'Facebook', 6),
(7, 'facebook/Arsenic.com', 'Facebook', 7),
(8, 'facebook/FonckyFamily.com', 'Facebook', 8),
(9, 'instagram/Casseurs.com', 'Instagram', 9),
(10, 'instagram/SCrew.com', 'Instagram', 10);


-------

-- insertion des sous-styles

insert into SOUS_STYLE (ids, nomstyle)
values
(1, 'Rap'),
(2, 'Rock');


-------

-- insertion des utilisateurs

insert into UTILISATEUR (iduser, nomuser, ddn, email, mdp, admin)
values
(1, 'Daniel Malleron', '2004-09-13', 'danyyyy@gmail.com', 'mdp', true),
(2, 'Kevin Le Breton', '2004-09-13', 'kevin.le.breton@gmail.com', 'mdp', false),
(3, 'Adam Daniel', '2004-09-13', 'dadam@gmail.com', 'mdp', false),
(4, 'Alicia Romero', '2004-09-13', 'alicia.romero@gmail.com', 'mdp', false),
(5, 'Jordan Zebo', '2004-09-13', 'jojo5sec@gmail.com', 'mdp', false),
(6, 'Cyril Doumbe', '2004-09-13', 'jordanTmort@gmail.com', 'mdp', false);


-------

-- insertion des instance POSSEDER (UTILISATEUR-BILLET)

insert into POSSEDER(iduser, typebillet)
values
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,2);


-------

-- insertion dans la table apprecier

insert into APPRECIER (idgroupe, iduser)
values
(1, 1),
(7, 1),
(2, 2),
(3, 2),
(6, 3),
(5, 4),
(4, 6);


-------

-- insertion dans la table avoir

insert into AVOIR (ids, idgroupe)
values
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(2, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10);


-------

-- insertion dans la table contenir

insert into CONTENIR (idphoto, idgroupe)
values
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

-------

-- insertion dans la table geolocaliser

insert into GEOLOCALISER (idact, dateact, noml)
values
(1, '2023-09-20 15:00:00', 'Main Stage'),
(2, '2023-09-21 14:30:00', 'Outdoor Arena'),
(3, '2023-09-22 16:45:00', 'Intimate Hall'),
(4, '2023-09-21 13:45:00', 'Club Venue'),
(5, '2023-09-22 17:00:00', 'Club Venue');


-------

-- insertion dans la table participer

insert into PARTICIPER (idgroupe, idact, dateact)
values
(1, 1, '2023-09-20 15:00:00'),
(2, 1, '2023-09-20 15:00:00'),
(3, 1, '2023-09-20 15:00:00'),
(4, 1, '2023-09-20 15:00:00'),
(5, 1, '2023-09-20 15:00:00'),
(6, 1, '2023-09-20 15:00:00'),
(7, 1, '2023-09-20 15:00:00'),
(8, 1, '2023-09-20 15:00:00'),
(1, 2, '2023-09-21 14:30:00'),
(2, 3, '2023-09-22 16:45:00');


-------

-- insertion dans la table participer

insert into SIMILAIRE (idgroupe, idgroupe_1)
values
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(2, 3),
(2, 4),
(2, 5),
(3, 4),
(3, 5),
(4, 5),
(6, 7),
(6, 8),
(6, 9),
(6, 10),
(7, 8),
(7, 9),
(7, 10),
(8, 9),
(8, 10),
(9, 10);


-------

-- insertion dans la table jouer

insert into JOUER (idinstrument, idartiste)
values
(1, 1),
(3, 2),
(2, 3),
(5, 4),
(4, 5),
(5, 6),
(5, 7),
(1, 8),
(4, 9),
(5, 10);


-------

-- insertion dans la table participer

insert into REGARDER (idact, dateact, typebillet)
values
(1, '2023-09-20 15:00:00', 1),
(1, '2023-09-20 15:00:00', 2),
(1, '2023-09-20 15:00:00', 3),
(2, '2023-09-21 14:30:00', 4),
(2, '2023-09-21 14:30:00', 5),
(3, '2023-09-22 16:45:00', 1);


-------

-- insertion dans la table contenir

insert into CONTRIBUER (idgroupe, idconcert, tempsdemontage, tempsmontage)
values
(1, 1, 0.75, 0.5),
(2, 2, 1, 0.5),
(3, 3, 1.25, 0.75),
(4, 4, 1, 0.5),
(7, 5, 1, 0.5);


-------

-- insertion des acceder

insert into ACCEDER (idconcert, typebillet, preinscription)
values
(1, 1, false),
(2, 2, false),
(3, 3, false);



-- Test trigger groupeDisponibleConcert

-- Test 1: Insertion d'un concert avec un événement précédent trop proche en temps
INSERT INTO CONTRIBUER (idgroupe, idconcert, tempsdemontage, tempsmontage)
VALUES (1, 2, 0.75, 0.5);

-- Test 2: Insertion d'un concert avec un événement suivant trop proche en temps
INSERT INTO CONTRIBUER (idgroupe, idconcert, tempsdemontage, tempsmontage)
VALUES (2, 1, 0.75, 0.5);

--Test trigger groupeDisponibleActiviteAnnexe

-- Test 1: Insertion d'un concert avec un événement suivant trop proche en temps
INSERT INTO PARTICIPER (idgroupe, idact, dateact)
VALUES (1, 4, '2023-09-21 13:45:00');

-- Test 2: Insertion d'une activité annexe avec un événement précédent trop proche en temps
INSERT INTO PARTICIPER (idgroupe, idact, dateact)
VALUES (2, 5, '2023-09-22 17:00:00');

-- test trigger lieuUtiliseConcert

INSERT INTO CONCERT values('6','Vendredi','2023-09-22 18:00:00', 100, 'Main Stage');


--  test trigger lieuUtiliseAnnexe

INSERT INTO ACTIVITE_ANNEXE values(2, '2023-09-20 14:30:00', 'Entretien avec les artistes', 2);
INSERT INTO GEOLOCALISER values(2, '2023-09-20 14:30:00', 'Main Stage');

-- test trigger nbPreinscrip

insert into LIEU values('test', 5, 0);
insert into CONCERT values(600, 'Lundi', '2023-08-16 10:15:00', 100, 'test');
insert into ACCEDER values(600, 1, 0);
insert into ACCEDER values(600, 2, 0);
insert into ACCEDER values(600, 3, 0);
insert into ACCEDER values(600, 4, 0);
insert into ACCEDER values(600, 5, 0);
insert into ACCEDER values(600, 6, 0);
