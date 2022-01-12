import re
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
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
