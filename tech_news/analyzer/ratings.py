from tech_news.database import find_news


# Requisito 10
def top_5_news():
    bd_news = find_news()
    news_with_ratings = []
    for new in bd_news:
        rating = new["shares_count"] + new["comments_count"]
        news_with_ratings.append((new["title"], new["url"], rating))
    news_with_ratings.sort(key=lambda news_tup: news_tup[2], reverse=True)
    rated_news = []
    for new in news_with_ratings:
        rated_news.append((new[0], new[1]))
    return rated_news[0:5]


# Requisito 11
def top_5_categories():
    bd_news = find_news()
    categories = [
        category for bd_new in bd_news for category in bd_new["categories"]]
    categories.sort(key=lambda category: category)
    return categories[0:5]
