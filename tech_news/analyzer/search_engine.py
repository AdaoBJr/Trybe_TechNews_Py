from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    search = search_news({
        'title': {
            '$regex': title,
            '$options': 'i',
        }
    })

    return [
        (news['title'], news['url'])
        for news in search
        if title.lower() in news['title'].lower()
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
