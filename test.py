from parsel import Selector


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    links = selector.css('head link').xpath('@href').getall()
    matching = [s for s in links if "https://www.tecmundo.com.br" in s]
    url = matching[1]
    return url


if __name__ == "__main__":
    path = (
        "tests/"
        "assets/"
        "tecmundo_pages/"
        "minha-serie|"
        "215168-10-viloes-animes-extremamente-inteligentes.htm."
        "html"
    )
    with open(path) as f:
        html_content = f.read()
    print(scrape_noticia(html_content))
