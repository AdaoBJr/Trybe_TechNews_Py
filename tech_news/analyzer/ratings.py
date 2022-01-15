import tech_news.database as db


# Requisito 10
def top_5_news():
    news = db.find_news()
    top5 = []

    news.sort(
        key=lambda x: x["shares_count"] + x["comments_count"], reverse=True
    )

    for new in news:
        new["count"] = new["shares_count"] + new["comments_count"]

    top = news[:5]
    for new in top:
        top5.append((new["title"], new["url"]))
    return top5


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
