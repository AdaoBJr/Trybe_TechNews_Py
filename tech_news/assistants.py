def list_strip(list_str):
    return [text.strip() for text in list_str]


seletores = {
    "url": "link[rel=canonical]::attr(href)",
    "title": "#js-article-title::text",
    "timestamp": "#js-article-date::attr(datetime)",
    "writer": ".z--font-bold",
    "shares_count": "#js-author-bar div:nth-child(1)::text",
    "comments_count": "#js-comments-btn::attr(data-count)",
    "sumary": "div.tec--article__body p:nth-child(1) *::text",
    "sources": ".z--mb-16 .tec--badge::text",
    "categories": ".tec--badge--primary::text",
    "list_titles": ".tec--list__item h3 a::attr(href)",
    "next_page": "div.tec--list.tec--list--lg > a::attr(href)",
}


URL_MAIN = "https://www.tecmundo.com.br/novidades"
