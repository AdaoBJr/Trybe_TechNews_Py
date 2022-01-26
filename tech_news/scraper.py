from parsel import Selector
import time
import requests
import re


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f"\n{response.status_code}")
            return response.text
        else:
            print("else")
            return None
    except requests.Timeout:
        response = requests.Timeout
        print(response)
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    parentElement = selector.css("div.tec--list")
    links = parentElement.css("a.tec--card__thumb__link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page_link = selector.css("div.tec--list a.tec--btn::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css(
        "div.tec--timestamp__item time::attr(datetime)"
    ).get()
    author = selector.css(".z--font-bold *::text").get().strip() or ""
    print("author", author)
    shares_count_selector = (
        selector.css(".tec--toolbar .tec--toolbar__item::text").get() or "0"
    )
    if shares_count_selector:
        int_share_count = (
            int(re.findall(r"\d+", shares_count_selector)[0]) or 0
        )
    comments_count = int(
        selector.css(".tec--toolbar__item button::attr(data-count)").get() or 0
    )
    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    )
    sources = [
        source.strip() for source in selector.css(".z--mb-16 a::text").getall()
    ]
    categories = [
        category.strip()
        for category in selector.css("#js-categories a::text").getall()
    ]
    print(categories)
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": author.strip(),
        "shares_count": int_share_count or 0,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
