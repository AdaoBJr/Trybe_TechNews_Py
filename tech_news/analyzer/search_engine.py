from tech_news.database import db
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    find_news = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    result_list = []
    for i in find_news:
        result_list += [(i["title"], i["url"])]
    return result_list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Data inválida')

    news_list = list(db.news.find({"timestamp": {"$regex": date}}))
    result_list = []
    for i in news_list:
        result_list += [(i["title"], i["url"])]
    return result_list


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
