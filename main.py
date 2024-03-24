from flask import Flask, Blueprint
from essentils.pages import *
from flask_login import LoginManager
app = Flask(__name__)


init_app(app)


app.run(debug=True, port=80)