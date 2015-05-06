# FilmDB
FilmDB is a website, which collects information about films and television series has been released or being released. The system provides basic information. Developers can access the information through system’s API.

## API ##
 Method | Url                    | Parameter
:------:|------------------------|----------
 get    | /schema                |
 post   | /select                | &lt;query&gt;
 post   | /table                 | &lt;name&gt;
 post   | wh/video               | &lt;id&gt;, &lt;name&gt;
 post   | wh/detail              | &lt;id&gt;
 post   | wh/episode             | &lt;id&gt;, &lt;name&gt;
 post   | wh/genre               | &lt;id&gt;, &lt;name&gt;
 post   | wh/company             | &lt;id&gt;, &lt;name&gt;
 post   | wh/person              | &lt;id&gt;, &lt;name&gt;
 post   | wh/character           | &lt;id&gt;, &lt;name&gt;
 post   | wh/director            | &lt;id&gt;
 post   | wh/poster              | &lt;id&gt;, &lt;name&gt;
 post   | wh/video/cn/detail     | &lt;id&gt;
 post   | wh/video/cn/episode    | &lt;id&gt;
 post   | wh/person/cn/character | &lt;id&gt;
 post   | wh/person/cn/director  | &lt;id&gt;
 post   | wh/video/cr/company    | &lt;id&gt;
 post   | wh/video/cr/genre      | &lt;id&gt;
 post   | wh/video/cr/character  | &lt;id&gt;
 post   | wh/video/cr/director   | &lt;id&gt;
 post   | wh/video/cr/poster     | &lt;id&gt;
 post   | wh/person/cr/poster    | &lt;id&gt;

<b>/schema:</b> return all tables schema of database in text format

```
curl -X GET <hostname>/schema
```

<b>/select:</b> execute &lt;query&gt; as select statement and return that result in JSON Array format

```
curl -d "query=SELECT * FROM Video" -X POST <hostname>/select
```

<b>/table:</b> return all records of &lt;table&gt; in JSON Array format

```
curl -d "name=Video" -X POST <hostname>/table
```

<b>/wh/&lt;table&gt;:</b> return all records from &lt;table&gt; where(wh) &lt;id&gt; is matched in JSON Array format

```
curl -d "id=1" -X POST <hostname>/wh/video
curl -d "name=The Fast and the Furious" -X POST <hostname>/wh/video
```

<b>/wh/&lt;table&gt;/cn/&lt;subtable&gt;:</b> return all records from &lt;subtable&gt; which connect(cn) and exist in &lt;table&gt; that &lt;id&gt; is matched in JSON Array format

```
curl -d "id=1" -X POST <hostname>/wh/video/cn/detail
```

<b>/wh/&lt;table&gt;/cr/&lt;subtable&gt;:</b> return all records from &lt;subtable&gt; which cross(cr) and exist in &lt;table&gt; that &lt;id&gt; is matched

```
curl -d "id=1" -X POST <hostname>/wh/video/cr/company
```

## Developed by ##
### Gang of Three (GoT) ###
* Supachai    Laparparat [@supachailllpay](https://github.com/supachailllpay)
* Bodin   Chinthanet [@gotzillaz](https://github.com/gotzillaz)
* Saringkarn  Pumjan [@SaringkarnP](https://github.com/SaringkarnP)
