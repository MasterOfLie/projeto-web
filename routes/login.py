from flask import Flask, render_template, Blueprint


login_page = Blueprint('login', __name__)

@login_page.route('/auth/login')
def login():
    return render_template('login.html')