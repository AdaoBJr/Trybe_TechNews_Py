from tech_news.database import db
import re


# Requisito 6
def search_by_title(title):
    # https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently
    news_list = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    result = []
    for each_news in news_list:
        result += [(each_news['title'], each_news['url'])]
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
