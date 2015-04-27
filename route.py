from flask import Flask
from flask import render_template
import json, sqlite3

conn = sqlite3.connect('db.sqlite3')
conn.execute('PRAGMA foreign_keys = ON')
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)

def objToJSON(st) :
    return json.dumps(st)

if __name__ == "__main__":
    app.run()
