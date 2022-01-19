from tech_news.database import search_news

# Requisito 6


def search_by_title(title):
    result = [
        (news["title"], news["url"])
        for news in search_news(
            {"title": {"$regex": f"{title}", "$options": "i"}}
        )
    ]
    # The $options with ‘I’ parameter means case insensitivity
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
