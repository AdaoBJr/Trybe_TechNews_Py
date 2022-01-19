from tech_news.database import find_news
import datetime


# FONTE lower(): https://shortest.link/2z5G
# Requisito 6
def search_by_title(title):
    search_news = find_news()
    news_by_title = []
    for new in search_news:
        if new['title'].lower() == title.lower():
            item = new["title"], new["url"]
            news_by_title.append(item)
    return news_by_title


# FONTE strptime(): encr.pw/Pf9PS
# Requisito 7
def search_by_date(date):
    search_news = find_news()
    news_by_date = []
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        for new in search_news:
            if new['timestamp'][:10] == date:
                item = new["title"], new["url"]
                news_by_date.append(item)
        return news_by_date
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
