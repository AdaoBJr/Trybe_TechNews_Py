from parsel import Selector


def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    if not isinstance(html_content, str):
        return list()
    else:
        selector = Selector(text=html_content)
        next_page_link = selector.css('.tec--list > a::attr(href)').get()
        return next_page_link


if __name__ == "__main__":
    with open("tests/assets/tecmundo_pages/novidades.html") as f:
        html_content = f.read()
    print(html_content)
    # print(scrape_novidades(html_content))
