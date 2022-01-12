from parsel import Selector


def getUrl(html_content):
    selector = Selector(text=html_content)
    link_canonical = selector.xpath(
        "//link[contains(@rel, 'canonical')]"
    ).get()
    url = Selector(text=link_canonical).css("::attr(href)").get()
    return url


def getTitle(html_content):
    selector = Selector(text=html_content)
    title = selector.css("#js-article-title::text").get().strip()
    return title


def getTimestamp(html_content):
    selector = Selector(text=html_content)
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    return timestamp


def getWriter(html_content):
    selector = Selector(text=html_content)
    getWritersByLinks = selector.xpath(
        "//a[contains(@href,'autor')]/text()"
    ).getall()
    writer = None
    for author in getWritersByLinks:
        if author is not None and author != "":
            writer = author.strip()
    getWriterByCss = selector.css(
        ".tec--author__info p:nth-child(1)::text"
    ).get()
    if getWriterByCss is not None:
        writer = getWriterByCss.strip()
    return writer


def getSharedCount(html_content):
    selector = Selector(text=html_content)
    shares_count = selector.css(
        "#js-author-bar .tec--toolbar__item::text"
    ).get()
    if shares_count == "":
        shares_count = 0
    elif shares_count is not None:
        shares_count = int(shares_count.split()[0])
    else:
        shares_count = 0
    return shares_count


def getCommentCount(html_content):
    selector = Selector(text=html_content)
    comments_count = selector.css("#js-comments-btn::text").get()
    if comments_count == "":
        comments_count = 0
    elif comments_count is not None:
        try:
            comments_count = int(comments_count.split()[0])
        except IndexError:
            comments_count = 0
    return comments_count


def getSummary(html_content):
    selector = Selector(text=html_content)
    getSummaryCss = selector.css(
        ".tec--article__body p:nth-child(1) *::text"
    ).getall()
    summary = "".join(getSummaryCss).strip("\/n")
    return summary


def getSource(html_content):
    selector = Selector(text=html_content)
    getSources = selector.css(
        ".tec--article__body-grid .z--mb-16 a::text"
    ).getall()
    sources = []
    for source in getSources:
        sources.append(source.strip())
    return sources


def getCategories(html_content):
    selector = Selector(text=html_content)
    getCategoriesCss = selector.css("#js-categories a::text").getall()
    categories = []
    for category in getCategoriesCss:
        categories.append(category.strip())
    return categories


def dictTechNews(html_content):
    news_info = {
        "url": getUrl(html_content),
        "title": getTitle(html_content),
        "timestamp": getTimestamp(html_content),
        "writer": getWriter(html_content),
        "shares_count": getSharedCount(html_content),
        "comments_count": getCommentCount(html_content),
        "summary": getSummary(html_content),
        "sources": getSource(html_content),
        "categories": getCategories(html_content),
    }

    return news_info
