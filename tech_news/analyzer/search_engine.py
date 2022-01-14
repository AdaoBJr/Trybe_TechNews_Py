from tech_news.database import db
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    # https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently
    news_list = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    result = []
    for each_news in news_list:
        result += [(each_news['title'], each_news['url'])]
    return result


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Data inválida')

    news_list = db.news.find({"timestamp": {"$regex": date}})
    result = []
    for each_news in news_list:
        result += [(each_news['title'], each_news['url'])]
    return result


# Requisito 8
def search_by_source(source):
    news_list = db.news.find({"sources": re.compile(source, re.IGNORECASE)})
    result = []
    for each_news in news_list:
        result += [(each_news['title'], each_news['url'])]
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
