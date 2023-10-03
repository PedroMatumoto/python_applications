#pegar um json com os dados da taxa selic e transformar em um csv

import json
import csv

# baixa a taxa selic
import urllib.request
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=json'
urllib.request.urlretrieve(url, 'selic.json')


with open('selic.json') as json_file:
    data = json.load(json_file)
    with open('selic.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for item in data:
            writer.writerow([item['data'], item['valor']])

# pegar ultima taxa
ultima_taxa = data[-1]['valor']
print(ultima_taxa)

# coloque seu telefone aqui
telefone = ''

# mande uma mensagem para +34 644 51 95 23 com 'I allow callmebot to send me messages' e pegue sua api key
apikey = ''

# fazer requisição http para a api do whatsapp
import requests
url = f'https://api.callmebot.com/whatsapp.php?phone={telefone}&text=Taxa+Selic+{ultima_taxa}&apikey={apikey}'
r = requests.post(url)
print(r.status_code)






