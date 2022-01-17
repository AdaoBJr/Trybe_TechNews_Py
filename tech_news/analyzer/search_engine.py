from tech_news.database import search_news
from datetime import datetime

# Based on:
# https://stackoverflow.com/a/3483399/14362230
# https://stackoverflow.com/a/48693451/14362230


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    return [(val["title"], val["url"]) for val in search_news({"title": {
        "$regex": f"{title}", "$options": "i"
        }})]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    return [(val["title"], val["url"]) for val in search_news({
        "timestamp": {"$regex": f"{date}", "$options": "i"}})]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
