from flask import Blueprint

# Blueprint is simply used to indicate that this file
# has routes (.i.e URLs). It allows us to have routes defined
# in multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"
