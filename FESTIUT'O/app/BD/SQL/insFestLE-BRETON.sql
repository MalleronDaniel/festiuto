
-- insertion des lieux

insert into LIEU (noml, capacite, scene)
values
('Main Stage', 5000, true),
('Outdoor Arena', 10000, true),
('Intimate Hall', 100, false),
('Club Venue', 500, false),
('Open Air Park', 8000, true);


-- insertion des activités annexes

insert into ACTIVITE_ANNEXE (idact, dateact, typeact, dureeact, noml)
values

(1, '2023-09-20 15:00:00', 'Séance photo avec les artiste', 2, 'Main Stage'),
(2, '2023-09-21 14:30:00', 'spectateurs qui monte sur scène', 1, 'Outdoor Arena'),
(3, '2023-09-22 16:45:00', 'tir à la corde', 1.5, 'Intimate Hall'),
(4, '2023-09-21 13:45:00', 'dégustation de fromages', 1, 'Club Venue'),
(5, '2023-09-22 17:00:00', 'dégustation de vins', 1.5, 'Open Air Park');

-------

-- insertion des types de billets

insert into BILLET (idbillet, typebillet, descbillet, prixbillet)
values
(1, 1, 'Billet Un Jour Vendredi', 50.00),
(2, 2, 'Billet Un Jour Samedi', 50.00),
(3, 3, 'Billet Un Jour Dimanche', 50.00),
(4, 4, 'Billet Totalité', 129.00),
(5, 5, 'Billet Totalité + VIP', 199.00);


-------

-- insertion des concerts

insert into CONCERT (idconcert, jour, datedebutc, duree, noml)
values
(1, 'Vendredi', '2024-02-21 18:00:00', 120, 'Main Stage'),
(2, 'Vendredi', '2024-02-21 19:30:00', 150, 'Outdoor Arena'),
(3, 'Vendredi', '2024-02-21 20:15:00', 105, 'Intimate Hall'),
(4, 'Vendredi', '2024-02-21 21:00:00', 120, 'Club Venue'),
(5, 'Vendredi', '2024-02-21 22:45:00', 135, 'Open Air Park'),

(6, 'Samedi', '2024-02-22 18:00:00', 120, 'Main Stage'),
(7, 'Samedi', '2024-02-22 19:30:00', 150, 'Outdoor Arena'),
(8, 'Samedi', '2024-02-22 20:15:00', 105, 'Intimate Hall'),
(9, 'Samedi', '2024-02-22 21:00:00', 120, 'Club Venue'),
(10, 'Samedi', '2024-02-22 22:45:00', 135, 'Open Air Park'),

(11, 'Dimanche', '2024-02-23 18:00:00', 120, 'Main Stage'),
(12, 'Dimanche', '2024-02-23 19:30:00', 150, 'Outdoor Arena'),
(13, 'Dimanche', '2024-02-23 20:15:00', 105, 'Intimate Hall'),
(14, 'Dimanche', '2024-02-23 21:00:00', 120, 'Club Venue'),
(15, 'Dimanche', '2024-02-23 22:45:00', 135, 'Open Air Park');



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


