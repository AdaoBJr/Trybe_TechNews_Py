from tech_news.database import find_news


# Requisito 10
# AJUDA DA ALESSANDRA REZENDE
def top_5_news():
    result = find_news()
    data = []

    for notice in result:
        notice["soma"] = notice["shares_count"] + notice["comments_count"]

    result.sort(key=lambda x: x["soma"], reverse=True)
    top_five = result[:5]

    for notice in top_five:
        data.append((notice["title"], notice["url"]))

    return data


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
