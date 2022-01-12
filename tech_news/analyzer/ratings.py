from tech_news.database import find_news


# Requisito 10
def top_5_news():
    top_news = find_news()
    result = []

    for news in top_news:
        news["count"] = news["shares_count"] + news["comments_count"]

    top_news.sort(key=lambda x: x["count"], reverse=True)
    top_five = top_news[:5]

    for news in top_five:
        result.append((news["title"], news["url"]))
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
