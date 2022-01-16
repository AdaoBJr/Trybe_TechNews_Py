from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    dbNews = find_news()
    data = []
    for news in dbNews:
        if news["title"].lower() == title.lower():
            data.append((news["title"], news["url"]))
    return data


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news_list = find_news()
    result = []
    for news in news_list:
        result.append((news["title"], news["url"]))
    return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
