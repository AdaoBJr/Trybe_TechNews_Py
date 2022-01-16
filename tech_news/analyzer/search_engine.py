from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """https://www.thecodebuzz.com/mongodb-query-case-sensitive-case-
    insensitive/"""
    results = search_news(
        {"title": {'$regex': title, '$options': 'i'}})

    zero = 0
    if len(results) > zero:
        for result in results:
            tupla_result = [(result['title'], result['url'])]
            return tupla_result
    return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
