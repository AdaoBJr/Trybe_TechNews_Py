import tech_news.database as db_connection
from tech_news.database import db


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = db_connection.search_news({"title": {"$regex": title, '$options': 'i'}})
    filtered_news = []
    if len(news):
        for data in news:
            filtered_news.append((data['title'], data['url']))
        return filtered_news
    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
