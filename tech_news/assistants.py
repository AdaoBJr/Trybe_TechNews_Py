def list_strip(list_str):
    return [text.strip() for text in list_str]


def get_writer(content):
    pipelines = [
        content.css(".tec--author__info__link::text").get(),
        content.css("#js-main div.tec--timestamp__item a::text").get(),
        content.css("#js-author-bar p::text").get(),
    ]
    result, *rest = [exists for exists in pipelines if exists]
    return result.strip() if result else result


seletores = {
    "url": "link[rel=canonical]::attr(href)",
    "title": "#js-article-title::text",
    "timestamp": "#js-article-date::attr(datetime)",
    "writer": ".tec--author__info__link::text",
    "shares_count": "#js-author-bar div:nth-child(1)::text",
    "comments_count": "#js-comments-btn::attr(data-count)",
    "sumary": "div.tec--article__body p:nth-child(1) *::text",
    "sources": "#js-main .z--mb-16.z--px-16 a::text",
    "categories": "#js-categories a::text",
    "list_titles": ".tec--list__item h3 a::attr(href)",
    "next_page": "div.tec--list.tec--list--lg > a::attr(href)",
}


URL_MAIN = "https://www.tecmundo.com.br/novidades"
