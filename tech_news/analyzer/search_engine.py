from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    case_sensitive_title = title.capitalize()
    news = search_news({"title": case_sensitive_title})
    result = []
    for n in news:
        result.append((n["title"], n["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
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
    """Seu código deve vir aqui"""
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    result = []
    for n in news:
        result.append((n["title"], n["url"]))
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    result = []
    for n in news:
        result.append((n["title"], n["url"]))
    return result
