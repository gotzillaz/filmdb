from flask import Flask
from flask import render_template
import json
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)

def objToJSON(st) :
    return json.dumps(st)

if __name__ == "__main__":
    app.run()
