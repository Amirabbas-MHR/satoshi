from flask import Blueprint


home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
@home_bp.route('/')
def home():
    return "HOME"

