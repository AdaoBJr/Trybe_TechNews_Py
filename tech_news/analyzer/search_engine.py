from tech_news.database import find_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = find_news()
    list_news = []

    for new in news:
        if new['title'].lower() == title.lower():
            list_news.append((new['title'], new['url']))

    return list_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        news = find_news()
        date_search = datetime.strptime(date, '%Y-%m-%d').date()
        list_news = []

        for new in news:
            array_date = new['timestamp'].split("T")
            date_news = datetime.strptime(array_date[0], '%Y-%m-%d').date()
            if date_search == date_news:
                list_news.append((new['title'], new['url']))
    except ValueError:
        raise ValueError('Data inválida')

    return list_news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
