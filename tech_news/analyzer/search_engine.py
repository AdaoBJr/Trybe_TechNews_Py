from tech_news.database import db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = db.news.find({"title": {"$regex": title, "$options": "i"}})
    list_news = []

    for curNews in news:
        list_news.append((curNews["title"], curNews["url"]))

    return list_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:

        datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        raise ValueError("Data inválida")

    news = db.news.find({"timestamp": {"$regex": date}})
    list_titles = []

    for curNews in news:
        list_titles.append((curNews["title"], curNews["url"]))

    return list_titles


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = db.news.find({"sources": {"$regex": source, "$options": "i"}})
    list_titles = []

    for curNews in news:
        list_titles.append((curNews["title"], curNews["url"]))

    return list_titles


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
