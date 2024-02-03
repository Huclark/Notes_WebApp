from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db
from flask_login import login_user, login_required, logout_user, current_user
# Blueprint is simply used to indicate that this file
# has routes (.i.e URLs). It allows us to have routes defined
# in multiple files
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

            flash('Incorrect password, try again.', category='error')
        else:
            flash('There is no account registered with that email.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully! Enter your details to sign in again.', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # form = "signup form"
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must have more than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must have more than 1 character.', category='error')
        elif password1 != password2:
            flash("Passwords don't match.", category='error')
        elif len(password1) < 7:
            flash('Password must have at least 7 characters.', category='error')
        else:
            # add user to database
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method='pbkdf2:sha256')
                )
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
