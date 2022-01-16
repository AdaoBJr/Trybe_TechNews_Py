from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    find_title = search_news({"title": {'$regex': title, '$options': 'i'}})
    if find_title:
        for dic in find_title:
            tupla = [(dic["title"], dic["url"])]
            return tupla
    return []


def is_valid_date(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 7
def search_by_date(date):
    validate = is_valid_date(date)
    find_date = search_news({"timestamp": {'$regex': date}})
    if validate:
        for dic in find_date:
            tupla = [(dic["title"], dic["url"])]
            return tupla
    return []


# Requisito 8
def search_by_source(source):
    find_source = search_news({"sources": {'$regex': source, '$options': 'i'}})
    if find_source:
        for dic in find_source:
            tupla = [(dic["title"], dic["url"])]
            return tupla
    return []


# Requisito 9
def search_by_category(category):
    find_category = search_news({"categories": {'$regex': category, '$options': 'i'}})
    if find_category:
        for dic in find_category:
            tupla = [(dic["title"], dic["url"])]
            return tupla
    return []
