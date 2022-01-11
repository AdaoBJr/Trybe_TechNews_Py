from parsel import Selector


def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    links = selector.css('head link').xpath('@href').getall()

    matching = [s for s in links if "https://www.tecmundo.com.br" in s]
    url = matching[1]

    title = selector.css('#js-article-title::text').get()

    timestamp = selector.css(
        '.tec--timestamp__item > time::attr(datetime)').get()

    writer = selector.css(
        '.tec--article__body-grid .z--font-bold a::text').get()

    shares_count = selector.css('.tec--toolbar > .tec--toolbar__item::text')
    if not shares_count:
        shares_count = 0

    comments_count = int(selector.css(
        '#js-comments-btn::attr(data-count)').get())

    sources = selector.css('.z--mb-16 > div > a::text').getall()

    categories = selector.css("#js-categories a::text").getall()

    paragraph = selector.css('.tec--article__body > p:first-child *::text').getall()
    summary = "".join(paragraph)
    
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "sources": sources,
        "categories": categories,
        "summary": summary
    }


if __name__ == "__main__":
    path = (    
        "tests/"
        "assets/"
        "tecmundo_pages/"
        "dispositivos-moveis|"
        "215327-pixel-5a-tera-lancamento-limitado-devido-escassez-chips.htm."
        "html"
    )
    with open(path) as f:
        html_content = f.read()
    print(scrape_noticia(html_content))
