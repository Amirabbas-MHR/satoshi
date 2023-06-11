from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return 'logout'

@auth.route('/register', methods=['GET', 'POST'])
def register():
    return 'register'