from tech_news.database import db
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    list = []
    for new in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        item = new["title"], new["url"]
        list.append(item)
    return list


# Requisito 7
# verifica se a data esta no formato correto
def valid_date(datestring):
    try:
        datetime.datetime.strptime(datestring, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def search_by_date(date):
    """Seu código deve vir aqui"""
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
