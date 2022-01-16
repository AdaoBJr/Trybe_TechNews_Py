from tech_news.database import search_news
from datetime import datetime


def find_regex(field, text):
    news = search_news({field: {"$regex": text, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 6
def search_by_title(title):
    return find_regex("title", title)


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date).timestamp()
    except ValueError:
        raise ValueError("Data inválida")
    return find_regex("timestamp", date)


# Requisito 8
def search_by_source(source):
    return find_regex("sources", source)


# Requisito 9
def search_by_category(category):
    return find_regex("categories", category)
