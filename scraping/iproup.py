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
        noticias = soup.find('div', attrs={'class':'notahomebombasimple notahomebombasimpleblanca'})
        lista_noticias = noticias.find_all('a')
    except:
        None
    titulos = []
    url = []
    for noticia in lista_noticias:
        try:
            titulos.append(noticia.img['alt'])
            url.append('https://www.iproup.com'+noticia['href'])
        except:
            continue

    #Selecciona los elementos de la lista que realmente son noticias
    titulosA = []
    urlA = []
    for i in range(len(titulos)):
        if i % 2 == 0:
            try:
                titulosA.append(titulos[i])
                urlA.append(url[i])
            except:
                continue

    #Arma el diccionario con las noticias
    noticiasDic = {}
    for i in range(len(titulosA)):
        try:
            titulo = titulosA[i]
            url = urlA[i]
            diccio = {"noticia"+str(i):{"titulo":titulo,"url":url}}
            noticiasDic.update(diccio)
            i=i+1
        except:
            continue
    return(noticiasDic)

def iproup():
    return scrapper_soup('https://www.iproup.com/')
    
if __name__ == '__main__':
    iproup()