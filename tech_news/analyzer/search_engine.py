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
    dbNews = find_news()
    result = []
    try:
        datetime.date.fromisoformat(date)  # Documentação do Python
        for news in dbNews:
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
