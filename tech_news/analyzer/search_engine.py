from tech_news.database import db
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    find_title = db.news.find({"title": re.compile(title, re.IGNORECASE)})    
    list_title = []
    for item in find_title:
        list_title += [(item["title"], item["url"])]
    return list_title


# Requisito 7
def search_by_date(date):
    # https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Data inválida')

    news_list = list(db.news.find({"timestamp": {"$regex": date}}))
    list_by_data = []
    for item in news_list:
        list_by_data += [(item["title"], item["url"])]
    return list_by_data


# Requisito 8
def search_by_source(source):
    find_news_by_font = db.news.find({
        "sources": re.compile(source, re.IGNORECASE)
        })    
    list_news = []
    for item in find_news_by_font:
        list_news += [(item["title"], item["url"])]
    return list_news


# Requisito 9
def search_by_category(category):
    find_news_by_category = db.news.find({
        "categories": re.compile(category, re.IGNORECASE)
        })    
    list_categories = []
    for item in find_news_by_category:
        list_categories += [(item["title"], item["url"])]
    return list_categories