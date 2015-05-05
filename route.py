from flask import Flask, jsonify, render_template, request, Response
import json, sqlite3, re, traceback, base64

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect('db.sqlite3')
conn.row_factory = dict_factory
conn.execute('PRAGMA foreign_keys = ON')
cur = conn.cursor()

app = Flask(__name__)

def showTableSchemaObj():
    f = open('table.sql','r')
    all_line = ''.join(f.readlines())
    tables = re.findall(r'CREATE TABLE (.*?);', all_line, re.S)
    all_obj = [] 
    for table in tables:
        name = table.split()[0]
        attrs = map(lambda x:x.strip(), re.findall(r'\((.*?)\n\)', table, re.S)[0].split(','))
        print "*"*50
        obj = {}
        obj['name'] = name
        print name
        print attrs
        al = []
        for at in attrs:
            if at[:11] == "PRIMARY KEY":
                break
            sp = at.split()
            attr_obj = {}
            attr_obj['name'] = sp[0]
            attr_obj['type'] = sp[1]
            if(sp[-2]+sp[-1] == "NOTNULL"): attr_obj['required'] = True 
            else : attr_obj['required'] = False
            al.append(attr_obj)
        print al
        obj['attr'] = al
        primary = map(lambda x:x.strip(), re.findall(r'PRIMARY KEY \((.*?)\)', table, re.S)[0].split(','))
        print primary
        obj['primary'] = primary
        foreign_lt = re.findall(r'REFERENCES (.*?)\((.*?)\)', table, re.S)
        foreign_obj_lt = []
        for ob in foreign_lt:
            foreign_obj_lt.append({'ref':ob[0], 'name':ob[1]})
        print foreign_obj_lt
        obj['foreign'] = foreign_obj_lt
        all_obj.append(obj)
    return json.dumps(all_obj)

def objToJSON(st) :
    return json.dumps(st)

def readTableFile():
    f = open('table.sql', 'r')
    all_line = ''.join(map(lambda x: x, f.readlines()))
    table = re.findall(r'CREATE(.*?));', all_line, re.S)
    f.close()
    return '=======\n'.join(table)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route("/table", methods=['POST'])
def table():
    try:
        sql_q = "SELECT * FROM %s" % (request.form['name'])
        cur.execute(sql_q)
        return json.dumps(cur.fetchall())
    except BaseException, e:
        print str(e)
        return jsonify(status=False,error=str(e))

@app.route("/wh/<table>", methods=['POST'])
def wt(table=None):
    try:
        sql_q = ""
        if 'id' in request.form:
            sql_q = "SELECT * FROM %s WHERE %sID='%s'" % (table, table, request.form['id'])
        else:
            sql_q = "SELECT * FROM %s WHERE Name='%s'" % (table, request.form['name'])
        cur.execute(sql_q)
        return json.dumps(cur.fetchall())
    except BaseException, e:
        print str(e)
        return jsonify(status=False,error=str(e))

@app.route("/wh/<m_table>/cn/<s_table>", methods=['POST'])
def wh_cn(m_table=None, s_table=None):
    try:
        m_table = m_table.capitalize()
        s_table = s_table.capitalize()
        sql_q = """ SELECT * FROM %s
                    WHERE %s.%sID IN
                    (
                        SELECT %s.%sID FROM %s
                        WHERE %s.%sID='%s'
                    )
                """ % (s_table, s_table, s_table, s_table, s_table, s_table, s_table, m_table, request.form['id'])
        cur.execute(sql_q)
        return json.dumps(cur.fetchall())
    except BaseException, e:
        print str(e)
        return jsonify(status=False,error=str(e))

@app.route("/wh/<m_table>/cr/<s_table>", methods=['POST'])
def wh_cr(m_table=None, s_table=None):
    try:
        m_table = m_table.capitalize()
        s_table = s_table.capitalize()
        sql_q = """ SELECT * FROM %s
                    WHERE %s.%sID IN
                    (
                        SELECT %s.%sID FROM %s
                        WHERE %s.%sID='%s'
                    )
                """ % (s_table, s_table, s_table, m_table+s_table, s_table, m_table+s_table, m_table+s_table, m_table, request.form['id'])
        cur.execute(sql_q)
        return json.dumps(cur.fetchall())
    except BaseException, e:
        print str(e)
        return jsonify(status=False,error=str(e))

@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        try:
            print request.data, request.args, request.form
            # data = json.loads(request.data)
            cur.execute(request.form['query'])
            print "Before"
            lt = cur.fetchall()
            '''
            for i in xrange(len(lt)):
                if 'Image' in lt[i]:
                    lt[i]['Image'] = base64.urlsafe_b64encode((lt[i]['Image']))
            '''
            print "After"
            print json.dumps(lt)
            return Response(json.dumps(lt), mimetype='application/json') 
        except BaseException, e:
            print str(e)
            return jsonify(status=False,error=str(e))
    else:
        pass

@app.route('/schema', methods=['GET','POST'])
def schema():
    if request.method == 'POST':
        try:
            return showTableSchemaObj()
        except BaseException, e:
            print str(e)
            return jsonify(status=False, error=str(e))
    else:
        try:
            cur.execute("SELECT sql FROM sqlite_master WHERE type='table'")
            res = cur.fetchall()
            print json.dumps('\n'.join(map(lambda x: x['sql'], res)))
            return json.dumps('\n'.join(map(lambda x: x['sql'], res)))
        except BaseException, e:
            print str(e)
            return jsonify(status=False, error=str(e))

@app.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        try:
            print request.data, request.args, request.form, request.files
            print len(request.files)
            key = []
            value = []
            for k in request.form.keys():
                if k == 'table':
                    continue
                key.append(k)
                value.append(request.form[k])
            for k in request.files.keys():
                key.append(k)
                value.append('data:' + request.files[k].mimetype + ';base64,' + base64.b64encode(sqlite3.Binary(request.files[k].read())))
            query_str = 'INSERT INTO '+ request.form['table'] + '(' + ', '.join(key) + ') VALUES (?'+',?'*(len(value)-1) +')'  #+ ', '.join(map(lambda x: '\"'+x+'\"',value)) + ')' 
            print "=== Query_str ==="
            print query_str
            conn.execute(query_str, tuple(value))
            conn.commit()
            return jsonify(status=True)
        except BaseException, e:
            print str(e)
            return jsonify(status=False,error=str(e))
    else:
        pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
