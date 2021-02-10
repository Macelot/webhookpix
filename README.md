# webhookpix 
Este projeto é para exemplificar o funcionamento de um webhook Pix 
Para colocar em funcionamento é necessário um servidor Linux para rodar o server2.py  
A configuração do server precisa seguir os seguintes comandos: 

Criar DNS: 
Criar DNS free em https://www.cloudns.net/ 
teste-pix.cloudns.cl 
Criar dois registros A: 
A.teste-pix.cloudns.cl outro www.teste-pix.cloudns.cl apontando para o IP de seu Linux 

Criação certificados: 
sudo apt install snapd 
sudo snap install core 
sudo snap install --classic certbot 
sudo ln -s /snap/bin/certbot /usr/bin/certbot 
--
sudo apt-get install python-certbot-apache 
sudo certbot --apache
[preencher com seus dados]

Copiar o arquivo https://pix.gerencianet.com.br/webhooks/chain-pix-prod.crt
curl -O https://pix.gerencianet.com.br/webhooks/chain-pix-prod.crt
cp chain-pix-prod.crt /etc/ssl/certs/

Instalação Python:
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
curl -O https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz
tar -xf Python-3.8.2.tar.xz
cd Python-3.8.2
./configure --enable-optimizations
make -j 4
sudo make altinstall
python3.8 --version

apt-get install python-flask
sudo apt install python3-pip
python3 -m pip list
python3 -m pip install flask 

mkdir my_app
cd my_app
nano server2.py ->colocar código deste exemplo
python3 server2.py 

Para testar podes executar localmente o programa configurar_webhook.py. Note que o programa configurar_webhook deve ser preenchido com seu webhookUrl correto definido na configuração anterior.
O programa vai informar a PSP Gerencianet seu webhookUrl.
Agora basta criar uma cobrança, fazer o pagamento e conferir o arquivo data.txt, que vai receber a confirmação do pagamento.

No arquivo server2.py existem algumas linhas comentadas para que você faça seus testes. Bons códigos!
