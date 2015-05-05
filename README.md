# FilmDB
FilmDB is a website, which collects information about films and television series has been released or being released. The system provides basic information. Developers can access the information through system’s API.

## API ##

<b>Parameter format</b> : JSON Object <br>
<b>Result format</b> : JSON Array

Method | Route | Description | Parameter   
:-------:|-------|-------------|-------------
POST   |/select|Send SELECT statement to server and get query result| {query: 'sql_query'}
POST   |/list  |Get list of | {table: 'table_name'}
POST   |/video |Get video information by name or id | {name: 'video_name' or id: 'video_id'}
POST   |/character||
POST   |/person||
POST   |/company||
POST   |/episode||

## Developed by ##
Gang of Three (G.O.T)
