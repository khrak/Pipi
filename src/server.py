from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='../templates')

@app.route("/")
def hello_world():
    return render_template('homePage.html')