import requests
import csv
import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env

API_KEY = os.getenv("API_KEY")

def get_cotacao_dolar():
    try:
        url = "https://api.hgbrasil.com/finance?format=json&key={API_KEY}"
        r = requests.get(url)
        r.raise_for_status()
        dados = r.json()
        valor_dolar = dados['results']['currencies']['USD']['buy']
        return valor_dolar
    except Exception as e:
        print(f'Aconteceu um erro inesperado. Tente novamente mais tarde.')
        return None

def gerar_linha():
    valor_dolar = get_cotacao_dolar()
    if valor_dolar is None:
        print(f'Erro na obtenção de dados, tente novamente mais tarde.')
        return None
    else:
        agora = datetime.now()
        data_hora = agora.strftime("%Y-%m-%d %H:%M:%S")
        linha = (data_hora, valor_dolar)
        return linha
   
def registrar_dados_csv(linha):
    arquivo_existe = os.path.exists("historico.csv")
    with open('historico.csv', 'a', newline='', encoding='utf-8-sig') as arquivo:
        escritor_csv = csv.writer(arquivo)
        if not arquivo_existe:
            escritor_csv.writerow(['Data e Hora', 'Valor do Dólar'])
        escritor_csv.writerow(linha)

while True:
    try:
        intervalo = input('Indique o intervalo de atualização desejado (minutos):')
        intervalo_resposta = float(intervalo)
        if intervalo_resposta <= 0:
            print(f'Quantidade inválida. Digite um número maior que zero.')
            continue
        break
    except ValueError:
        print('Por favor, digite um número válido.')

while True:
    #Gerar a linha com data e cotação
    linha = gerar_linha()
    if linha is not None:
        #Registrar a linha no CSV
        registrar_dados_csv(linha)
        print(f'Linha registrada: {linha}')
    time.sleep(intervalo_resposta*60)
