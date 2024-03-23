from flask import Flask, redirect, render_template, Blueprint, url_for


login_page = Blueprint('login', __name__)



@login_page.route('/auth')
def auth():
    return redirect(url_for('login.login'))

@login_page.route('/auth/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

register_page = Blueprint('register', __name__)

@register_page.route('/auth/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')