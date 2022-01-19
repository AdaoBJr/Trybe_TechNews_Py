from tech_news.database import db


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    list = []
    for new in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        item = new["title"], new["url"]
        list.append(item)
    return list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