INSERT INTO GROUPE (idgroupe, nomgroupe, description, stylemusical)
VALUES
    (11,'Les Enfoirés', "Collectif d'artistes pour les Restos du Cœur", 'Variété française'),
    (12,'Indochine', 'Groupe de rock français', 'Variété française'),
    (13,'Zaz', 'Chanteuse mêlant jazz, variété et musique du monde', 'Variété française'),
    (14,'Stromae', 'Auteur-compositeur-interprète belge', 'Variété française'),
    (15,'Louane', 'Chanteuse révélée dans The Voice et actrice', 'Variété française'),
    (16,'M. Pokora', 'Chanteur et danseur français', 'Variété française'),
    (17,'Céline Dion', 'Chanteuse québécoise populaire dans le monde entier', 'Variété française'),
    (18,'Véronique Sanson', 'Auteure-compositrice-interprète', 'Variété française'),
    (19,'Soprano', 'Rappeur et chanteur français', 'Variété française'),
    (20,'Michel Sardou', 'Chanteur de variété française', 'Variété française');
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
(10, 'Lee', 'Daniel', '1950-09-19', 'Chanteur', 10),
(11, 'Jean-Jacques', 'Goldman', '1951-10-11', 'Chanteur et compositeur français', 11),
(12, 'Mimie', 'Mathy', '1957-07-08', 'Actrice et humoriste', 11),
(13, 'Patrick', 'Bruel', '1959-05-14', 'Chanteur et acteur français', 11),
(14, 'Amel', 'Bent', '1985-06-21', 'Chanteuse française de R&B et de pop', 11),
(15, 'Michèle', 'Laroque', '1960-06-15', 'Actrice et humoriste', 11),
(16, 'Nicola', 'Sirkis', '1959-06-22', "Chanteur principal d\'Indochine", 12),
(17, 'Boris', 'Jardel', '1962-01-01', "Guitariste d\'Indochine", 12),
(18, 'Oli', 'de Sat', '1970-04-15', "Bassiste d\'Indochine", 12),
(19, 'Ludwig', ' Dahlberg', '1971-01-01', "Batteur d\'Indochine", 12),
(20, 'Matu', '', '1971-01-01', "Claviériste d\'Indochine", 12),
(21, 'Zaz', '', '1980-05-01', 'Chanteuse principale', 13),
(22, 'Stromae', '', '1985-03-12', 'Auteur-compositeur-interprète belge', 14),
(23, 'Louane', 'Emera', '1996-11-26', 'Chanteuse et actrice française', 15),
(24, 'M.Pokora', '', '1985-09-26', 'Chanteur et danseur français', 16),
(25, 'Céline', 'Dion', '1968-03-30', 'Chanteuse québécoise populaire', 17),
(26, 'Véronique', 'Sanson', '1949-04-24', 'Auteure-compositrice-interprète', 18),
(27, 'Soprano', '', '1979-01-14', 'Rappeur et chanteur français', 19),
(28, 'Michel', 'Sardou', '1947-01-26', 'Chanteur de variété française', 20);


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

insert into RESEAUX (idreseau, lienreseau, nomreseau)
values
(1, 'instagram/Beathles.com', 'Instagram'),
(2, 'instagram/RollingStones.com', 'Instagram'),
(3, 'instagram/ACDC.com', 'Instagram'),
(4, 'facebook/Queen.com', 'Facebook'),
(5, 'facebook/Nirvana.com', 'Facebook'),
(6, 'facebook/PNL.com', 'Facebook'),
(7, 'facebook/Arsenic.com', 'Facebook'),
(8, 'facebook/FonckyFamily.com', 'Facebook'),
(9, 'instagram/Casseurs.com', 'Instagram'),
(10, 'instagram/SCrew.com', 'Instagram');


-------

-- insertion des sous-styles

insert into SOUS_STYLE (ids, nomstyle)
values
(1, 'Rap'),
(2, 'Rock'),
(3, 'Variété française');


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

insert into REGARDER (idact, dateact, idbillet)
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

insert into ACCEDER (idconcert, idbillet)
values
(1, 1),
(2, 2),
(3, 3);



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

INSERT INTO CONCERT values('100','Vendredi','2023-09-22 18:00:00', 100, 'Main Stage');


--  test trigger lieuUtiliseAnnexe

INSERT INTO ACTIVITE_ANNEXE values(2, '2023-09-20 14:30:00', 'Entretien avec les artistes', 2, 'Main Stage');

-- test trigger nbPreinscrip

insert into LIEU values('test', 5, 0);
insert into CONCERT values(600, 'Vendredi', '2024-03-21 10:15:00', 100, 'test');
insert into ACCEDER values(600, 1);
insert into ACCEDER values(600, 2);
insert into ACCEDER values(600, 3);
insert into ACCEDER values(600, 4);
insert into ACCEDER values(600, 5);
insert into ACCEDER values(600, 6);
