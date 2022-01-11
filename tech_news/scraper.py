import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        res.raise_for_status()
        return res.text
    except requests.HTTPError:
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)

    result = selector.css(".tec--list--lg h3 > a ::attr(href)").getall()

    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    result = selector.css(".tec--list--lg > a ::attr(href)").get()

    return result


def generic_get_scrape(selector, string):
    result = selector.css(string).get()

    print(">>>>>>>>>>>", type(result), result)

    if result:
        return result.strip()
    else:
        return '0'


def generic_getall_scrape(selector, string):
    results = selector.css(string).getall()

    a = []
    for result in results:
        a.append(result.strip())

    return a


def summary_scrape(selector, string):
    results = selector.css(string).getall()

    return results


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    data = {}

    shares_count = generic_get_scrape(
        selector, ".tec--toolbar > div:nth-child(1) ::text"
    ).split(' ')[0]
    print("<<<<<<<<<<<<<", shares_count)

    data["shares_count"] = int(generic_get_scrape(
        selector, ".tec--toolbar > div:nth-child(1) ::text"
    ).split(' ')[0])
    data["url"] = generic_get_scrape(
        selector, "head > link[rel=canonical]::attr(href)"
    )
    data["title"] = generic_get_scrape(
        selector, "h1.tec--article__header__title ::text"
    )
    data["timestamp"] = generic_get_scrape(
        selector, ".tec--timestamp__item > time ::attr(datetime)"
    )
    data["comments_count"] = int(generic_get_scrape(
        selector, "#js-comments-btn ::attr(data-count)"
    ))
    data["writer"] = generic_get_scrape(
        selector, ".tec--author__info > p > a ::text"
    ).strip()
    data["sources"] = generic_getall_scrape(
        selector, ".z--mb-16.z--px-16 > div > a ::text"
    )
    data["categories"] = generic_getall_scrape(
        selector, "#js-categories > a ::text"
    )
    data["summary"] = "".join(summary_scrape(
        selector, ".tec--article__body > p:nth-child(1) ::text"
    ))

    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
