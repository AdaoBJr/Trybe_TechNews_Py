from tech_news.database import find_news
import datetime


#  Requisito 6
def search_by_title(title):
    news_list = find_news()
    result = []
    for news in news_list:
        if news["title"].lower() == title.lower():
            result.append((news["title"], news["url"]))
    return result


# Requisito 7
def search_by_date(date):
    news_list = find_news()
    result = []
    try:
        datetime.date.fromisoformat(date)
        for news in news_list:
            if news["timestamp"][0:10] == date:
                result.append((news["title"], news["url"]))
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
