from flask import Flask

def create_app():
    """Creates a flask app, initializes its secret key and
    returns the app

    Returns:
        object: app
    """
    # name of app
    app = Flask(__name__)
    # create secret key
    app.config['SECRET KEY'] = 'dhskhdsskdjsfkjn'
    
    # register all blueprints here
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    # return app
    return app
