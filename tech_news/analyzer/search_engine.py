from tech_news.database import db
import re

# Requisito 6
def search_by_title(title):
    find_result = db.news.find({"title": re.compile(title, re.IGNORECASE)})    
    list_title = []
    for item in find_result:
        list_title += [(item["title"], item["url"])]
    return list_title


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
