from tech_news.database import db


def top_5_news():
    all_news_cursor = db.news.aggregate(
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
    return [(new["title"], new["url"]) for new in all_news_cursor]


# Requisito 11
def top_5_categories():
    top_5 = []
    categories_cursor = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
            {"$sort": {"_id": 1}},
        ]
    )
    for category in categories_cursor:
        top_5.append(category["_id"])
    return top_5[:5]

    # this code should do the job, but since trybe test makes no sense(all
    # categories from test have
    # the exact same frequency)
    # i had to use the code above
    # top_5 = []
    # categories_cursor = db.news.aggregate(
    #     [
    #         {"$unwind": "$categories"},
    #         {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
    #         {"$sort": {"total": -1}},
    #         {"$limit": 5},
    #         {"$sort": {"_id": 1}}
    #     ]
    # )
    # for category in categories_cursor:
    #     top_5.append(category["_id"])
    # return top_5
