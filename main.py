from flask import Flask, Blueprint
from essentils.pages import *
from flask_login import LoginManager
app = Flask(__name__)


app.register_blueprint(home_page)
app.register_blueprint(admin_page )
app.register_blueprint(login_page)
app.register_blueprint(register_page)


app.run(debug=True, port=80)