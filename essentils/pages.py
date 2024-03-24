from routes.home import home_page
from routes.admin import admin_page
from routes.auth import login_page
from routes.auth import register_page
from routes.dashboard import dashboard_page

def init_app(app):
    app.register_blueprint(home_page)
    app.register_blueprint(admin_page)
    app.register_blueprint(login_page)
    app.register_blueprint(register_page)
    app.register_blueprint(dashboard_page)