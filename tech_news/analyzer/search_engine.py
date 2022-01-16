from tech_news.database import search_news
import datetime


# Função feita com ajuda da Letícia Galvão
def valid_date(date):
    try:
        return datetime.datetime.strptime(date, '%Y-%m-%d')
        # return True
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 6
def search_by_title(title):
    """https://www.thecodebuzz.com/mongodb-query-case-sensitive-case-
    insensitive/"""
    results = search_news(
        {"title": {'$regex': title, '$options': 'i'}})

    ZERO = 0
    if len(results) > ZERO:
        for result in results:
            tupla_result = [(result['title'], result['url'])]
            return tupla_result
    return []


# Requisito 7
def search_by_date(date):
    results = search_news(
        {"timestamp": {'$regex': date}})
    date_validation = valid_date(date)

    # tupla_result = []

    if date_validation:
        for result in results:
            tupla_result = [(result['title'], result['url'])]
            return tupla_result
    return []


# Requisito 8
def search_by_source(source):
    results = search_news(
        {"sources": {"$elemMatch": {'$regex': source, '$options': 'i'}}})

    # tupla_result = []
    ZERO = 0
    if len(results) > ZERO:
        for result in results:
            tupla_result = [(result['title'], result['url'])]
            return tupla_result
    # print(results, "Camilaaa")
    return []


# Requisito 9
def search_by_category(category):
    results = search_news(
        {"categories": {"$elemMatch": {'$regex': category, '$options': 'i'}}})

    ZERO = 0
    if len(results) > ZERO:
        for result in results:
            tupla_result = [(result['title'], result['url'])]
            return tupla_result

    return []
