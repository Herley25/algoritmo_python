from bs4 import BeautifulSoup
import concurrent.futures
import requests
### PRIMEIRA PÁGINA DE PODCASTS ###
url = 'https://www.montebravo.com.br/blog/podcasts/'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
webpage = requests.get(url, headers=headers).content
soup = BeautifulSoup(webpage, 'html.parser')
first_page_divs = soup.find("div", {"class": "grid-items"})
first_page_a = first_page_divs.find_all('a')
links_podcasts = []
count = 0
for a in first_page_a:
    count += 1
    if count % 2 != 0:
       single_link = a['href']
       links_podcasts.append(single_link)

### EXEMPLO DE PÁGINA DE PODCAST ABERTA ###
url = 'https://www.montebravo.com.br/blog/podcasts/fechamento-semanal/fechamento-semanal-29/'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
webpage = requests.get(url, headers=headers).content
soup = BeautifulSoup(webpage, 'html.parser')
iframe = soup.find("iframe")
podcast = iframe.get('src')
print(podcast)