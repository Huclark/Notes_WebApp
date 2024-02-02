from flask import Blueprint

# Blueprint is simply used to indicate that this file
# has routes (.i.e URLs). It allows us to have routes defined
# in multiple files
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"
