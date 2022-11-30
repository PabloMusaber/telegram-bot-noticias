import requests
from bs4 import BeautifulSoup

def scrapper_noticias(url):
    """Obtiene el objeto soup."""
    try:
        noticias = requests.get(url, headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            })
        soup = BeautifulSoup(noticias.text, features="html.parser")
    except:
        None
    principalesDic = principales(soup)
    secundariasDic = secundarias(soup)
    noticiasDiccio = principalesDic.copy()
    noticiasDiccio.update(secundariasDic)
    return(noticiasDiccio)

def principales(soup):
    """Busca las noticias principales de Xataka a partir del objeto soup."""
    try:
        principales = soup.find('div', attrs={'class':'section-hero-container'})
        lista_principales = principales.find_all('a')
    except:
        None
    i=0
    principalesDic = {}
    for noticia in lista_principales:
        try:
            titulo = noticia.img['alt']
            url = 'https://www.xataka.com'+noticia['href']
            diccio = {"noticia"+str(i):{"titulo":titulo,"url":url}}
            principalesDic.update(diccio)
            i=i+1
        except:
            continue
    return(principalesDic)

def secundarias(soup):
    """Busca las noticias secundarias de Xataka a partir del objeto soup."""
    try:
        secundarias = soup.find('div', attrs={'class':'section-recent-list js-s4'})
        lista_secundarias = secundarias.find_all('a')
    except:
        None
    i=0
    secundariasDic = {}
    for noticia in lista_secundarias:
        try:
            titulo = noticia.img['alt']
            url = noticia['href']
            diccio = {"noticiaB"+str(i):{"titulo":titulo,"url":url}}
            secundariasDic.update(diccio)
            i=i+1
        except:
            continue
    return(secundariasDic)

def xataka():
    return scrapper_noticias('https://www.xataka.com/')
    
if __name__ == '__main__':
    xataka()
