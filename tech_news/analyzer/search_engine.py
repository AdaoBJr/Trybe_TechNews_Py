from tech_news.database import db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    list_news = []
    news = db.news.find({"title": {"$regex": title, "$options": "i"}})
    for i in news:
        list_news.append((i["title"], i["url"]))
    return list_news


# Requisito 7
def search_by_date(date):
    new = []
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    news = db.news.find({"timestamp": {"$regex": date}})
    for curNews in news:
        new.append((curNews["title"], curNews["url"]))
    return new


# Requisito 8
def search_by_source(source):
    list_titles = []
    news = db.news.find({"sources": {"$regex": source, "$options": "i"}})
    for curNews in news:
        list_titles.append((curNews["title"], curNews["url"]))
    return list_titles


# Requisito 9
def search_by_category(category):
    data_by_category = []
    news = db.news.find({"categories": {"$regex": category, "$options": "i"}})
    for curNews in news:
        data_by_category.append((curNews["title"], curNews["url"]))
    return data_by_category
