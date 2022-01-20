from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""


def sorted_value(val):
  top_val = val.sort()
  return top_val[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    empyt = []
    top_categories = []
    list_news = find_news()
    return list_news

