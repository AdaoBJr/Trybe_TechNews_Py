from tech_news.database import db
import datetime


# Requisito 6
# https://www.thecodebuzz.com/mongodb-query-case-sensitive-case-insensitive/
# MongoDb regex query with case insensitive search
def search_by_title(title):
    list = []
    for n in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        item = n["title"], n["url"]
        list.append(item)
    return list


# Leticia Galvão
def valid_date(datestring):
    try:
        datetime.datetime.strptime(datestring, '%Y-%m-%d')
        return True
    except ValueError:
        return False


# Requisito 7
def search_by_date(date):
    if valid_date(date):
        news = []
        for n in db.news.find({
            "timestamp": {"$regex": date, "$options": "i"}
        }):
            item = n["title"], n["url"]
            news.append(item)
        return news
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
