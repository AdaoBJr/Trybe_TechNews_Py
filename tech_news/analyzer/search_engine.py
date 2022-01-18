from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    response = find_news()
    search = []
    for new in response:
        if new["title"].lower() == title.lower():
            search.append((new["title"], new["url"]))
    return search


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
