from tech_news.database import find_news
import operator


# Requisito 10
def top_5_news():
    notices = find_news()
    if (notices):
        for notice in notices:
            notice["score"] = notice["shares_count"] + notice["comments_count"]
        sort_notice = (
            sorted(notices, key=operator.itemgetter("score"), reverse=True)
        )
        top_5 = sort_notice[:5]
        return [(notice["title"], notice["url"]) for notice in top_5]
    return []


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
