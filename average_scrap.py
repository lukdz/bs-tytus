import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs
import os
import io
import logging
import traceback
import sys

def get_soup(page_url):
    page = requests.get(page_url)
    return BeautifulSoup(page.content, 'html.parser')

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

domain = 'https://komiksy-dla-dzieci.prv.pl/'
start_path = '/?komiks=Tytus_Romek_i_A-Tomek'
download_directory = "Tytus Romek i A-Tomek"
download_directory = "test"

soup = get_soup(domain + start_path)

episode_list = []
for a in soup.find_all('a', href=True):
    if 'epizod' in a['href']:
        episode_list.append(a['href'])
logging.info('Number of episodes %d', len(episode_list))

for episode in episode_list:
    directory = download_directory + '/' + parse_qs(episode)['epizod'][0]
    if not os.path.exists(directory):
        logging.info('Make directory "%s"', directory)
        os.makedirs(directory)

    logging.info('Downloading episode %s', episode)
    soup = get_soup(domain + episode)

    page_list = []
    for a in soup.find_all('a', href=True):
        if 'strona' in a['href']:
            page_list.append(a['href'])
    page_list

    for page in page_list:
        try:
            page_url = domain + page
            logging.info('Downloading comic page %s', page_url)
            soup = get_soup(page_url)

            picture_url = domain + soup.find('img')['src']
            
            logging.info('Downloading picture_ul %s', picture_url)

            page = requests.get(picture_url)
            path = directory + '/' + parse_qs(page_url)['strona'][0] + '.jpg'

            logging.info('Save path %s', path)

            with io.open(path, "wb") as f:
                f.write(page.content)
        except Exception as err:
            logging.error(traceback.format_exc())
