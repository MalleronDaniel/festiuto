CREATE TABLE `ACTIVITE_ANNEXE` (
  `idact` int(3),
  `dateact` datetime,
  `typeact` VARCHAR(42),
  `dureeact` float,
  PRIMARY KEY (`idact`, `dateact`)
);
CREATE TABLE `ARTISTE` (
  `idartiste` int(3),
  `nomartiste` VARCHAR(42),
  `prenomartiste` VARCHAR(42),
  `ddn` date,
  `descriptiona` VARCHAR(42),
  `idgroupe` int(3),
  PRIMARY KEY (`idartiste`)
);
CREATE TABLE `BILLET` (
  `idbillet` int(3),
  `typebillet` VARCHAR(42),
  `prixbillet` float(6),
  `nbjoursbillet` int(2),
  PRIMARY KEY (`idbillet`)
);
CREATE TABLE `CONCERT` (
  `jour` ENUM('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'),
  `datedebutc` datetime,
  `idconcert` int(3),
  `duree` float,
  `noml` VARCHAR(42),
  PRIMARY KEY (`jour`, `datedebutc`, `idconcert`)
);
CREATE TABLE `GROUPE` (
  `idgroupe` int(3),
  `nomgroupe` VARCHAR(42),
  `description` TINYTEXT,
  `lienvideo` VARCHAR(42),
  `stylemusical` VARCHAR(42),
  PRIMARY KEY (`idgroupe`)
);
CREATE TABLE `HEBERGER`(
  `idh` int(3),
  `idgroupe` int(3),
  `jourDebut` ENUM('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'),
  `dureeH` int(2),
  PRIMARY KEY (`idh`, `idGroupe`)
);
CREATE TABLE `HEBERGEMENT` (
  `idh` int(3),
  `adresse` VARCHAR(42),
  `nbplace` int(5),
  PRIMARY KEY (`idh`)
);
CREATE TABLE `INSTRUMENTS` (
  `idinstrument` int(3),
  `nominstrument` VARCHAR(42),
  PRIMARY KEY (`idinstrument`)
);
CREATE TABLE `LIEU` (
  `noml` VARCHAR(42),
  `capacite` int(5),
  `scene` boolean,
  PRIMARY KEY (`noml`)
);
CREATE TABLE `PHOTOS`(
  `idphoto` int(3),
  `nomphoto` VARCHAR(42),
  `photo` VARCHAR(42),
  PRIMARY KEY (`idphoto`)
);
CREATE TABLE `RESEAUX` (
  `idreseau` int(3),
  `lienreseau` VARCHAR(42),
  `nomreseau` VARCHAR(42),
  PRIMARY KEY (`idreseau`)
);
CREATE TABLE `SOUS_STYLE` (
  `ids` int(3),
  `nomstyle` VARCHAR(42),
  PRIMARY KEY (`ids`)
);
CREATE TABLE `UTILISATEUR` (
  `iduser` int(3),
  `nomuser` VARCHAR(42),
  `ddn` date,
  `email` VARCHAR(42),
  `idbillet` int(3),
  `mdp` VARCHAR(42),
  `admin` boolean,
  PRIMARY KEY (`iduser`)
);
CREATE TABLE `ACCEDER` (
  `jour` ENUM('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'),
  `datedebutc` datetime,
  `idconcert` int(3),
  `idbillet` int(3),
  `preinscription` boolean,
  PRIMARY KEY (`jour`, `datedebutc`, `idconcert`, `idbillet`)
);
CREATE TABLE `APPRECIER` (
  `idgroupe` int(3),
  `iduser` int(3),
  PRIMARY KEY (`idgroupe`, `iduser`)
);
CREATE TABLE `AVOIR` (
  `ids` int(3),
  `idgroupe` int(3),
  PRIMARY KEY (`ids`, `idgroupe`)
);
CREATE TABLE `CONTENIR` (
  `idphoto` int(3),
  `idgroupe` int(3),
  PRIMARY KEY (`idphoto`, `idgroupe`)
);
CREATE TABLE `CONTRIBUER` (
  `idgroupe` int(3),
  `jour` ENUM('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'),
  `datedebutc` datetime,
  `idconcert` int(3),
  `tempsdemontage` float,
  `tempsmontage` float,
  PRIMARY KEY (`idgroupe`, `jour`, `datedebutc`, `idconcert`)
);

