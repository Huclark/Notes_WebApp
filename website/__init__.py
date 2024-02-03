from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """Creates a flask app, initializes its secret key and
    returns the app

    Returns:
        object: app
    """
    # name of app
    app = Flask(__name__)
    # create secret key
    app.config['SECRET_KEY'] = 'dhskhdsskdjsfkjn'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    # initialize the database
    db.init_app(app)
    
    # register all blueprints here
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note  # so that we run our app init first loads all our
    # models before initialising or database
    
    # create the database
    create_database(app)
    
    # Tell flask which route user should be redirected to when not logged in
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        """Loads an existing user
        """
        return User.query.get(int(id))
    
    # return app
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
