from tech_news.database import find_news
from tech_news.database import db

# Requisito 10


def top_5_news():
    result = find_news()
    data_news = []
    # Requisito feito com a ajuda do código a Alê, com autorização dela.
    # Ordenação por soma - https://docs.python.org/3/howto/sorting.html
    for notice in result:
        notice["soma"] = notice["shares_count"] + notice["comments_count"]

    result.sort(key=lambda x: x["soma"], reverse=True)
    top_five_news = result[:5]

    for notice in top_five_news:
        data_news.append((notice["title"], notice["url"]))

    return data_news


# Requisito 11
def top_5_categories():
    pipeline = [
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$project": {"categories": True}},
        {"$limit": 5},
    ]

    return [
        categorie["_id"] for categorie in list(db.news.aggregate(pipeline))
    ]
