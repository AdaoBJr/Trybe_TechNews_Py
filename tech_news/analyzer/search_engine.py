from tech_news.database import db
import re


# Requisito 6
def search_by_title(title):
    found_news = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    result = []
    for news in found_news:
        result += [(news["title"], news["url"])]
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
