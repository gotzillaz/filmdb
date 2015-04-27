CREATE TABLE Flim (
  FlimID      INTEGER   PRIMARY KEY   NOT NULL,
  Type        TEXT                    NOT NULL,
  Title       TEXT                    NOT NULL,
  Year        TEXT                    NOT NULL,
  Plot        TEXT                    NOT NULL
);

CREATE TABLE Episode (
  EpisodeID   INTEGER   PRIMARY KEY   NOT NULL,
  FlimID      INTEGER                 NOT NULL,
  Name        TEXT                    NOT NULL,
  Number      INTEGER                 NOT NULL,
  Season      TEXT                    NOT NULL,
  FOREIGN KEY (FlimID)  REFERENCES    Flim(FlimID)
);
