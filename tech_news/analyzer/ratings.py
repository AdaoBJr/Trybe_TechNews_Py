from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    news_formated = []
    res = []
    for new in news:
        sum_amount = new["shares_count"] + new["comments_count"]
        news_formated.append((new["title"], new["url"], sum_amount))

    news_formated.sort(key=lambda tup: tup[2], reverse=True)

    for new in news_formated:
        res.append((new[0], new[1]))
    return res[0:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
