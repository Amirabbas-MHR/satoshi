from flask import Blueprint, render_template
from flask_login import current_user
from back.api_interfaces.news_api import Alphav_news
from random import choices



home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    av = Alphav_news()
    chosen_news_feed = av.get_news(count=5)
    chosen_news_feed
    if chosen_news_feed: #TODO maybe pickle this to avoid requesting too much
        return render_template("home.html", user = current_user, news_feed = chosen_news_feed)
    else:
        return "alphav feed error"
