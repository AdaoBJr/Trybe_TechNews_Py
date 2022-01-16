from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": title.lower()}

    result = search_news(query)

    tupla_title_url = [(item.title, item.url) for item in result]

    return tupla_title_url


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        query = {"timestamp": {"$regex": date}}

        result = search_news(query)

        tupla_title_url = [(item.title, item.url) for item in result]

        return tupla_title_url
    except ValueError:
        return "Data inválida"


# Requisito 8
# https://petrim.com.br/blog/index.php/2018/08/22/consultando-dentro-de-arrays-no-mongodb/
def search_by_source(source):
    query = {"sources": {"$elemMatch": {"$eq": source.lower()}}}

    result = search_news(query)

    tupla_title_url = [(item.title, item.url) for item in result]

    return tupla_title_url


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$elemMatch": {"$eq": category.lower()}}}

    result = search_news(query)

    tupla_title_url = [(item.title, item.url) for item in result]

    return tupla_title_url
