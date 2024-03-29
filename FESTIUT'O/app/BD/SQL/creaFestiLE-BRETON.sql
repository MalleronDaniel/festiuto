CREATE TABLE `ACTIVITE_ANNEXE` (
  `idact` int(3) NOT NULL AUTO_INCREMENT,
  `dateact` datetime NOT NULL,
  `typeact` VARCHAR(42) NOT NULL,
  `dureeact` float NOT NULL,
  `noml` VARCHAR(42) NOT NULL,
  PRIMARY KEY (`idact`, `dateact`)
);
CREATE TABLE `ARTISTE` (
  `idartiste` int(3) NOT NULL AUTO_INCREMENT,
  `nomartiste` VARCHAR(42),
  `prenomartiste` VARCHAR(42),
  `ddn` date ,
  `descriptiona` VARCHAR(42),
  `idgroupe` int(3),
  PRIMARY KEY (`idartiste`)
);
CREATE TABLE `BILLET` (
  `idbillet` int(3) NOT NULL AUTO_INCREMENT,	
  `typebillet` int(3) NOT NULL,
  `descbillet` VARCHAR(42),
  `prixbillet` float(6),
  `iduser` int(3),
  PRIMARY KEY (`idbillet`)
);
CREATE TABLE `CONCERT` (

  `idconcert` int(3) NOT NULL AUTO_INCREMENT,
  `jour` ENUM('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche') NOT NULL,
  `datedebutc` datetime NOT NULL,
  `duree` float NOT NULL,
  `noml` VARCHAR(42) NOT NULL,
  PRIMARY KEY (`idconcert`)
);
CREATE TABLE `GROUPE` (
  `idgroupe` int(3) NOT NULL AUTO_INCREMENT,
  `nomgroupe` VARCHAR(42) NOT NULL,
  `description` TINYTEXT NOT NULL,
  `lienvideo` VARCHAR(42),
  `stylemusical` VARCHAR(42) NOT NULL,
  PRIMARY KEY (`idgroupe`)
);
CREATE TABLE `HEBERGER`(
  `idh` int(3) NOT NULL AUTO_INCREMENT,
  `idgroupe` int(3) NOT NULL,
  `jourDebut` ENUM('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche') NOT NULL,
  `dureeH` int(2) NOT NULL,
  PRIMARY KEY (`idh`, `idgroupe`)
);
CREATE TABLE `HEBERGEMENT` (
  `idh` int(3) NOT NULL AUTO_INCREMENT,
  `adresse` VARCHAR(42) NOT NULL,
  `nbplace` int(5) NOT NULL,
  PRIMARY KEY (`idh`)
);
CREATE TABLE `INSTRUMENTS` (
  `idinstrument` int(3) NOT NULL AUTO_INCREMENT,
  `nominstrument` VARCHAR(42) NOT NULL,
  PRIMARY KEY (`idinstrument`)
);
CREATE TABLE `LIEU` (
  `noml` VARCHAR(42) NOT NULL,
  `capacite` int(5) NOT NULL,
  `scene` boolean NOT NULL,
  PRIMARY KEY (`noml`)
);
CREATE TABLE `PHOTOS`(
  `idphoto` int(3) NOT NULL AUTO_INCREMENT,
  `nomphoto` VARCHAR(42) NOT NULL,
  `photo` VARCHAR(42) NOT NULL,
  PRIMARY KEY (`idphoto`)
);
CREATE TABLE `RESEAUX` (

  `idreseau` int(3) NOT NULL AUTO_INCREMENT,
  `lienreseau` VARCHAR(42) NOT NULL,
  `nomreseau` VARCHAR(42) NOT NULL,
  PRIMARY KEY (`idreseau`)
);
CREATE TABLE `SOUS_STYLE` (
  `ids` int(3) NOT NULL AUTO_INCREMENT,
  `nomstyle` VARCHAR(42) NOT NULL,
  PRIMARY KEY (`ids`)
);
CREATE TABLE `UTILISATEUR` (
  `iduser` int(3) NOT NULL AUTO_INCREMENT,
  `nomuser` VARCHAR(42) NOT NULL,
  `ddn` date NOT NULL,
  `email` VARCHAR(42) NOT NULL,
  `mdp` VARCHAR(42) NOT NULL,
  `admin` boolean NOT NULL,
  PRIMARY KEY (`iduser`)
);
CREATE TABLE `ACCEDER` (
  `idconcert` int(3) NOT NULL,
  `idbillet` int(3) NOT NULL,
  PRIMARY KEY (`idconcert`,`idbillet`)
);
CREATE TABLE `APPRECIER` (
  `idgroupe` int(3) NOT NULL,
  `iduser` int(3) NOT NULL,
  PRIMARY KEY (`idgroupe`, `iduser`)
);
CREATE TABLE `AVOIR` (
  `ids` int(3) NOT NULL,
  `idgroupe` int(3) NOT NULL,
  PRIMARY KEY (`ids`, `idgroupe`)
);
CREATE TABLE `CONTENIR` (
  `idphoto` int(3) NOT NULL,
  `idgroupe` int(3) NOT NULL,
  PRIMARY KEY (`idphoto`, `idgroupe`)
);
CREATE TABLE `CONTRIBUER` (
  `idgroupe` int(3) NOT NULL,
  `idconcert` int(3) NOT NULL,
  `tempsdemontage` float NOT NULL,
  `tempsmontage` float NOT NULL,
  PRIMARY KEY (`idgroupe`, `idconcert`)
);


