import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs
import os
import io

def get_soup(page_url):
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')

domain = 'https://komiksy-dla-dzieci.prv.pl/'
start_path = '/?komiks=Tytus_Romek_i_A-Tomek'

soup = get_soup(domain + start_path)

episode_list = []
for a in soup.find_all('a', href=True):
    if 'epizod' in a['href']:
        episode_list.append(a['href'])
print('Number of episodes ', len(episode_list))

for episode in episode_list:
    directory = parse_qs(episode)['epizod'][0]
    if not os.path.exists(directory):
        print('Make directory ', directory)
        os.makedirs(directory)

    print('Downloading episode ', episode)
    soup = get_soup(domain + episode)

    page_list = []
    for a in soup.find_all('a', href=True):
        if 'strona' in a['href']:
            page_list.append(a['href'])
    page_list

    for page in page_list:
        page_url = domain + page
        print('Downloading comic page ', page_url)
        soup = get_soup(page_url)

        picture_path = soup.find('img')['src']

        page = requests.get(domain + picture_path)
        path = directory + '/' + os.path.basename(picture_path)
        print('Save path ', path)
        with io.open(path, "wb") as f:
            f.write(page.content)
