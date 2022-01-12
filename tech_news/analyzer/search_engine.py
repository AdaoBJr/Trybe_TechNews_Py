from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    result = find_news()
    data = []
    for notice in result:
        if notice['title'].lower() == title.lower():
            data.append((notice['title'], notice['url']))
    return data


# Requisito 7
def search_by_date(date):
    result = find_news()
    data = []
    try:
        datetime.date.fromisoformat(date)  # Documentação do Python
        for notice in result:
            if notice['timestamp'][0:10] == date:
                data.append((notice['title'], notice['url']))
        return data
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
