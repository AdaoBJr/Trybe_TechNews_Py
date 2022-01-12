import re
from datetime import datetime
from tech_news.database import db


# Requisito 6
# https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently
def search_by_title(title):
    news_list = list(db.news.find({"title": re.compile(title, re.IGNORECASE)}))
    result = []
    for notice in news_list:
        notice_tuple = (notice["title"], notice["url"])
        result.append(notice_tuple)
    return result


# Requisito 7
# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Data inválida')

    news_list = list(db.news.find({"timestamp": {"$regex": date}}))
    result = []
    for notice in news_list:
        notice_tuple = (notice["title"], notice["url"])
        result.append(notice_tuple)
    return result


# Requisito 8
def search_by_source(source):
    news_list = list(db.news.find({
        "sources": re.compile(source, re.IGNORECASE)
    }))
    result = []
    for notice in news_list:
        notice_tuple = (notice["title"], notice["url"])
        result.append(notice_tuple)
    return result


# Requisito 9
def search_by_category(category):
    news_list = list(db.news.find({
        "categories": re.compile(category, re.IGNORECASE)
    }))
    result = []
    for notice in news_list:
        notice_tuple = (notice["title"], notice["url"])
        result.append(notice_tuple)
    return result
