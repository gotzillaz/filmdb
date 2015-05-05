# FilmDB
FilmDB is a website, which collects information about films and television series has been released or being released. The system provides basic information. Developers can access the information through system’s API.


## API ##
Method |Url                    |Parameter
:-----:|-----------------------|---------
get    |/schema                |
post   |/select                |<query>
post   |/table                 |<name>

post   |wh/video               |<id>, <name>
post   |wh/episode             |<id>, <name>
post   |wh/company             |<id>, <name>
post   |wh/person              |<id>, <name>
post   |wh/character           |<id>, <name>
post   |wh/poster              |<id>, <name>

post   |wh/video/sq/detail     |<id>
post   |wh/video/sq/episode    |<id>
post   |wh/video/sq/company    |<id>
post   |wh/video/sq/genre      |<id>
post   |wh/video/sq/character  |<id>
post   |wh/video/sq/poster     |<id>
post   |wh/person/sq/character |<id>
post   |wh/person/sq/poster    |<id>

### Get schema ###
<b>Description:</b> Return all tables schema of database in text format.

### Post select ###
<b>Description:</b> Execute <query> as select statement and return that result in JSON Array format.

### Post table ###
<b>Description:</b> Return all records of <table> in JSON Array format.

### Post wh/<table> ###
<b>Description:</b> Return all records from <table> where(wh) <id> is matched in JSON Array format.

### Post wh/<table>/sq/<subtable> ###
<b>Description:</b> Return all records from <subtable> by subquery(sq) exist in <table> and <subtable> in JSON Array format.

## Developed by ##
Gang of Three (G.O.T)
