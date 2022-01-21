from tech_news.database import db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = db.news.find({"title": {"$regex": title, "$options": "i"}})
    news_list = []

    for iNews in news:
        news_list.append((iNews["title"], iNews["url"]))

    return news_list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news = db.news.find({"timestamp": {"$regex": date}})
    list_titles = []

    for iNews in news:
        list_titles.append((iNews["title"], iNews["url"]))
    return list_titles


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
