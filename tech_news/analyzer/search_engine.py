from tech_news.database import find_news


def getTitleAndUrl(fullNews):
    filteredNews = []

    for news in fullNews:
        filteredNews.append((news['title'], news['url']))

    return filteredNews


# Requisito 6
def search_by_title(title):
    allNews = find_news()

    fullNews = [n for n in allNews if title.lower() == n['title'].lower()]

    return getTitleAndUrl(fullNews)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
