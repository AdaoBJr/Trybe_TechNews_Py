from tech_news.database import db
import datetime


# Requisito 6
# https://app.betrybe.com/course/computer-science/redes-e-raspagem-de-dados/raspagem-de-dados/ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/b63ffce8-be02-4be1-9b88-bda695400647/banco-de-dados/9eed5076-b74a-4789-aa19-b0564d12f5f8?use_case=side_bar
# https://docs.mongodb.com/manual/reference/operator/query/regex/
def search_by_title(title):
    news_list = []
    for new in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        item = new["title"], new["url"]
        news_list.append(item)
    return news_list


# Source https://stackoverflow.com/questions/9978534/match-dates-using-
# python-regular-expressions/9978701
def valid_date(datestring):
    try:
        datetime.datetime.strptime(datestring, '%Y-%m-%d')
        return True
    except ValueError:
        return False


# Requisito 7
def search_by_date(date):
    is_valid = valid_date(date)
    news_list = []

    if is_valid:
        for new in db.news.find({"timestamp": {"$regex": date,
                                               "$options": "i"}}):
            item = new["title"], new["url"]
            news_list.append(item)
        return news_list
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
