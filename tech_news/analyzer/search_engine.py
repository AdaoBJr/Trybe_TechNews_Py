from tech_news.database import find_news, search_news
import datetime


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
    # dica da Camila
    # https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo
    news = search_news({"timestamp": {"$regex": date}})
    result = []

    try:
        # https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat
        datetime.date.fromisoformat(date)
        for new in news:
            result.append((new["title"], new["url"]))
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    results_search_news = search_news(
        {"sources": {"$elemMatch": {'$regex': source}}})

    ZERO = 0
    if len(results_search_news) > ZERO:
        for result in results_search_news:
            tupla_result = [(result['title'], result['url'])]
            return tupla_result
    return []


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
