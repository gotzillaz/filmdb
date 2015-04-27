from flask import Flask, jsonify, render_template, request
import json, sqlite3, re

conn = sqlite3.connect('db.sqlite3')
conn.execute('PRAGMA foreign_keys = ON')
c = conn.cursor()

app = Flask(__name__)

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
        return jsonify(result="GGDP")  
    else:
        return jsonify(result="GET")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
