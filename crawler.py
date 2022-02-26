import requests
from bs4 import BeautifulSoup as bs

# cover-basic-tile tile-content
r = requests.get('https://www.capital.sp.gov.br/')
soup = bs(r.text, 'lxml')

res = soup.find_all('div', { 'class' : 'cover-basic-tile tile-content' } )

for link in res:
    print(f" Link: {link.a.get('href')} ")
    
    









