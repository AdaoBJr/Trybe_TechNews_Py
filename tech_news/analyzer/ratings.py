from tech_news.database import db
from tech_news.utils import format_news
# from pprint import pprint


# Requisito 10
def top_5_news():
    array_news = list(db.news.aggregate(
        [
            {
                "$project": {
                    "title": "$title",
                    "url": "$url",
                    "popularity": {
                        "$sum": ["$shares_count", "$comments_count"]
                    }
                }
            },
            {
                "$sort": {
                    "popularity": -1,
                    "title": 1
                }
            },
            {
                "$limit": 5
            }
        ]
    ))

    return format_news(array_news)


# Requisito 11
def top_5_categories():
    array_categories = list(db.news.aggregate(
        [
            {
                "$unwind": "$categories"
            },
            {
                "$project": {
                    "category": "$categories",
                }
            },
            {
                "$group": {
                   "_id": "$category",
                   "qtd": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "qtd": -1,
                    "_id": 1
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "category": "$_id"
                }
            },
            {
                "$limit": 5
            }
        ]
    ))
    # pprint([obj["category"] for obj in array_categories])

    return [obj["category"] for obj in array_categories]
