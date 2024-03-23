from flask import Flask, render_template, Blueprint


register_page = Blueprint('register', __name__)

@register_page.route('/auth/register')
def register():
    return render_template('register.html')