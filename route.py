from flask import Flask, jsonify, render_template, request, Response
import json, sqlite3, re, traceback

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

@app.route("/sql")
def sql():
    c.execute("SELECT * FROM Film")
    return str(c.fetchall())
    #return str(len(st))

@app.route("/table")
def table():
    return readTableFile()

@app.route('/ajax', methods=['GET', 'POST'])
def ajaxtest():
    if request.method == "POST":
        user = request.form['username']
        pwd = request.form['password']
        print user, pwd , request.args, request.form
        return jsonify(user=user, pwd=pwd)  
    else:
        return jsonify(result="GET")

@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        try:
            print request.data, request.args, request.form
            data = json.loads(request.data)
            cur.execute(data['query'])
            lt = cur.fetchall()
            print json.dumps(lt)
            return Response(json.dumps(lt), mimetype='application/json') 
        except:
            print traceback.print_exec()
            return jsonify(error=str(traceback.print_exec()))
    else:
        pass

@app.route('/schema', methods=['GET','POST'])
def schema():
    if request.method == 'POST':
        try:
            return showTableSchemaObj()
        except:
            print traceback.print_exec()
            return jsonify(error=str(traceback.print_exec()))
    else:
        pass

@app.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        try:
            print request.data, request.args, request.form
            key = [], value = []
            for k in request.form.keys():
                key.append(k)
                value.append(request.form[k])
            query_str = 'INSERT INTO '+ request.form['table'] + '(' + ', '.join(key) + ') VALUES (' + ', '.join(value) + ')' 
            print "=== Query_str ==="
            print query_str
            conn.execute(query_str)
            conn.commit()
            return jsonify(status=True)
        except:
            print traceback.print_exec()
            return jsonify(status=False,error=str(traceback.print_exec()))
    else:
        pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
