from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    news_found = find_news()
    result = []
    for new in news_found:
        if new["title"].lower() == title.lower():
            result.append((new["title"], new["url"]))
    return result


# Requisito 7
def search_by_date(date):
    news_found = find_news()
    result = []
    try:
        # https://docs.python.org/3/library/datetime.html
        datetime.datetime.fromisoformat(date)
        for new in news_found:
            if new["timestamp"][0:10] == date:
                result.append((new["title"], new["url"]))
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
