import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.exceptions.HTTPError:  # source: shorturl.at/lsEX6
        return None
    except requests.exceptions.Timeout:
        return None

    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selection = Selector(html_content)
    urls = selection.css('h3.tec--card__title a::attr(href)').getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selection = Selector(html_content)
    # get() returns None when there are no matches
    url = selection.css('.tec--btn::attr(href)').get()
    return url


# Requisito 4
def get_url(selection):
    return selection.css('link[rel=canonical]::attr(href)').get()


def get_title(selection):
    return selection.css('#js-article-title::text').get()


def get_timestamp(selection):
    return selection.css('#js-article-date::attr(datetime)').get()


def get_writer(selection):
    try:
        writer = selection.css(
            ".z--font-bold"
        ).css("*::text").get().strip() or ''  # get helped by @gmcerqueira
        return writer.strip()
    except AttributeError:
        return None


def get_shares(selection):
    try:
        shares_count = (
            selection.css('.tec--toolbar__item::text').get().strip().split(' ')
        )
        return int(shares_count[0])
    except AttributeError:
        return 0


def get_comments(selection):
    comments_count = selection.css('#js-comments-btn::attr(data-count)').get()
    return int(comments_count)


def get_summary(selection):
    return ''.join(
        selection.css('.tec--article__body > p:nth-child(1) ::text').getall()
    )


def get_sources(selection):
    sources = selection.css('.z--mb-16 .tec--badge::text').getall()
    return [source.strip() for source in sources]


def get_categories(selection):
    categories = selection.css('#js-categories > a::text').getall()
    return [category.strip() for category in categories]


def scrape_noticia(html_content):
    selection = Selector(html_content)

    return {
        'url': get_url(selection),
        'title': get_title(selection),
        'timestamp': get_timestamp(selection),
        'writer': get_writer(selection),
        'shares_count': get_shares(selection),
        'comments_count': get_comments(selection),
        'summary': get_summary(selection),
        'sources': get_sources(selection),
        'categories': get_categories(selection),
    }


# Requisito 5
def get_tech_news(amount):
    URL = 'https://www.tecmundo.com.br/novidades'
    html = fetch(URL)
    scraped_news = scrape_novidades(html)
    tech_news = []

    while len(scraped_news) < amount:
        next_link = scrape_next_page_link(html)
        fetch_next_page = fetch(next_link)
        scraped_news.extend(scrape_novidades(fetch_next_page))

    for news in scraped_news[:amount]:
        html_news = fetch(news)
        tech_news.append(scrape_noticia(html_news))

    create_news(tech_news)
    return tech_news
