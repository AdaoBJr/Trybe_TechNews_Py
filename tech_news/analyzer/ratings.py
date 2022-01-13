from tech_news.database import aggregation


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = aggregation()
    result = []
    for n in news:
        result.append((n["title"], n["url"]))
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    return print("Top 5 Categorias")
