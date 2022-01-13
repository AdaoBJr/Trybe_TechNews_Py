import re
import datetime
from tech_news.database import db

# source
# https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently
# https://www.tutorialspoint.com/python/python_dictionary.htm
# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
# https://docs.mongodb.com/manual/reference/operator/query/regex/


# Requisito 6
def search_by_title(title):
    list_news = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    list_title_find = []
    for title_news in list_news:
        list_title_find.append((title_news["title"], title_news["url"]))
    return list_title_find


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    list_news = list(db.news.find({"timestamp": {"$regex": date}}))

    list_title_find = []
    for title_news in list_news:
        list_title_find.append((title_news["title"], title_news["url"]))
    return list_title_find


# Requisito 8
def search_by_source(source):
    list_news = db.news.find({"sources": re.compile(source, re.IGNORECASE)})

    list_title_find = []
    for title_news in list_news:
        list_title_find.append((title_news["title"], title_news["url"]))
    return list_title_find


# Requisito 9
def search_by_category(category):
    pass
