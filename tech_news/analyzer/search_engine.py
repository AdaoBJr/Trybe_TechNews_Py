from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    matched_news = search_news({"title": {"$regex": title, "$options": "i"}})
    news_tuples = [(new["title"], new["url"]) for new in matched_news]
    return news_tuples


# Requisito 7

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def search_by_date(date):
    if validate_date(date):
        matched_news = search_news({"timestamp": {"$regex": date}})
        news_tuples = [(new["title"], new["url"]) for new in matched_news]
        return news_tuples
    else:
        raise ValueError("Data Invalida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
