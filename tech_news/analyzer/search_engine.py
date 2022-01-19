from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    response = find_news()
    search = []
    for new in response:
        if new["title"].lower() == title.lower():
            search.append((new["title"], new["url"]))
    return search


# Requisito 7
def search_by_date(date):
    response = find_news()
    search = []
    try:
        datetime.date.fromisoformat(date)
        for new in response:
            if new["timestamp"][0:10] == date:
                search.append((new["title"], new["url"]))
        return search
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
