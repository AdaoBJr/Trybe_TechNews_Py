from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    news = [
        (
            new["title"],
            new["url"],
            new["shares_count"] + new["comments_count"],
        )
        for new in news
    ]
    # https://docs.python.org/pt-br/dev/howto/sorting.html
    top_news = sorted(news, key=lambda new: new[2], reverse=True)
    return [(new[0], new[1]) for new in top_news][:5]


# Requisito 11
def top_5_categories():
    news = find_news()
    news = [category for new in news for category in new["categories"]]
    return sorted(news, key=lambda new: new)[:5]
     

