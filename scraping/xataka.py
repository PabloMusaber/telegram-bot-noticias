import requests
from bs4 import BeautifulSoup

def scrapper_soup(url):
    """Obtiene el objeto soup."""
    try:
        noticias = requests.get(url, headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            })
        soup = BeautifulSoup(noticias.text, features="html.parser")
        noticias_principales = soup.find('div', attrs={'class':'section-hero-container'})
        noticias_secundarias = soup.find('div', attrs={'class':'section-recent-list js-s4'})
    except:
        None
    noticias = scrapper_noticias(noticias_principales)
    noticias_secundarias = scrapper_noticias(noticias_secundarias)

    for noticia in noticias_secundarias:
        noticias.append(noticia)
    
    return(noticias)

def scrapper_noticias(soup):
    """Extrae las noticias a partir del objeto soup."""  
    try:
        lista_noticias = soup.find_all('a')
    except:
        None
    noticias = []
    for noticia in lista_noticias:
        try:
            titulo = noticia.img['alt']
            if noticia['href'].startswith('https'):
                url = noticia['href']
            else:
                url = 'https://www.xataka.com'+noticia['href']
            noticias.append([titulo, url])
        except:
            continue
    return(noticias)

def xataka():
    return scrapper_soup('https://www.xataka.com/')
    
if __name__ == '__main__':
    xataka()
