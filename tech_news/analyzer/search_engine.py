import tech_news.database as db_connection
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, '$options': 'i'}}
    news = db_connection.search_news(query)
    filtered_news = []
    for data in news:
        filtered_news.append((data['title'], data['url']))
    return filtered_news


def check_date_format(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    check_date_format(date)

    try:
        query = {"timestamp": {"$regex": date}}
        news = db_connection.search_news(query)
        filtered_news = []
        for data in news:
            filtered_news.append((data['title'], data['url']))
        return filtered_news
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    query = {"sources": {"$regex": source, '$options': 'i'}}
    news = db_connection.search_news(query)
    filtered_news = []
    for data in news:
        filtered_news.append((data['title'], data['url']))
    return filtered_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    query = {"categories": {"$regex": category, '$options': 'i'}}
    news = db_connection.search_news(query)
    filtered_news = []
    for data in news:
        filtered_news.append((data['title'], data['url']))
    return filtered_news
