from parsel import Selector
import time
import requests

regex_number = r"\d+"
selector_url = "head > link[rel=canonical]::attr(href)"
selector_title = "h1.tec--article__header__title::text"
selector_timestamp = "div.tec--timestamp__item > time::attr(datetime)"
selector_writer = ".tec--author a.tec--author__info__link::attr(href)"
selector_writer_2 = ".tec--timestamp__item a::attr(href)"
selector_shares_count = ".tec--toolbar > .tec--toolbar__item::text"
selector_comments_count = ".tec--toolbar > "
selector_comments_count += ".tec--toolbar__item > button::attr(data-count)"
selector_sumary = "head > meta[name=description]::attr(content)"
selector_sources = ".z--mb-16 div a::text"
selector_categories = "#js-categories a::text"


def rm_spaces_in_string(string):
    if(string is not None):
        return string[1:-1]


def rm_spaces_in_array(array):
    result = []
    for string in array:
        result.append(string[1:-1])
    return result


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None

    if(response.status_code == 200):
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    notice = selector.css("div.tec--list")
    links = notice.css("figure a.tec--card__thumb__link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css("div.tec--list > a.tec--btn::attr(href)").get()
    return link


def scrape_writer(url_writer):
    html = fetch(url_writer)
    selector = Selector(text=html)
    writer_name = selector.css(".tec--author-header__title::text").get()
    return writer_name


def get_writer(html_content):
    selector = Selector(text=html_content)
    link_writer_type1 = selector.css(selector_writer).get()
    if(link_writer_type1):
        return scrape_writer(link_writer_type1)

    link_writer_type2 = selector.css(selector_writer_2).get()
    if(link_writer_type2):
        return scrape_writer(link_writer_type2)

    writer_name = selector.css(".tec--author__info p:first-child::text").get()
    if(writer_name):
        return writer_name


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css(selector_url).get()
    title = selector.css(selector_title).get()
    timestamp = selector.css(selector_timestamp).get()
    writer = get_writer(html_content)
    shares_count = int(
        selector.css(selector_shares_count).re_first(regex_number) or 0
    )
    comments_count = int(selector.css(selector_comments_count).get())
    summary = selector.css(selector_sumary).get()
    sources = rm_spaces_in_array(selector.css(selector_sources).getall())
    categories = rm_spaces_in_array(selector.css(selector_categories).getall())
    return{
        'url': url, 'title': title, 'timestamp': timestamp,
        'writer': writer, 'shares_count': (shares_count),
        'comments_count': comments_count, 'summary': summary,
        'sources': sources, 'categories': categories
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
