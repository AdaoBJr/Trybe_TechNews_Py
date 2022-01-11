response = requests.get('http://https://www.tecmundo.com.br/novidades')
selector = Selector(text=response)
links = selector.css(
    '.tec--card .tec--card__info h3 a::attr(src)').getall()
print(links)