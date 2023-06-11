from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from datetime import timedelta

def create_app():
    """creates the flask app"""

    app = Flask(__name__)

    #Secret key for encoding sessions
    app.secret_key = "SECRET"

    #setting session lifetime
    app.permanent_session_lifetime = timedelta(days = 1)

    #registering auth module
    from .auth import auth
    app.register_blueprint(auth, url_prefix = "/auth")

    #returns the app
    return app

"""
#index page
@app.route("/")
def index():
    return {"message" : "index"}

#dashboard, different for each user
@app.route("/dashboard")
def dashboard():
    return {"user" : f"{session['email']}"}

#login page
@app.route("/login", methods = ["POST", "GET"])
def login():
    #request is either commiting data: POST
    if request.method == "POST":

        #making session stay in server for the time delta given
        session.permanent = True

        #Saving email and pass to session
        session['email'] = request.form['email']
        session['pwrd'] = request.form['pwrd']

        #redirects to dashboard
        return redirect(url_for("dashboard"))
    
    #or is getting the login page itself
    return render_template("login.html")


"""