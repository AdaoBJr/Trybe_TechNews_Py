import re
from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = set()
    # https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    news = set()
    try:
        # https://docs.python.org/3/library/datetime.html
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
        # https://stackoverflow.com/questions/9978534/match-dates-using-python-regular-expressions/9978701
    news = search_news({"timestamp": re.compile(date)})
    return [(new["title"], new["url"]) for new in news]


# Requisito 8
def search_by_source(source):
    news = set()
    news = search_news({"sources": re.compile(source, re.IGNORECASE)})
    return [(new["title"], new["url"]) for new in news]    


# Requisito 9
def search_by_category(category):
    news = set()
    news = search_news({"categories": re.compile(category, re.IGNORECASE)})
    return [(new["title"], new["url"]) for new in news]
    