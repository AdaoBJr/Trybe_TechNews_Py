from tech_news.database import search_news
# https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
import re


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # search = search_news({'title': re.compile(title, re.IGNORECASE)})
    my_arr = []
    find = {"title": {"$regex": title, "$options": "i"}}
    send = search_news(find)
    for a in send:
      title = a.get("title")
      path = a.get("url")
      my_arr.append((title, path))
    return my_arr
      


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
