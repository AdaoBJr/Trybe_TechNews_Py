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
    news = find_news()
    res = []
    for new in news:
        if source.upper() in [src.upper() for src in new["sources"]]:
            res.append((new["title"], new["url"]))
            return res
        return []


# Requisito 9
def search_by_category(category):
    news = find_news()
    res = []
    for new in news:
        if category.upper() in [cat.upper() for cat in new["categories"]]:
            res.append((new["title"], new["url"]))
            return res
        return []
