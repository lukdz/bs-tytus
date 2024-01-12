import requests
from bs4 import BeautifulSoup

# id is uniq on the page
# soup.find_all('a')
# soup.find_all(id='text-3')
# soup.find_all(id='text-3')[0].get_text()
# soup.select('body h3 a')


domain = 'https://komiksy-dla-dzieci.prv.pl/'
start_path = '/?komiks=Tytus_Romek_i_A-Tomek'


page_url = domain + start_path
page = requests.get(page_url)
soup = BeautifulSoup(page.content, 'html.parser')

episode_list = []
for a in soup.find_all