from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    title_query = title.capitalize()
    query = {"title": {"$eq": title_query}}
    news_list = []
    search_list = search_news(query)
    for news in search_list:
        news_list.append((news['title'], news['url']))

    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
