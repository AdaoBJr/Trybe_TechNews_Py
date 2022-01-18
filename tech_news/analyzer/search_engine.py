from tech_news.database import search_news
from datetime import datetime

# BASED ON
# https://docs.python.org/3/library/datetime.html
# https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362


def search(field, text):
    news_list = search_news({field: {"$regex": text, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 6
def search_by_title(title):
    return search("title", title)


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date).timestamp()
    except ValueError:
        raise ValueError("Data inválida")
    return search("timestamp", date)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
