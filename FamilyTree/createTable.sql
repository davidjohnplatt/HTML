DROP TABLE Person;

CREATE TABLE Person
  (Pid          INTEGER  PRIMARY KEY ,
   Gen          INTEGER,
   Pantecedent  INTEGER,
   Mantecedant  INTEGER ,
   FirstName    TEXT,
   LastName     TEXT,
   Sex          TEXT,
   MarriedTo    INTEGER,
   Photo        TEXT,
   PhotoYear    INTEGER,
   DoB          TEXT,
   DoD          TEXT );
   
 DROP TABLE PersonChild;
   
 CREATE TABLE PersonChild
  (Pid          INTEGER,
   PChildId     INTEGER);