from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = search_news({"title": {"$regex": f"{title}", "$options": "i"}})
    results = [(new["title"], new["url"]) for new in news]
    return results


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    news = search_news({"timestamp": {"$regex": f"{date}"}})
    results = [(new["title"], new["url"]) for new in news]
    return results


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = search_news({"sources": {"$regex": f"^{source}$", "$options": "i"}})
    results = [(new["title"], new["url"]) for new in news]
    return results


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
