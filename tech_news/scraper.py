import requests
import time
import parsel
import re


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
    get_element = parsel.Selector(html_content)

    return get_element.css(
        "div.tec--card__info > h3 > a ::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    get_element = (
        parsel.Selector(html_content).css(".tec--btn--lg::attr(href)").get()
    )
    return get_element


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    get_element = parsel.Selector(html_content)

    class_select = {
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

    counter_share = get_element.css(class_select["shares_count"]).get() or "0"
    counter_coment = (
        get_element.css(class_select["comments_count"]).get() or "0"
    )

    def func_strip(list_str):
        return [text.strip() for text in list_str]

    return {
        "url": get_element.css(class_select["url"]).get(),
        "title": get_element.css(class_select["title"]).get(),
        "timestamp": get_element.css(class_select["timestamp"]).get(),
        "writer": get_element.css(".z--font-bold")
        .css("*::text")
        .get()
        .strip(),
        "shares_count": int(re.sub("[^0-9]", "", counter_share)),
        "comments_count": int(counter_coment),
        "summary": "".join(get_element.css(class_select["sumary"]).getall()),
        "sources": func_strip(
            get_element.css(class_select["sources"]).getall()
        ),
        "categories": func_strip(
            get_element.css(class_select["categories"]).getall()
        ),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
