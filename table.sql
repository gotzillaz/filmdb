CREATE TABLE Video (
  VideoID       INTEGER     NOT NULL,
  Type          TEXT        NOT NULL,
  Name          TEXT        NOT NULL,
  Year          INTEGER     NOT NULL,
  Plot          TEXT        NOT NULL,
  Rating        REAL        NOT NULL,
  PRIMARY KEY (VideoID)
);
CREATE TABLE Detail (
  DetailID      INTEGER     NOT NULL,
  VideoID       INTEGER     NOT NULL,
  Language      TEXT        NOT NULL,
  ReleaseDate   TEXT        NOT NULL,
  Runtime       INTEGER     NOT NULL,
  AspectRatio   TEXT        NOT NULL,
  PRIMARY KEY (DetailID),
  FOREIGN KEY (VideoID) REFERENCES Video(VideoID)
);
CREATE TABLE Episode (
  EpisodeID     INTEGER     NOT NULL,
  VideoID       INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  Number        INTEGER     NOT NULL,
  Season        INTEGER     NOT NULL,
  PRIMARY KEY (EpisodeID),
  FOREIGN KEY (VideoID) REFERENCES Video(VideoID)
);
CREATE TABLE Company (
  CompanyID     INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  Country       TEXT        NOT NULL,
  PRIMARY KEY (CompanyID)
);
CREATE TABLE VideoCompany (
  VideoID       INTEGER     NOT NULL,
  CompanyID     INTEGER     NOT NULL,
  PRIMARY KEY (VideoID, CompanyID)
  FOREIGN KEY (VideoID) REFERENCES Video(VideoID)
  FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);
CREATE TABLE Genre (
  GenreID       INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  PRIMARY KEY (GenreID)
);
CREATE TABLE VideoGenre (
  VideoID       INTEGER     NOT NULL,
  GenreID       INTEGER     NOT NULL,
  PRIMARY KEY (VideoID, GenreID)
  FOREIGN KEY (VideoID) REFERENCES Video(VideoID)
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
CREATE TABLE VideoCharacter (
  VideoID       INTEGER     NOT NULL,
  CharacterID   INTEGER     NOT NULL,
  PRIMARY KEY (VideoID, CharacterID)
  FOREIGN KEY (VideoID) REFERENCES Video(VideoID)
  FOREIGN KEY (CharacterID) REFERENCES Character(CharacterID)
);
CREATE TABLE Director (
  VideoID       INTEGER     NOT NULL,
  PersonID      INTEGER     NOT NULL,
  PRIMARY KEY (VideoID, PersonID)
  FOREIGN KEY (VideoID) REFERENCES Video(VideoID)
  FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);
CREATE TABLE Poster (
  PosterID      INTEGER     NOT NULL,
  Name          TEXT        NOT NULL,
  Image         BLOB        NOT NULL,
  PRIMARY KEY (PosterID)
);
CREATE TABLE VideoPoster (
  VideoID       INTEGER     NOT NULL,
  PosterID      INTEGER     NOT NULL,
  PRIMARY KEY (VideoID, PosterID)
  FOREIGN KEY (VideoID) REFERENCES Video(VideoID)
  FOREIGN KEY (PosterID) REFERENCES Poster(PosterID)
);
CREATE TABLE PersonPoster (
  PersonID      INTEGER     NOT NULL,
  PosterID      INTEGER     NOT NULL,
  PRIMARY KEY (PersonID, PosterID)
  FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
  FOREIGN KEY (PosterID) REFERENCES Poster(PosterID)
);