CREATE TABLE `GEOLOCALISER` (
  `idact` int(3),
  `dateact` DATETIME,
  `noml` VARCHAR(42),
  PRIMARY KEY (`idact`, `dateact`, `noml`)
);
CREATE TABLE `JOUER` (
  `idinstrument` int(3),
  `idartiste` int(3),
  PRIMARY KEY (`idinstrument`, `idartiste`)
);
CREATE TABLE `PARTAGER` (
  `idreseau` int(3),
  `idgroupe` int(3),
  PRIMARY KEY (`idreseau`, `idgroupe`)
);
CREATE TABLE `PARTICIPER` (
  `idgroupe` int(3),
  `idact` int(3),
  `dateact` DATETIME,
  PRIMARY KEY (`idgroupe`, `idact`, `dateact`)
);
CREATE TABLE `POSSEDER`(
  `iduser` int(3),
  `idBillet` int(3),
  PRIMARY KEY (`iduser`, `idBillet`)
);
CREATE TABLE `REGARDER` (
  `idact` int(3),
  `dateact` DATETIME,
  `idbillet` int(3),
  PRIMARY KEY (`idact`, `dateact`, `idbillet`)
);
CREATE TABLE `SIMILAIRE` (
  `idgroupe` int(3),
  `idgroupe_1` int(3),
  PRIMARY KEY (`idgroupe`, `idgroupe_1`)
);
ALTER TABLE `ARTISTE` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `CONCERT` ADD FOREIGN KEY (`noml`) REFERENCES `LIEU` (`noml`);
ALTER TABLE `UTILISATEUR` ADD FOREIGN KEY (`idbillet`) REFERENCES `BILLET` (`idbillet`);
ALTER TABLE `ACCEDER` ADD FOREIGN KEY (`idbillet`) REFERENCES `BILLET` (`idbillet`);
ALTER TABLE `ACCEDER` ADD FOREIGN KEY (`jour`, `datedebutc`, `idconcert`) REFERENCES `CONCERT` (`jour`, `datedebutc`, `idconcert`);
ALTER TABLE `APPRECIER` ADD FOREIGN KEY (`iduser`) REFERENCES `UTILISATEUR` (`iduser`);
ALTER TABLE `APPRECIER` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `AVOIR` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `AVOIR` ADD FOREIGN KEY (`ids`) REFERENCES `SOUS_STYLE` (`ids`);
ALTER TABLE `CONTENIR` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `CONTENIR` ADD FOREIGN KEY (`idphoto`) REFERENCES `PHOTOS` (`idphoto`);
ALTER TABLE `CONTRIBUER` ADD FOREIGN KEY (`jour`, `datedebutc`, `idconcert`) REFERENCES `CONCERT` (`jour`, `datedebutc`, `idconcert`);
ALTER TABLE `CONTRIBUER` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `GEOLOCALISER` ADD FOREIGN KEY (`noml`) REFERENCES `LIEU` (`noml`);
ALTER TABLE `GEOLOCALISER` ADD FOREIGN KEY (`idact`, `dateact`) REFERENCES `ACTIVITE_ANNEXE` (`idact`, `dateact`);
ALTER TABLE `JOUER` ADD FOREIGN KEY (`idartiste`) REFERENCES `ARTISTE` (`idartiste`);
ALTER TABLE `JOUER` ADD FOREIGN KEY (`idinstrument`) REFERENCES `INSTRUMENTS` (`idinstrument`);
ALTER TABLE `PARTAGER` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `PARTAGER` ADD FOREIGN KEY (`idreseau`) REFERENCES `RESEAUX` (`idreseau`);
ALTER TABLE `PARTICIPER` ADD FOREIGN KEY (`idact`, `dateact`) REFERENCES `ACTIVITE_ANNEXE` (`idact`, `dateact`);
ALTER TABLE `PARTICIPER` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `REGARDER` ADD FOREIGN KEY (`idbillet`) REFERENCES `BILLET` (`idbillet`);
ALTER TABLE `REGARDER` ADD FOREIGN KEY (`idact`, `dateact`) REFERENCES `ACTIVITE_ANNEXE` (`idact`, `dateact`);
ALTER TABLE `SIMILAIRE` ADD FOREIGN KEY (`idgroupe_1`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `SIMILAIRE` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `HEBERGER` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `HEBERGER` ADD FOREIGN KEY (`idh`) REFERENCES `HEBERGEMENT` (`idh`);
ALTER TABLE `POSSEDER` ADD FOREIGN KEY (`iduser`) REFERENCES `UTILISATEUR` (`iduser`);
ALTER TABLE `POSSEDER` ADD FOREIGN KEY (`idBillet`) REFERENCES `BILLET` (`idbillet`);

-- FONCTIONS 



DELIMITER |

CREATE FUNCTION prochaineDateEvenementGroupe(idGr int, heure datetime) RETURNS datetime
BEGIN
    DECLARE prochaineDate datetime;

    SELECT MIN(dateEvenement) INTO prochaineDate FROM (
        SELECT MIN(datedebutc) as dateEvenement
        FROM CONTRIBUER
        WHERE idgroupe = idGr AND datedebutc > heure

        UNION ALL

        SELECT MIN(dateact) as dateEvenement
        FROM PARTICIPER
        WHERE idgroupe = idGr AND dateact > heure
    ) as evenements;

    RETURN prochaineDate;
END |

DELIMITER ;

DELIMITER |

CREATE FUNCTION derniereDateEvenementGroupe(idGr int, heure datetime) RETURNS datetime
BEGIN
    DECLARE dernierConcert datetime;
    DECLARE dateDerniereAct datetime;
    DECLARE dateEvenement datetime;
    DECLARE dureeConcert int;
    DECLARE dureeActAnnexe float;

    -- Trouver la dernière date de concert
    SELECT MAX(datedebutc) INTO dernierConcert 
    FROM CONTRIBUER
    WHERE idgroupe = idGr AND datedebutc < heure;

    -- Trouver la dernière date d'activité annexe
    SELECT MAX(dateact) INTO dateDerniereAct
    FROM PARTICIPER
    WHERE idgroupe = idGr AND dateact < heure;

    IF dernierConcert > dateDerniereAct THEN
        SELECT duree INTO dureeConcert FROM CONCERT NATURAL JOIN CONTRIBUER WHERE datedebutc = dernierConcert and idgroupe = idGr;
        SET dateEvenement = ADDDATE(dernierConcert, INTERVAL dureeConcert MINUTE);
        RETURN dateEvenement;
    END IF;
    
    IF dateDerniereAct > dernierConcert THEN
        SELECT dureeact INTO dureeActAnnexe FROM ACTIVITE_ANNEXE NATURAL JOIN PARTICIPER WHERE dateact = dateDerniereAct and idgroupe = idGr;
        SET dateEvenement = ADDDATE(dateDerniereAct, INTERVAL dureeActAnnexe HOUR);
        RETURN dateEvenement;
    END IF;

    IF dernierConcert IS NOT NULL AND dateDerniereAct IS NULL THEN
        SELECT duree INTO dureeConcert FROM CONCERT NATURAL JOIN CONTRIBUER WHERE datedebutc = dernierConcert AND idgroupe = idGr;
        SET dateEvenement = ADDDATE(dernierConcert, INTERVAL dureeConcert MINUTE);
        RETURN dateEvenement;
    END IF;
    
    IF dateDerniereAct IS NOT NULL AND dernierConcert IS NULL THEN
        SELECT dureeact INTO dureeActAnnexe FROM ACTIVITE_ANNEXE NATURAL JOIN PARTICIPER WHERE dateact = dateDerniereAct AND idgroupe = idGr;
        SET dateEvenement = ADDDATE(dateDerniereAct, INTERVAL dureeActAnnexe HOUR);
        RETURN dateEvenement;
    END IF;

    RETURN NULL;
END|

DELIMITER ;


-- TRIGGERS

DELIMITER |

CREATE TRIGGER groupeDisponibleConcert BEFORE INSERT ON CONTRIBUER
FOR EACH ROW
BEGIN
    DECLARE dernierEvenement datetime;
    DECLARE prochainEvenement datetime;
    DECLARE dureeConcert float;
    DECLARE mes varchar(100);

    -- Récupérer la dernière date d'événement du groupe
    SET dernierEvenement = derniereDateEvenementGroupe(NEW.idgroupe, NEW.datedebutc);

    -- Récupérer la prochaine date d'événement du groupe
    SET prochainEvenement = prochaineDateEvenementGroupe(NEW.idgroupe, NEW.datedebutc);

    -- Récupérer la durée du concert
    SELECT duree
    INTO dureeConcert
    FROM CONCERT
    WHERE idconcert = NEW.idconcert;

    -- Vérifier la disponibilité pour le concert
    IF dernierEvenement IS NOT NULL AND dernierEvenement > NEW.datedebutc THEN
        SET mes = CONCAT('Insertion impossible : temps de démontage trop proche du dernier événement du groupe ', NEW.idgroupe);
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;

    IF prochainEvenement IS NOT NULL AND ADDTIME(ADDTIME(NEW.datedebutc, CONCAT(dureeConcert, ':00:00')), CONCAT(NEW.tempsmontage, ':00:00')) > prochainEvenement THEN
        SET mes = CONCAT('Insertion impossible : concert trop proche du prochain événement du groupe ', NEW.idgroupe);
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;
END|

DELIMITER ;


DELIMITER |
CREATE TRIGGER groupeDisponibleActiviteAnnexe BEFORE INSERT ON PARTICIPER
FOR EACH ROW
BEGIN
    DECLARE dernierEvenement datetime;
    DECLARE prochainEvenement datetime;
    DECLARE dureeActAnnexe float;
    DECLARE mes varchar(100);

    -- Récupérer la dernière date d'événement du groupe
    SET dernierEvenement = derniereDateEvenementGroupe(NEW.idgroupe, NEW.dateact);

    -- Récupérer la prochaine date d'événement du groupe
    SET prochainEvenement = prochaineDateEvenementGroupe(NEW.idgroupe, NEW.dateact);

    -- Récupérer la durée de l'activité annexe
    SELECT dureeact
    INTO dureeActAnnexe
    FROM ACTIVITE_ANNEXE
    WHERE idact = NEW.idact AND dateact = NEW.dateact;

    -- Vérifier la disponibilité pour l'activité annexe
    IF dernierEvenement IS NOT NULL AND dernierEvenement > NEW.dateact THEN
        SET mes = CONCAT('Insertion impossible : activité annexe trop proche du dernier événement du groupe ', NEW.idgroupe);
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;

    IF prochainEvenement IS NOT NULL AND ADDDATE(NEW.dateact, INTERVAL dureeActAnnexe HOUR) > prochainEvenement THEN
        SET mes = CONCAT('Insertion impossible : activité annexe trop proche du prochain événement du groupe ', NEW.idgroupe);
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;
END|

DELIMITER ;

-- Bloquer l'insertion de concert si le lieu est déjà utilisé pour le moment
DELIMITER |

create or replace trigger lieuUtiliseConcert before insert on CONCERT for each row
begin
    declare jourC Varchar(42);
    declare dateDebC datetime;
    declare dureeC float;
    declare nomlC Varchar(42);
    declare msg varchar(100);
    declare newConcertFin datetime;

    declare fini boolean default false;
    declare lesConcerts cursor for select jour, datedebutc, duree, noml from CONCERT;
    declare continue handler for not found set fini=true;

    set newConcertFin=ADDDATE(new.datedebutc, INTERVAL new.duree MINUTE);

    open lesConcerts;
    while not fini do
        fetch lesConcerts into jourC, dateDebC, dureeC, nomlC;

        if new.jour=jourC and new.noml=nomlC then
            if new.datedebutc>=dateDebC and newConcertFin<=ADDDATE(dateDebC, INTERVAL dureeC MINUTE) then
                set msg = "INSERTION IMPOSSIBLE: nouveau concert se chevauche";
                signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
            end if;
            if new.datedebutc<ADDDATE(dateDebC, INTERVAL dureeC MINUTE) and new.datedebutc>=dateDebC then
                set msg = "INSERTION IMPOSSIBLE: nouveau concert se chevauche";
                signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
            end if;
            if newConcertFin>dateDebC and newConcertFin<ADDDATE(dateDebC, INTERVAL dureeC MINUTE) then
                set msg = "INSERTION IMPOSSIBLE: nouveau concert se chevauche";
                signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
            end if;
        end if;
    end while;
    close lesConcerts;
end |
DELIMITER ;

-- Bloquer l'insertion d'une activité annexe si le lieu est déjà utilisé pour le moment
DELIMITER |

create or replace trigger lieuUtiliseAnnexe before insert on GEOLOCALISER for each row
begin
    declare dateactA datetime;
    declare dureeactA float;
    declare dateFinA datetime;
    declare nomlA varchar(42);
    declare msg varchar(100);
    declare newDureeActivite float;
    declare newActiviteFin datetime;

    declare fini boolean default false;
    declare lesActivites cursor for select dateact, dureeact, noml from ACTIVITE_ANNEXE natural join GEOLOCALISER;
    declare continue handler for not found set fini=true;

    select dureeact into newDureeActivite from ACTIVITE_ANNEXE where idact=new.idact and dateact=new.dateact;
    set newActiviteFin=ADDDATE(new.dateact, INTERVAL newDureeActivite HOUR);

    open lesActivites;
    while not fini do
        fetch lesActivites into dateactA, dureeactA, nomlA;
        if new.dateact>=dateactA and newActiviteFin<=ADDDATE(dateactA, INTERVAL dureeactA HOUR) then
            set msg = "INSERTION IMPOSSIBLE: nouvelle activité se chevauche";
            signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
        end if;
        if new.dateact<ADDDATE(dateactA, INTERVAL dureeactA HOUR) and new.dateact>=dateactA then
            set msg = "INSERTION IMPOSSIBLE: nouvelle activité se chevauche";
            signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
        end if;
        if newActiviteFin>dateactA and newActiviteFin<ADDDATE(dateactA, INTERVAL dureeactA HOUR) then
            set msg = "INSERTION IMPOSSIBLE: nouvelle activité se chevauche";
            signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
        end if;
    end while;
    close lesActivites;
end |
DELIMITER ;

DELIMITER |
create or replace trigger nbPreinscrip before insert on ACCEDER for each row
begin
    declare nbDejaPreinsc int;
    declare capaciteLieu int;
    declare msg varchar(100);

    select count(*) into nbDejaPreinsc from ACCEDER where jour=new.jour and datedebutc=new.datedebutc and idconcert=new.idconcert;
    select distinct capacite into capaciteLieu from ACCEDER natural join CONCERT natural join LIEU where jour=new.jour and datedebutc=new.datedebutc and idconcert=new.idconcert;

    if nbDejaPreinsc+1>capaciteLieu then
        set msg = "INSERTION IMPOSSIBLE: dépassement de capacité de lieu";
        signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
    end if;
end |
DELIMITER ;

