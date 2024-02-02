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
    # return app
    return app
