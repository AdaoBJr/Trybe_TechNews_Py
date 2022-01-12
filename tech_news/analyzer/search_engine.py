from tech_news.database import db
import re


# Requisito 6
def search_by_title(title):
    news = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    news_list = []
    for notice in news:
        news_list += [(notice["title"], notice["url"])]
    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
