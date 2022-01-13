import re
from tech_news.database import db

# source
# https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently
# https://www.tutorialspoint.com/python/python_dictionary.htm


# Requisito 6
def search_by_title(title):
    list_news = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    list_title_find = []
    for title_news in list_news:
        list_title_find.append((title_news["title"], title_news["url"]))
    return list_title_find


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
