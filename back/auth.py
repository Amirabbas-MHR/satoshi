from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import User
from .tools import is_valid_email
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

#Managing auth routes

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember')== "1" else False

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('You have successfully logged in.', category='success')
                login_user(user, remember=remember)
                return redirect(url_for('dashboard.index'))
            else:
                flash('Invalid password.', category='error')
        else:
            flash('Email not found.', category='error')
    print(current_user.is_authenticated)
    return render_template('login.html', user = current_user)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_exists = User.query.filter_by(email=email).first()
        user_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash('Email already exists.', category='error')
        elif user_exists:
            flash('Username already exists.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 6:
            flash('Password must be at least 6 characters.', category='error')
        elif len(username) < 3:
            flash('Username must be at least 3 characters.', category='error')
        elif not is_valid_email(email):
            flash('Email invalid.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('You have successfully registered', category='success')
            return redirect(url_for('auth.login'))

    return render_template('register.html', user = current_user)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))