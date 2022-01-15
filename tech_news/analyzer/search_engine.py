from tech_news.database import db
from datetime import datetime as dt


# Requisito 6
def search_by_title(title):
    # Referência
    # https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
    news = db.news.find({"title": {"$regex": title, "$options": "i"}})
    titles_and_urls = []

    for n in news:
        titles_and_urls.append((n["title"], n["url"]))

    return titles_and_urls


# Requisito 7
def search_by_date(date):
    try:
        # REFERÊNCIA
        # https://docs.python.org/3/library/datetime.html#datetime.date.strftime
        dt.strptime(date, "%Y-%m-%d")

    except ValueError:
        raise ValueError("Data inválida")

    news = db.news.find({"timestamp": {"$regex": date}})
    titles_and_urls = []

    for n in news:
        titles_and_urls.append((n["title"], n["url"]))

    return titles_and_urls


# Requisito 8
def search_by_source(source):
    # REFERÊNCIA
    # https://stackoverflow.com/questions/35321004/mongodb-query-in-with-regex-array-of-element/35321231
    news = db.news.find({"sources": {"$regex": source, "$options": "i"}})
    titles_and_urls = []

    for n in news:
        titles_and_urls.append((n["title"], n["url"]))

    return titles_and_urls


# Requisito 9
def search_by_category(category):
    news = db.news.find({"categories": {"$regex": category, "$options": "i"}})
    titles_and_urls = []

    for n in news:
        titles_and_urls.append((n["title"], n["url"]))

    return titles_and_urls
