from flask import Flask, render_template, Blueprint


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def dashboard():
    return render_template('index.html')