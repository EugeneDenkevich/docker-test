from flask import Flask
from flask import render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('index.html', name=name)
