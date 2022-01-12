from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news_list = find_news()
    result = []

    for news in news_list:
        news["count"] = news["shares_count"] + news["comments_count"]

    news_list.sort(key=lambda x: x["count"], reverse=True)
    top_five = news_list[:5]

    for news in top_five:
        result.append((news["title"], news["url"]))

    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
