from tech_news.database import db
from datetime import datetime
import re


def format_news(array_news):
    result = []
    for news in array_news:
        result.append((news['title'], news['url']))
    return result


# Requisito 6
def search_by_title(title):
    regx_title = re.compile(title, re.IGNORECASE)
    array_news = list(db.news.find({"title": regx_title}))
    return format_news(array_news)


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
    return format_news(array_news)


# Requisito 8
def search_by_source(source):
    regx_source = re.compile(source, re.IGNORECASE)
    array_news = list(db.news.find({"sources": {"$in": [regx_source]}}))
    return format_news(array_news)


# Requisito 9
def search_by_category(category):
    regx_category = re.compile(category, re.IGNORECASE)
    array_news = list(db.news.find({"categories": {"$in": [regx_category]}}))
    return format_news(array_news)


""" regex: https://stackoverflow.com/questions/3483318/
performing-regex-queries-with-pymongo """

""" date: https://pt.stackoverflow.com/questions/377579/
valida%C3%A7%C3%A3o-de-data-testes-com-python """
