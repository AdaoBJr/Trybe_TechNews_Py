import requests
import time
from parsel import Selector

from tech_news.database import create_news

# Requisito 1


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = selector.xpath(
        "/html/body/div/main/div/div/div/div/div/article/div/h3/a/@href"
    ).getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.xpath(
        "/html/body/div/main/div/div/div/div/a/@href"
    ).get()
    return result


# Requisito 4
def verify_share(numberShare):
    if numberShare == ' ':
        return 0
    number = numberShare

    if number is not None:
        print(number)
        return int(number.strip().split(" ")[0])

    return 0


def check_writer(author):
    selector = Selector(author)
    css_paths = [
        ".tec--timestamp__item.z--font-bold ::text",
        ".tec--author__info__link ::text",
        "div > p.z--m-none.z--truncate.z--font-bold::text",
    ]
    for path in css_paths:
        writer = selector.css(path).get()
        if writer is not None:
            return writer.strip()
    return


def check_source(source):
    selector = Selector(source)
    css_paths = [
        "#js-main > div.z--container > article > div.tec--article__body-grid >"
        "div.z--mb-16.z--px-16 > div > a ::text",
        "#js-main > div > article > div.tec--article__body-grid >"
        " div.z--mb-16 > div > a::text",
    ]
    for path in css_paths:
        get = selector.css(path).getall()
        if len(get) > 0:
            return [element.strip() for element in get]
    return []


def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head > link[rel=canonical] ::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()
    dateTime = selector.css("#js-article-date ::attr(datetime)").get()
    writer = check_writer(html_content)
    shares_count = verify_share(
        selector.css("#js-author-bar > nav > div:nth-child(1) ::text").get()
    )
    comments_count = verify_share(
        selector.css("#js-comments-btn ::attr(data-count)").get()
    )
    summary = "".join(
        selector.css(
            ".tec--article__body > p:nth-child(1) *::text"
        ).getall()
    )
    sources = check_source(html_content)
    categories = [
        element.strip()
        for element in selector.css("#js-categories a::text").getall()
    ]
    data = {}
    data["url"] = url
    data["title"] = title
    data["timestamp"] = dateTime
    data["writer"] = writer
    data["shares_count"] = shares_count
    data["comments_count"] = int(comments_count)
    data["summary"] = summary
    data["sources"] = sources
    data["categories"] = categories
    return data


# Requisito 5
def get_tech_news(amount):
    base_url = "https://www.tecmundo.com.br/novidades"
    fetch_url = fetch(base_url)
    novidades_urls = scrape_novidades(fetch_url)

    info_lista = []
    while len(novidades_urls) < amount:
        next_page = scrape_next_page_link(fetch_url)
        fetch_url = fetch(next_page)
        novidades_urls.extend(scrape_novidades(fetch_url))

    for url in novidades_urls[:amount]:
        fetch_url = fetch(url)
        info_lista.append(scrape_noticia(fetch_url))

    create_news(info_lista)
    return info_lista



