from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    db.init_app(app)
    # with app.app_context():
    #   db.create_all()


    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskpitch.users.routes import users
    from flaskpitch.posts.routes import posts
    from flaskpitch.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app