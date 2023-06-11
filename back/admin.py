from flask import Blueprint
from flask_login import login_required
from .models import User
from . import db

admin_bp = Blueprint('admin', __name__)

#TODO add restrictions for other users than admin
@admin_bp.route('/')
@login_required
def index():
    data = [(user.id,user.email, user.username, user.date_created, user.password) for user in User.query.all()]
    temp = ''
    for d in data:
        temp += f"<p>{str(d)}</p>"
    return temp