import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = 'http://web.chal.csaw.io:5010/'

cur_url = '/stuff'
values = []

while True:
    absolute_url = urljoin(BASE_URL, cur_url)
    # print(absolute_url)
    r = requests.get(absolute_url, cookies={'solChain': ' '.join(values)})
    values.append(cur_url[1:])
    soup = BeautifulSoup(r.text, 'html.parser')
    rel_links = [rel_link_tag.get('href') for rel_link_tag in soup.find_all('a', href=True)]
    if not rel_links:
        print(absolute_url, r.text)
        input()
    assert(len(set(rel_links)) == 1)
    for rel_link in rel_links:
        cur_url = rel_link