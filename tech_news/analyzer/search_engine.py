from tech_news.database import db


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
