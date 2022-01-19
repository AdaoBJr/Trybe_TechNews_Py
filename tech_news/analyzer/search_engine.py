from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    selected_news = search_news(query)
    tupla_title_url = [(item["title"], item["url"]) for item in selected_news]

    return tupla_title_url


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
