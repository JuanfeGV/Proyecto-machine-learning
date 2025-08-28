from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
        name = None
        name = "Flask"
        return f"Helllo, {name}"

@app.route("/index")
def index():
        myname = "Flask"
        return render_template ('index.html', name=myname)