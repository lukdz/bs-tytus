import requests
from bs4 import BeautifulSoup

def get_episodes(page_url):
    page = requests.get(page_url)

    soup = BeautifulSoup(page.content, 'html.parser')

    main = soup.find(id='main')
    episodes = main.find("div", {"class": "episodes"})
    episodes_list = episodes.find_all('a', href=True)

    url_autors = []
    for a in episodes_list:
        url_autors.append(page_url.split('?')[0]+a['href'])
    
    return url_autors

def get_pages(page_url):
    page = requests.get(page_url)

    soup = BeautifulSoup(page.content, 'html.parser')

    main = soup.find(id='main')
    episodes = main.find("div", {"class": "pages center"})
    episodes_list = episodes.find_all('a', href=True)

    url_autors = []
    for a in episodes_list:
        url_autors.append(page_url+a['href'])

    print(soup.find_all("img"))
    
    return url_autors


episodes_list = get_episodes('https://komiksy-dla-dzieci.prv.pl/?komiks=Tytus_Romek_i_A-Tomek')
for link in episodes_list:
    print(link)
    pages_list = get_pages(link)
    print(pages_list)
    exit