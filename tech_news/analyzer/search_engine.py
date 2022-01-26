from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    search = search_news({
        'title': {
            '$regex': title,
            '$options': 'i',
        }
    })

    return [  # I got helped by my friend Adão
        (news['title'], news['url'])
        for news in search
        if title.lower() in news['title'].lower()
    ]


# Requisito 7
def search_by_date(date):
    search = search_news({
        'timestamp': {
            '$regex': date,
        }
    })

    try:
        datetime.strptime(date, '%Y-%m-%d')  # Python Doc
        return [
            (news['title'], news['url'])
            for news in search
        ]
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
