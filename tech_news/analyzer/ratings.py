from tech_news.database import db


# Requisito 10
def top_5_news():
    all_news = db.news.aggregate(
        [
            {
                "$addFields": {
                    "popularity": {
                        "$add": ["$shares_count", "$comments_count"]
                    }
                }
            },
            {"$sort": {"popularity": -1}},
            {"$limit": 5},
        ]
    )
    return [(new["title"], new["url"]) for new in all_news]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
