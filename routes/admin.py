from flask import Flask, render_template, Blueprint


admin_page = Blueprint('admin', __name__)

@admin_page.route('/admin')
def admin():
    return render_template('admin.html')