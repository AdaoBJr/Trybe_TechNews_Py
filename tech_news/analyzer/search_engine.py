from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    # ale, zozimo, mari
    search_title = find_news()
    result = []

    for news in search_title:
        if news["title"].lower() == title.lower():
            result.append((news["title"], news["url"]))
    return result


# Requisito 7
def search_by_date(date):
    search_date = find_news()
    result = []

    try:
        datetime.date.fromisoformat(date)
        for news in search_date:
            if news["timestamp"][0:10] == date:
                result.append((news["title"], news["url"]))
        return result

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    search_source = find_news()
    result = []

    for news in search_source:
        for sourc in news["sources"]:
            if sourc.lower() == source.lower():
                result.append((news["title"], news["url"]))
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
