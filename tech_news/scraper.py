import requests
import time
from parsel import Selector
from tech_news.database import create_news


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


# Requisito 4
def generic_get_scrape(selector, css):
    result = selector.css(css).get()

    return result


def writer_scrape(selector, css1, css2):
    result1 = selector.css(css1).get()
    result2 = selector.css(css2).get()

    if result1 is None:
        return result2
    else:
        return result1


def number_scrape(selector, css):
    result = selector.css(css).get()

    if not result:
        return 0
    else:
        value = result.strip().split(" ")[0]
        return int(value)


def generic_getall_scrape(selector, css):
    results = selector.css(css).getall()

    a = []
    for result in results:
        a.append(result.strip())

    return a


def summary_scrape(selector, css):
    results = selector.css(css).getall()

    return results


def scrape_noticia(html_content):
    selector = Selector(html_content)

    data = {}

    data["url"] = generic_get_scrape(
        selector, "head > link[rel=canonical]::attr(href)"
    )
    data["title"] = generic_get_scrape(
        selector, "h1.tec--article__header__title ::text"
    )
    data["timestamp"] = generic_get_scrape(
        selector, ".tec--timestamp__item > time ::attr(datetime)"
    )
    data["writer"] = writer_scrape(
        selector,
        ".tec--author__info > p.z--m-none.z--truncate.z--font-bold *::text",
        ".tec--timestamp.tec--timestamp--lg > div > a ::text"
    ).strip()
    data["shares_count"] = number_scrape(
        selector, ".tec--toolbar > div:nth-child(1)::text"
    )
    data["comments_count"] = number_scrape(
        selector, "#js-comments-btn ::attr(data-count)"
    )
    data["summary"] = "".join(summary_scrape(
        selector, ".tec--article__body > p:nth-child(1) ::text"
    ))
    data["sources"] = generic_getall_scrape(
        selector, ".z--mb-16 > div > a ::text"
    )
    data["categories"] = generic_getall_scrape(
        selector, "#js-categories > a ::text"
    )

    return data


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url)
    url_list = scrape_novidades(html_content)

    data = []

    while len(url_list) < amount:
        next_page_url = scrape_next_page_link(html_content)
        next_page_html_content = fetch(next_page_url)
        next_page_url_list = scrape_novidades(next_page_html_content)
        url_list += next_page_url_list

    for i in range(amount):
        html_content = fetch(url_list[i])
        data += [scrape_noticia(html_content)]

    create_news(data)
    return data
