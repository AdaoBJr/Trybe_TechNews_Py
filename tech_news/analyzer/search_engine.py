import re
from tech_news.database import db
from datetime import datetime


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
    try:
        datetime.strptime(date, "%Y-%m-%d")
        # para ver se a data está correta, se não vai pro erro
        search_date = list(db.news.find({"timestamp": {"$regex": date}}))
        itens = []
        for item in search_date:
            itens.append((item["title"], item["url"]))
        return itens
    except ValueError:
        raise ValueError("Data inválida")
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    # https://www.programiz.com/python-programming/datetime/strptime


# Requisito 8
def search_by_source(source):
    search = list(
        db.news.find({"sources": re.compile(source, re.IGNORECASE)})
    )

    itens = []
    for item in search:
        itens.append((item["title"], item["url"]))
    return itens


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
