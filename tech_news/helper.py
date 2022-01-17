from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def aggregation_news():
    return list(
        db.news.aggregate(
            [
                {
                    "$project": {
                        "_id": 0,
                        "url": 1,
                        "title": 1,
                        "total": {
                            "$add": ["$shares_count", "$comments_count"]
                        },
                    }
                },
                {"$sort": {"total": -1, "title": 1}},
                {"$limit": 5},
            ]
        )
    )


def aggregation_categories():
    return list(
        db.news.aggregate(
            [
                {"$unwind": "$categories"},
                {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
                {"$sort": {"count": -1, "_id": 1}},
                {"$limit": 5},
            ]
        )
    )
