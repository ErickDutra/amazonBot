import datetime
import csv
from requests_html import HTMLSession
import re

s = HTMLSession()
asins = []

#leitura da lista de asins no csv 
with open('asins.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        asins.append(row[0])

#busca do preço e titulo 
for asin in asins:
    r = s.get(f'https://www.amazon.com.br/dp/{asin}')
    r.html.render(sleep=1)
    try:
        price = r.html.find('#corePrice_feature_div')[0].text.replace('R$', ' #').replace(',', '.').strip()
    except:
        price = r.html.find('#apex_offerDisplay_desktop')[0].text.replace('R$', ' #').replace(',', '.').strip()
    title = r.html.find('#productTitle')[0].text.strip()
    asin = asin
    date = datetime.datetime.today()
    
    print(title,re.sub(r"(^\#.+\#)", ' ', price), date)