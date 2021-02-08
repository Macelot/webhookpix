#esta é a aplicação cliente
import requests
from auth import token
import json

access_token = token()

chave = 'colocar sua chave'

url = "https://api-pix.gerencianet.com.br/v2/webhook/"+chave

payload={
    "webhookUrl": "https://www. colocar seu end point/"
    }

headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=json.dumps(payload), cert='./prod123456.pem')

print('PUT',response.text.encode('utf8'))

#response = requests.request("DELETE", url, headers=headers, data='', cert='./prod123456.pem')

#print('DELETE',response.text.encode('utf8'))

response = requests.request("GET", url, headers=headers, data='', cert='./prod278612.pem')

print('GET',response.text.encode('utf8'))

#url = "https://api-pix.gerencianet.com.br/v2/webhook/"+chave+"?inicio=2021-02-01T08:00:00Z&fim=2021-02-04T23:59:59Z"

#response = requests.request("GET", url, headers=headers, data='', cert='./prod123456.pem')

#print('GET período',response.text.encode('utf8'))
