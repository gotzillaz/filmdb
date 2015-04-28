CREATE TABLE Film (
  FilmID        INTEGER     NOT NULL,
  Type          TEXT        NOT NULL,
  Name          TEXT        NOT NULL,
  Year          INTEGER     NOT NULL,
  Plot          TEXT        NOT NULL,
  Rating        REAL        NOT NULL,
  PRIMARY KEY (FilmID)
);

CREATE TABLE Detail (
  DetailID      INTEGER     NOT NULL,
  FilmID        INTEGER     NOT NULL,
  Language      TEXT        NOT NULL,
  ReleaseDate   TEXT        NOT NULL,
  Runtime       INTEGER     NOT NULL,
  AspectRatio   TEXT        NOT NULL,
  PRIMARY KEY (DetailID),
  FOREIGN KEY (FilmID) REFERENCES Film(FilmID)
);

CREATE TABLE Episode (
  EpisodeID     INTEGER     NOT NULL,
  FilmID        INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  Number        INTEGER     NOT NULL,
  Season        INTEGER     NOT NULL,
  PRIMARY KEY (EpisodeID),
  FOREIGN KEY (FilmID) REFERENCES Film(FilmID)
);

CREATE TABLE Company (
  CompanyID     INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  Country       TEXT        NOT NULL,
  PRIMARY KEY (CompanyID)
);

CREATE TABLE FilmCompany (
  FilmID        INTEGER     NOT NULL,
  CompanyID     INTEGER     NOT NULL,
  PRIMARY KEY (FilmID, CompanyID)
  FOREIGN KEY (FilmID) REFERENCES Film(FilmID)
  FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

CREATE TABLE Genre (
  GenreID       INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  PRIMARY KEY (GenreID)
);

CREATE TABLE FilmGenre (
  FilmID        INTEGER     NOT NULL,
  GenreID       INTEGER     NOT NULL,
  PRIMARY KEY (FilmID, GenreID)
  FOREIGN KEY (FilmID) REFERENCES Film(FilmID)
  FOREIGN KEY (GenreID) REFERENCES Genre(GenreID)
);

CREATE TABLE Person (
  PersonID      INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  Surname       TEXT        NOT NULL,
  Gender        TEXT        NOT NULL,
  Height        REAL        NOT NULL,
  Birth         TEXT        NOT NULL,
  PRIMARY KEY (PersonID)
);

CREATE TABLE Character (
  CharacterID   INTEGER     NOT NULL,
  PersonID      INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  Gender        TEXT        NOT NULL,
  PRIMARY KEY (CharacterID),
  FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);

CREATE TABLE FilmCharacter (
  FilmID        INTEGER     NOT NULL,
  CharacterID   INTEGER     NOT NULL,
  PRIMARY KEY (FilmID, CharacterID)
  FOREIGN KEY (FilmID) REFERENCES Film(FilmID)
  FOREIGN KEY (CharacterID) REFERENCES Character(CharacterID)
);

CREATE TABLE Direction (
  FilmID        INTEGER     NOT NULL,
  PersonID      INTEGER     NOT NULL,
  PRIMARY KEY (FilmID, PersonID)
  FOREIGN KEY (FilmID) REFERENCES Film(FilmID)
  FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);

CREATE TABLE Poster (
  PosterID      INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  Image         BLOB        NOT NULL,
  PRIMARY KEY (PosterID)
);

CREATE TABLE FilmPoster (
  FilmID        INTEGER     NOT NULL,
  PosterID      INTEGER     NOT NULL,
  PRIMARY KEY (FilmID, PosterID)
  FOREIGN KEY (FilmID) REFERENCES Film(FilmID)
  FOREIGN KEY (PosterID) REFERENCES Poster(PosterID)
);

CREATE TABLE PersonPoster (
  PersonID      INTEGER     NOT NULL,
  PosterID      INTEGER     NOT NULL,
  PRIMARY KEY (PersonID, PosterID)
  FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
  FOREIGN KEY (PosterID) REFERENCES Poster(PosterID)
);
