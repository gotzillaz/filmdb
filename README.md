# FilmDB
FilmDB is a website, which collects information about films and television series has been released or being released. The system provides basic information. Developers can access the information through system’s API.

## API ##
 Method | Url                    | Parameter
:------:|------------------------|----------
 get    | /schema                |
 post   | /select                | &lt;query&gt;
 post   | /table                 | &lt;name&gt;
 post   | wh/video               | &lt;id&gt;, &lt;name&gt;
 post   | wh/episode             | &lt;id&gt;, &lt;name&gt;
 post   | wh/company             | &lt;id&gt;, &lt;name&gt;
 post   | wh/person              | &lt;id&gt;, &lt;name&gt;
 post   | wh/character           | &lt;id&gt;, &lt;name&gt;
 post   | wh/poster              | &lt;id&gt;, &lt;name&gt;
 post   | wh/video/sq/detail     | &lt;id&gt;
 post   | wh/video/sq/episode    | &lt;id&gt;
 post   | wh/video/sq/company    | &lt;id&gt;
 post   | wh/video/sq/genre      | &lt;id&gt;
 post   | wh/video/sq/character  | &lt;id&gt;
 post   | wh/video/sq/poster     | &lt;id&gt;
 post   | wh/person/sq/character | &lt;id&gt;
 post   | wh/person/sq/poster    | &lt;id&gt;

<b>/schema:</b> return all tables schema of database in text format

<b>/select:</b> execute &lt;query&gt; as select statement and return that result in JSON Array format

<b>/table:</b> return all records of &lt;table&gt; in JSON Array format

<b>/wh/&lt;table&gt;:</b> return all records from &lt;table&gt; where(wh) &lt;id&gt; is matched in JSON Array format

<b>/wh/&lt;table&gt;/sq/&lt;subtable&gt;:</b> return all records from &lt;subtable&gt; by subquery(sq) exist in &lt;table&gt; and &lt;subtable&gt; in JSON Array format

## Developed by ##
Gang of Three (G.O.T)
