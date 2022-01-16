from tech_news.database import find_news


def myFunc(e):
    return e['popularidade']


# Requisito 10
def top_5_news():
    news_list = []
    news_data = find_news()
    # Source https://docs.python.org/pt-br/dev/howto/sorting.html
    items = sorted(news_data, key=lambda new:
                   new["shares_count"] + new["comments_count"],
                   reverse=True)[:5]

    for new in items:
        item = new["title"], new["url"]
        news_list.append(item)
    return news_list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
