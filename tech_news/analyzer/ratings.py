from tech_news.database import db


# Requisito 10
def top_5_news():
    pipeline = [
        {"$project": {
            "popularity": {"$sum": ["shares_count", "comments_count"]},
            "title": True,
            "url": True,
        }},
        {
            "$sort": {
                "popularity": -1,
                "title": 1,
            },
        },
        {
            "$limit": 5,
        },
        {
            "$project": {
                "_id": False,
                "title": True,
                "url": True,
            },
        },
    ]
    news_list = list(db.news.aggregate(pipeline))
    result = []
    for notice in news_list:
        notice_tuple = (notice["title"], notice["url"])
        result.append(notice_tuple)
    return result

# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
