from flask import Blueprint, flash, redirect, render_template, url_for
from datetime import datetime as dt


blueprint = Blueprint('root', __name__, url_prefix='')


@blueprint.route('/')
def index():
    mock_news = [
        {
            'title': 'Оксимирон последовал примеру Гуфа и умер',
            'url': 'https://www.example.com',
            'published': dt.now()
        }
    ]
    title = 'Новости Python'
    return render_template('root/index.html', title=title, news_list=mock_news)
