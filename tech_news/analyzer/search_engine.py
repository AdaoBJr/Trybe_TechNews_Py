
from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    result = find_news()
    data = []
    for notice in result:
        if notice['title'].lower() == title.lower():
            data.append((notice['title'], notice['url']))
    return data


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
