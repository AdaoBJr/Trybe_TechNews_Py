from tech_news.database import db
import re


# Requisito 6
def search_by_title(title):
    regx = re.compile(title, re.IGNORECASE)
    array_news = list(db.news.find({"title": regx}))
    result = []
    for news in array_news:
        result.append((news['title'], news['url']))
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
