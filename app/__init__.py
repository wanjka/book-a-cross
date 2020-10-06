from flask import Flask, url_for
from flask_login import LoginManager, current_user
from flask_migrate import Migrate

# from app.admin.views import blueprint as admin_blueprint
from app.db import db
from app.root.views import blueprint as root_blueprint
from app.user.models import User
from app.user.views import blueprint as user_blueprint


# Implying "Factory" pattern
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    # app.register_blueprint(admin_blueprint)
    app.register_blueprint(root_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app


if __name__ == '__main__':
    app.run()
