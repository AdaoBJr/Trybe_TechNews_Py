import datetime
from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    news_database = find_news()
    new_list = []

    for new in news_database:
        if new["title"].lower() == title.lower():
            new_list.append((new["title"], new["url"]))
    return new_list


# Requisito 7
def search_by_date(date):
    news_database = find_news()
    new_list = []

    try:
        datetime.datetime.fromisoformat(date)
        for new in news_database:
            if new["timestamp"][0:10] == date:
                new_list.append((new["title"], new["url"]))

        return new_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
