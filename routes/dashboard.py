from flask import Flask, render_template, Blueprint


dashboard_page = Blueprint('dashboard', __name__)

@dashboard_page.route('/dashboard')
def dashboard():
    return render_template('index.html')