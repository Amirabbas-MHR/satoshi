from flask import Blueprint
from flask_login import login_required
from .models import User
from . import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    data = [(user.id,user.email, user.username, user.date_created, user.password) for user in User.query.all()]
    temp = ''
    for d in data:
        temp += f"<p>{str(d)}</p>"
    return temp