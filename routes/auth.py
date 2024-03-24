from flask import Flask, redirect, request, render_template, Blueprint, url_for


login_page = Blueprint('login', __name__)



@login_page.route('/auth')
def auth():
    return redirect(url_for('login.login'))


email = 'matheus@matheus'
senha = '1234'
@login_page.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_request = request.form['email']
        senha_request = request.form['password']
        if email_request == email and senha_request == senha:
            return redirect(url_for('dashboard.dashboard'))
        else:
            return render_template('login.html')
    return render_template('login.html')

register_page = Blueprint('register', __name__)

@register_page.route('/auth/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')