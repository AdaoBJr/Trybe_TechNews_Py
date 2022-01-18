import re
import datetime
from tech_news.database import search_news

# biblioteca re (que foi importante em basicamente todos os reqs aqui)
# lembrar de revisar biblioteca
# https://docs.python.org/pt-br/3/library/re.html


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_list = search_news({"title": re.compile(title, re.IGNORECASE)})
    if (news_list):
        for news in news_list:
            return [(news["title"], news["url"])]
    return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        # https://docs.python.org/pt-br/3/library/datetime.html
        datetime.datetime.strptime(date, "%Y-%m-%d")
        # https://www.programiz.com/python-programming/datetime/strptime
        news_list = search_news({"timestamp": re.compile(date)})
        if (news_list):
            for news in news_list:
                return [(news["title"], news["url"])]
        return []
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news_list = search_news({"sources": re.compile(source, re.IGNORECASE)})
    if (news_list):
        for news in news_list:
            return [(news["title"], news["url"])]
    return []


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news_list = search_news({
        "categories": re.compile(category, re.IGNORECASE)
        })
    if (news_list):
        for news in news_list:
            return [(news["title"], news["url"])]
    return []
