import re
from tech_news.database import db


# Requisito 6
def search_by_title(title):
    search_title = list(
        db.news.find({"title": re.compile(title, re.IGNORECASE)})
    )
    # buscando no banco e ignorando case sensitive
    result = []
    for titulo in search_title:
        result.append((titulo["title"], titulo["url"]))
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
