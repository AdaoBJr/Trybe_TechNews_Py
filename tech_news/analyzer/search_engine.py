from tech_news.database import db
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    find_news = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    result_list = []
    for i in find_news:
        result_list += [(i["title"], i["url"])]
    return result_list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Data inválida')

    find_news = db.news.find({"timestamp": {"$regex": date}})
    result_list = []
    for i in find_news:
        result_list += [(i["title"], i["url"])]
    return result_list


# Requisito 8
def search_by_source(source):
    find_news = db.news.find({"sources": re.compile(source, re.IGNORECASE)})
    result_list = []
    for i in find_news:
        result_list += [(i["title"], i["url"])]
    return result_list


# Requisito 9
def search_by_category(category):
    find_news = db.news.find({
        "categories": re.compile(category, re.IGNORECASE)
        })
    result_list = []
    for i in find_news:
        result_list += [(i["title"], i["url"])]
    return result_list
