from tech_news.database import db
import re


def search_notice(query):
    notices = db.news.find(query)
    return [(search_not["title"], search_not["url"]) for search_not in notices]


# Requisito 6
def search_by_title(title):
    return search_notice({"title": re.compile(title, re.IGNORECASE)})


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
