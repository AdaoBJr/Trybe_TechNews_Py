import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    find_news = db.find_news()
    return [
        (notice["title"], notice["url"])
        for notice in find_news
        if title.lower() in notice["title"].lower()
    ]


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    validate_date(date)
    find_news = db.find_news()
    return [
        (notice["title"], notice["url"])
        for notice in find_news
        if datetime.strptime(date, "%Y-%m-%d").date()
        == datetime.strptime(notice["timestamp"], "%Y-%m-%dT%H:%M:%S").date()
    ]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
