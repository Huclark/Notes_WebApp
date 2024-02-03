from flask import Blueprint, render_template, redirect

# Blueprint is simply used to indicate that this file
# has routes (.i.e URLs). It allows us to have routes defined
# in multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
