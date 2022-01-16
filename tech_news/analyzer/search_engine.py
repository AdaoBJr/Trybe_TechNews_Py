from tech_news.database import db
from datetime import datetime
import re


# Requisito 6
def search_by_title(title):
    regx_title = re.compile(title, re.IGNORECASE)
    array_news = list(db.news.find({"title": regx_title}))
    result = []
    for news in array_news:
        result.append((news['title'], news['url']))
    return result


def is_valid_date(data):
    try:
        datetime.strptime(data, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    is_valid_date(date)

    regx_date = re.compile(date, re.IGNORECASE)
    array_news = list(db.news.find({"timestamp": regx_date}))
    result = []
    for news in array_news:
        result.append((news['title'], news['url']))
    return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


""" regex: https://stackoverflow.com/questions/3483318/
performing-regex-queries-with-pymongo """

""" date: https://pt.stackoverflow.com/questions/377579/
valida%C3%A7%C3%A3o-de-data-testes-com-python """
