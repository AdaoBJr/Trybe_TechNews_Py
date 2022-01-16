from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    searching_for_all_news = find_news()
    result = []

    for new in searching_for_all_news:
        # usei o lower pra padronizar a pesquisa pois as noticias vem com
        # letra maiúsula
        if new["title"].lower() == title.lower():
            result.append((new["title"], new["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
