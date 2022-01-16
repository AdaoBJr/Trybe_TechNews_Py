from tech_news.database import db
from tech_news.utils import format_news


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
    """Seu código deve vir aqui"""
