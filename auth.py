#este código é utilizado pela aplicação cliente
import requests
import base64

credentials = {
    "client_id": "Client_Id_",
    "client_secret": "Client_Secret_",
}

certificado = './prod123456.pem' # A variável certificado é o diretório em que seu certificado em formato .pem deve ser inserido

auth = base64.b64encode(
    (f"{credentials['client_id']}:{credentials['client_secret']}"
     ).encode()).decode()


def token():
    #url = "https://api-pix-h.gerencianet.com.br/oauth/token" #Para ambiente de Desenvolvimento
    url = "https://api-pix.gerencianet.com.br/oauth/token" #Para ambiente de Produção

    payload="{\r\n    \"grant_type\": \"client_credentials\"\r\n}"
    headers = {
        'Authorization': f"Basic {auth}",
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, cert=certificado)

    result = response.json().get('access_token')
    
#    print(result)
 
    return result