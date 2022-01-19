from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    news = find_news()
    res = []
    for new in news:
        if new["title"].upper() == title.upper():
            res.append((new["title"], new["url"]))
            print(res)
    return res


# Requisito 7
def search_by_date(date):
    news = find_news()
    res = []
    for new in news:
        try:
            datetime.date.fromisoformat(date)
            if date in new["timestamp"]:
                res.append((new["title"], new["url"]))
            return res
        except ValueError:
            raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
