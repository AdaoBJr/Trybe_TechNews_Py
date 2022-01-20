from tech_news.database import search_news
# https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
# import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # search = search_news({'title': re.compile(title, re.IGNORECASE)})
    my_arr = []
    find_quer = {"title": {"$regex": title, "$options": "i"}}
    send = search_news(find_quer)
    for a in send:
        title = a.get("title")
        path = a.get("url")
        my_arr.append((title, path))
    return my_arr


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    my_arr = []
    datetime.strptime(date, "%Y-%m-%d")
    find_quer = {"timestamp":  {"$regex": date}}
    results = search_news(find_quer)
    if (results):
        for notice in results:
            my_arr.append((notice["title"], notice["url"]))
    else:
        raise ValueError("Data inválida")
    return my_arr


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
