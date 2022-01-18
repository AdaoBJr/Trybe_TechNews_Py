import datetime
from tech_news.database import search_news

# https://github.com/tryber/sd-010-b-tech-news/blob/angelobittencourt-tech-news/tech_news/analyzer/search_engine.py


# Requisito 6
def search_by_title(title):
    case_sensitive_title = title.capitalize()
    news = search_news({"title": {"$regex": case_sensitive_title}})
    result = []
    for n in news:
        result.append((n["title"], n["url"]))
    return result


# Requisito 7
def search_by_date(date):
    news = search_news({"timestamp": {"$regex": date}})
    result = []
    try:
        datetime.date.fromisoformat(date)
        for n in news:
            result.append((n["title"], n["url"]))
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    result = []
    for n in news:
        result.append((n["title"], n["url"]))
    return result


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    result = []
    for n in news:
        result.append((n["title"], n["url"]))
    return result
