from tech_news.database import db
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    found_news = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    result = []
    for news in found_news:
        result += [(news["title"], news["url"])]
    return result


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Data inválida')

    found_news = db.news.find({"timestamp": {"$regex": date}})
    result = []
    for news in found_news:
        result += [(news["title"], news["url"])]
    return result


# Requisito 8
def search_by_source(source):
    found_news = db.news.find({"sources": re.compile(source, re.IGNORECASE)})
    result = []
    for news in found_news:
        result += [(news["title"], news["url"])]
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
