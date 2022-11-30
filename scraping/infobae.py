from scraping.secciones_infobae import *
import requests
from bs4 import BeautifulSoup

def scrapper_soup(url):
    """Obtiene la página y la convierte en un objeto soup."""  
    try:
        noticias = requests.get(url, headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            })
        soup = BeautifulSoup(noticias.text, features="html.parser")
    except:
        None
    return(scrapper_noticias(soup))
    
def scrapper_noticias(soup):
    """Extrae las noticias a partir del objeto soup."""  
    try:  
        noticias = soup.find('div', attrs={'class':'nd-feed-list-wrapper'})
        lista_noticias = noticias.find_all('a')
    except:
        None
    i=0
    noticiasDic = {}
    for noticia in lista_noticias:
        try:
            titulo = noticia.h2.text
            url = 'https://www.infobae.com'+noticia['href']
            diccio = {"noticia"+str(i):{"titulo":titulo,"url":url}}
            noticiasDic.update(diccio)
            i=i+1
        except:
            continue
    return(noticiasDic)

    
def infobae(seccion):
    return scrapper_soup(seccionesDic[str(seccion)]['url'])

if __name__ == '__main__':
    infobae(0)
    

