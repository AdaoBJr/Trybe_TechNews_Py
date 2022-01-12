import requests
import time
import parsel
# from datetime import datetime


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""

    selector = parsel.Selector(html_content)
    css_selector_string = "div.tec--card__info > h3 > a ::attr(href)"

    return selector.css(css_selector_string).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    result = selector.css("div.tec--list.tec--list--lg > a ::attr(href)").get()
    return result


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(text=html_content)

    share = selector.css('.tec--toolbar__item ::text').get() or 0
    comments = selector.css('#js-comments-btn ::attr(data-count)').get()
    writer = selector.css(
        '.tec--article__body-grid .z--font-bold a ::text'
    ).get()
    summary = "".join(selector.css(
        "div.tec--article__body > p:nth-child(1) ::text"
    ).getall()).strip()
    source = selector.css('.z--mb-16 .tec--badge ::text').getall()

    categories = selector.css(
        '.tec--badge.tec--badge--primary ::text'
    ).getall()

    def handle_number(element):
        if element is not None and element != 0 and element != ' ':
            if len(element.split(' ')) > 1:
                return int(element.split(' ')[1])
            return int(element.split(' ')[0])
        return 0

    def handle_author(element):
        if element is None:
            result = selector.css('.tec--author__info > p::text').get()
            return result
        return element.strip()

    my_dic = {
        "url": selector.css("link[rel=canonical] ::attr(href)").get(),
        "title": selector.css("#js-article-title ::text").get().strip(),
        "timestamp":  selector.css("time ::attr(datetime)").get(),
        "writer": handle_author(writer),
        "shares_count": handle_number(share),
        "comments_count": handle_number(comments),
        "summary": summary,
        "sources": [item.strip() for item in source],
        "categories": [category.strip() for category in categories]
    }

    return my_dic


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
