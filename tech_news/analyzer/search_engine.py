from tech_news.database import db
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    news_list = []
    for notice in news:
        news_list += [(notice["title"], notice["url"])]
    return news_list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        find_date = list(db.news.find({"timestamp": {"$regex": date}}))

        news_date = []
        for notice in find_date:
            news_date += [(notice["title"], notice["url"])]

        return news_date

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
