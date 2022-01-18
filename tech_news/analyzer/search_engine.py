from tech_news.database import find_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    found_news = find_news()
    result = []
    for new in found_news:
        if new["title"].lower() == title.lower():
            content = (new["title"], new["url"])
            result.append(content)
    return result


# Requisito 7
def search_by_date(date):
    found_news = find_news()
    try:
        datetime.strptime(date, "%Y-%m-%d").date()
        result = []
        for new in found_news:
            if (
                datetime.strptime(date, "%Y-%m-%d").date()
                == datetime.strptime(
                    new["timestamp"], "%Y-%m-%dT%H:%M:%S"
                ).date()
            ):
                content = (new["title"], new["url"])
                result.append(content)
            return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    found_news = find_news()
    result = []
    for new in found_news:
        for new_source in new["sources"]:
            if new_source.lower() == source.lower():
                content = (new["title"], new["url"])
                result.append(content)
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
