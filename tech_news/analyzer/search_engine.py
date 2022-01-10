from tech_news.database import db
import datetime


# https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
def search_by_title(title):
    news = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )
    return [(new["title"], new["url"]) for new in news]


def search_by_date(date):
    # https://www.tutorialspoint.com/How-to-do-date-validation-in-Python
    date_string = date
    date_format = "%Y-%m-%d"
    try:
        date_obj = datetime.datetime.strptime(date_string, date_format)
        str_date = str(date_obj.date())
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news = db.news.find(
            {"timestamp": {"$regex": (str_date)}},
            {"title": 1, "url": 1, "_id": 0},
        )
        return [(new["title"], new["url"]) for new in news]


# Requisito 8
def search_by_source(source):
    news = db.news.find(
        {"sources": {"$regex": source, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )
    return [(new["title"], new["url"]) for new in news]


def search_by_category(category):
    news = db.news.find(
        {"categories": {"$regex": category, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )
    return [(new["title"], new["url"]) for new in news]
