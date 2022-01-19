from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    news_found = find_news()
    news_list = []
    for news in news_found:
        if news["title"].lower() == title.lower():
            news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    news_found = find_news()
    news_list = []
    try:
        datetime.datetime.fromisoformat(date)
        for news in news_found:
            if news["timestamp"][0:10] == date:
                news_list.append((news["title"], news["url"]))
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