CREATE TABLE `JOUER` (
  `idinstrument` int(3) NOT NULL,
  `idartiste` int(3) NOT NULL,
  PRIMARY KEY (`idinstrument`, `idartiste`)
);

CREATE TABLE `PARTAGER` (
  `idreseau` int(3) NOT NULL,
  `idgroupe` int(3) NOT NULL,
  PRIMARY KEY (`idreseau`, `idgroupe`)
);

CREATE TABLE `PARTICIPER` (
  `idgroupe` int(3) NOT NULL,
  `idact` int(3) NOT NULL,
  `dateact` DATETIME NOT NULL,
  PRIMARY KEY (`idgroupe`, `idact`, `dateact`)
);
CREATE TABLE `REGARDER` (
  `idact` int(3) NOT NULL,
  `dateact` DATETIME NOT NULL,
  `idbillet` int(3) NOT NULL,
  PRIMARY KEY (`idact`, `dateact`, `idbillet`)
);
CREATE TABLE `SIMILAIRE` (
  `idgroupe` int(3) NOT NULL,
  `idgroupe_1` int(3) NOT NULL,
  PRIMARY KEY (`idgroupe`, `idgroupe_1`)
);
ALTER TABLE `ACTIVITE_ANNEXE` ADD FOREIGN KEY (`noml`) REFERENCES `LIEU` (`noml`);
ALTER TABLE `ARTISTE` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `CONCERT` ADD FOREIGN KEY (`noml`) REFERENCES `LIEU` (`noml`);
ALTER TABLE `APPRECIER` ADD FOREIGN KEY (`iduser`) REFERENCES `UTILISATEUR` (`iduser`);
ALTER TABLE `APPRECIER` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `AVOIR` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `AVOIR` ADD FOREIGN KEY (`ids`) REFERENCES `SOUS_STYLE` (`ids`);
ALTER TABLE `BILLET` ADD FOREIGN KEY (`iduser`) REFERENCES `UTILISATEUR` (`iduser`);
ALTER TABLE `CONTENIR` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `CONTENIR` ADD FOREIGN KEY (`idphoto`) REFERENCES `PHOTOS` (`idphoto`);
ALTER TABLE `CONTRIBUER` ADD FOREIGN KEY (`idconcert`) REFERENCES `CONCERT` (`idconcert`);
ALTER TABLE `CONTRIBUER` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `JOUER` ADD FOREIGN KEY (`idartiste`) REFERENCES `ARTISTE` (`idartiste`);
ALTER TABLE `JOUER` ADD FOREIGN KEY (`idinstrument`) REFERENCES `INSTRUMENTS` (`idinstrument`);
ALTER TABLE `PARTICIPER` ADD FOREIGN KEY (`idact`, `dateact`) REFERENCES `ACTIVITE_ANNEXE` (`idact`, `dateact`);
ALTER TABLE `PARTICIPER` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `REGARDER` ADD FOREIGN KEY (`idbillet`) REFERENCES `BILLET` (`idbillet`);
ALTER TABLE `REGARDER` ADD FOREIGN KEY (`idact`, `dateact`) REFERENCES `ACTIVITE_ANNEXE` (`idact`, `dateact`);
ALTER TABLE `SIMILAIRE` ADD FOREIGN KEY (`idgroupe_1`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `SIMILAIRE` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `HEBERGER` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `HEBERGER` ADD FOREIGN KEY (`idh`) REFERENCES `HEBERGEMENT` (`idh`);
ALTER TABLE `ACCEDER` ADD FOREIGN KEY (`idbillet`) REFERENCES `BILLET` (`idbillet`);
ALTER TABLE `ACCEDER` ADD FOREIGN KEY (`idconcert`) REFERENCES `CONCERT` (`idconcert`);

-- FONCTIONS 



DELIMITER |

CREATE FUNCTION prochaineDateEvenementGroupe(idGr int, heure datetime) RETURNS datetime
BEGIN
    DECLARE prochaineDate datetime;

    SELECT MIN(dateEvenement) INTO prochaineDate FROM (
        SELECT MIN(datedebutc) as dateEvenement
        FROM CONTRIBUER NATURAL JOIN CONCERT
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
    FROM CONTRIBUER NATURAL JOIN CONCERT
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
    DECLARE dateConcert datetime;
    DECLARE mes varchar(100);

    -- Récupérer la date du concert
    SELECT datedebutc FROM CONCERT WHERE idconcert = NEW.idconcert INTO dateConcert;

    -- Récupérer la dernière date d'événement du groupe
    SET dernierEvenement = derniereDateEvenementGroupe(NEW.idgroupe, dateConcert);

    -- Récupérer la prochaine date d'événement du groupe
    SET prochainEvenement = prochaineDateEvenementGroupe(NEW.idgroupe, dateConcert);

    -- Récupérer la durée du concert
    SELECT duree
    INTO dureeConcert
    FROM CONCERT
    WHERE idconcert = NEW.idconcert;

    -- Vérifier la disponibilité pour le concert
    IF dernierEvenement IS NOT NULL AND dernierEvenement > dateConcert THEN
        SET mes = CONCAT('Insertion impossible : temps de démontage trop proche du dernier événement du groupe ', NEW.idgroupe);
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;

    IF prochainEvenement IS NOT NULL AND ADDTIME(ADDTIME(dateConcert, CONCAT(dureeConcert, ':00:00')), CONCAT(NEW.tempsmontage, ':00:00')) > prochainEvenement THEN
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
                set msg = "INSERTION IMPOSSIBLE: lieu déjà utilisé impossible de créer un nouveau concert";
                signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
            end if;
            if new.datedebutc<ADDDATE(dateDebC, INTERVAL dureeC MINUTE) and new.datedebutc>=dateDebC then
                set msg = "INSERTION IMPOSSIBLE: lieu déjà utilisé impossible de créer un nouveau concert";
                signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
            end if;
            if newConcertFin>dateDebC and newConcertFin<ADDDATE(dateDebC, INTERVAL dureeC MINUTE) then
                set msg = "INSERTION IMPOSSIBLE: lieu déjà utilisé impossible de créer un nouveau concert";
                signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
            end if;
        end if;
    end while;
    close lesConcerts;
end |
DELIMITER ;


-- Bloquer l'insertion d'une activité annexe si le lieu est déjà utilisé pour le moment
DELIMITER |

create or replace trigger lieuUtiliseAnnexe before insert on ACTIVITE_ANNEXE for each row
begin
    declare dateactA datetime;
    declare dureeactA float;
    declare dateFinA datetime;
    declare nomlA varchar(42);
    declare msg varchar(100);
    declare newDureeActivite float;
    declare newActiviteFin datetime;

    declare fini boolean default false;
    declare lesActivites cursor for select dateact, dureeact, noml from ACTIVITE_ANNEXE;
    declare continue handler for not found set fini=true;

    select dureeact into newDureeActivite from ACTIVITE_ANNEXE where idact=new.idact and dateact=new.dateact;
    set newActiviteFin=ADDDATE(new.dateact, INTERVAL newDureeActivite HOUR);

    open lesActivites;
    while not fini do
        fetch lesActivites into dateactA, dureeactA, nomlA;
        if new.dateact>=dateactA and newActiviteFin<=ADDDATE(dateactA, INTERVAL dureeactA HOUR) then
            set msg = "INSERTION IMPOSSIBLE: lieu déjà utilisé impossible de créer une nouvelle activité";
            signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
        end if;
        if new.dateact<ADDDATE(dateactA, INTERVAL dureeactA HOUR) and new.dateact>=dateactA then
            set msg = "INSERTION IMPOSSIBLE: lieu déjà utilisé impossible de créer une nouvelle activité";
            signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
        end if;
        if newActiviteFin>dateactA and newActiviteFin<ADDDATE(dateactA, INTERVAL dureeactA HOUR) then
            set msg = "INSERTION IMPOSSIBLE: lieu déjà utilisé impossible de créer une nouvelle activité";
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

    select count(*) into nbDejaPreinsc from ACCEDER where idconcert=new.idconcert;
    select distinct capacite into capaciteLieu from ACCEDER natural join CONCERT natural join LIEU where idconcert=new.idconcert;

    if nbDejaPreinsc+1>capaciteLieu then
        set msg = "INSERTION IMPOSSIBLE: dépassement de capacité de lieu";
        signal SQLSTATE '45000' set MESSAGE_TEXT=msg;
    end if;
end |
DELIMITER ;

