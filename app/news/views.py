from flask import Blueprint, current_app, render_template
from flask_login import current_user, login_required
from app.news.models import News


blueprint = Blueprint('news', __name__, url_prefix='')


@blueprint.route('/')
def index():
    title = 'Новости Python'
    # my_weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    my_news = News.query.order_by(News.published.desc()).all()
    return render_template('news/index.html', page_title=title, news_list=my_news)
