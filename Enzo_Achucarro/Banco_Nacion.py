import bs4 as bs
import requests
from tqdm import tqdm

resp = requests.get('https://www.bna.com.ar/Personas') 
resp = resp.text                      
soup = bs.BeautifulSoup(resp, 'lxml')  
table = soup.find('table', {'class': 'table cotizacion'})

titulo = ['      ','compra','venta']
a1 = []
b1 = []
c1 = []


for row in tqdm(table.findAll('tr')[1:]):
    a = row.findAll('td')[0].text
    b = row.findAll('td')[1].text
    c = row.findAll('td')[2].text


    a1.append(a)
    b1.append(b)
    c1.append(c)
    

print(titulo[0], end='    ')
for i in a1:
    print(i, end='       ')
print('\n')   
print(titulo[1], end='     ')
for i in b1:
    print(i, end='      ')
print('\n')
print(titulo[2], end='      ')
for i in c1:
    print(i, end='      ')
