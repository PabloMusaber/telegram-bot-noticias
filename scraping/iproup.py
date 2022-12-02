import requests
from bs4 import BeautifulSoup

def scrapper_soup(url):
    """Obtiene el objeto soup"""
    try:
        noticias = requests.get(url, headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            })
        soup = BeautifulSoup(noticias.text, features="html.parser")
    except:
        None
    return(scrapper_noticias(soup))

def scrapper_noticias(soup):
    """Busca las noticias de iProUP a partir del objeto soup."""
    try:
        noticias_soup = soup.find('div', attrs={'class':'notahomebombasimple notahomebombasimpleblanca'})
        lista_noticias = noticias_soup.find_all('a')
    except:
        None
    noticias = []
    for noticia in lista_noticias:
        try:
            titulo = noticia.img['alt']
            url = 'https://www.iproup.com'+noticia['href']
            if [titulo, url] not in noticias:
                noticias.append([titulo, url])
        except:
            continue
    return(noticias)

def iproup():
    return scrapper_soup('https://www.iproup.com/')
    
if __name__ == '__main__':
    iproup()