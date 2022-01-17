from tech_news.helper import aggregation_news
from tech_news.helper import aggregation_categories


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = aggregation_news()
    result = []
    for n in news:
        result.append((n["title"], n["url"]))
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    categories = aggregation_categories()
    result = []
    for c in categories:
        result.append(c["_id"])
    return result
