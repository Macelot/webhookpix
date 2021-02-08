#esta é a aplicação do server
from flask import Flask, jsonify, request
import ssl
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/", methods=["PUT"])
def hello_put():
    response = {"status": 200}
    return jsonify(response)

@app.route("/", methods=["POST"])
def hello_post():
    response = {"status": 200}
    imprimir()
    return jsonify(response)

def imprimir():
    imprime = print(request.json)
    data = request.json
    with open('data.txt', 'a') as outfile:
        outfile.write("\n")
        json.dump(data, outfile)
    return jsonify(imprime)

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations('/etc/ssl/certs/chain-pix-prod.crt')
    context.load_cert_chain(
        '/etc/letsencrypt/live/www.teste-pix.cloudns.cl/fullchain.pem',
        '/etc/letsencrypt/live/www.teste-pix.cloudns.cl/privkey.pem')
    app.run(ssl_context=context, host='colocar seu ip', port=80)