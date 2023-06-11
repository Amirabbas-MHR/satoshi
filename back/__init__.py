from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    """creates the flask app"""

    app = Flask(__name__)

    #Configurations
    app.secret_key = "SECRET" #Secret key for encoding sessions
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    db.init_app(app)
    app.app_context().push() #DONT KNOW THE USAGE OF THIS

    #registering auth/models module
    from .auth import auth_bp #relative import
    from .models import User
    from .dashboard import dashboard_bp
    from .home import home_bp
    from .admin import admin_bp
    create_database(app) #creates the database if it doesn't exist

    app.register_blueprint(auth_bp, url_prefix = "/auth") #setting the prefix to /auth
    app.register_blueprint(dashboard_bp, url_prefix = "/dashboard") 
    app.register_blueprint(home_bp, url_prefix = "/home") 
    app.register_blueprint(admin_bp, url_prefix = "/admin")
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    #Registering the user loader function
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    @app.route("/")
    def index():
        return redirect(url_for("home.index"))
    #returns the app
    return app


def create_database(app):
    """creates the database"""
    if not path.exists("back/" + DB_NAME):
        db.create_all()
        print("Database created")
    