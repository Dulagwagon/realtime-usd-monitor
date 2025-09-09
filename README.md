## Cotação do Dólar em Tempo Real 🤑

![Python](https://img.shields.io/badge/Python-3.13-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Dulagwagon/cotacao_moedas)
![Issues](https://img.shields.io/github/issues/Dulagwagon/cotacao_moedas)

Script Python que consulta a cotação do dólar via API, registra historicamente em CSV e permite atualização automática em intervalos definidos pelo usuário.

---

## Funcionalidades

- Consulta API HG Brasil para cotação do dólar
- Grava dados em CSV com timestamp
- Atualização automática com intervalo configurável
- Tratamento de erros de API e input do usuário

---

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Dulagwagon/cotacao_moedas.git

2. Navegue para a pasta do projeto:
    ```bash
    cd cotacao_moedas

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

4. Crie uma chave de acesso na HG Brasil
    ```bash
    https://console.hgbrasil.com/users/sign_in

5. Copie o conteúdo do arquivo env.example para .env
    ```bash
    cp env.example .env   # Linux / Mac
    copy env.example .env # Windows

    e depois adicione sua chave, deixando o arquivo dessa forma:

    # Copie este arquivo para .env e insira sua chave da API HG Brasil
    API_KEY=sua_chave_aqui


6. Execute o Script:
    ```bash
   python cotacao.py

## Exemplo de saída
    Linha registrada: ('2025-09-09 12:00:00', 5.41)

<img width="397" height="114" alt="image" src="https://github.com/user-attachments/assets/d68367f7-96ad-4b55-aa1f-f1173aea1e7e" />

   

## Possíveis Melhorias
+ Dashboard web para visualizar histórico;
+ Alertas de variação do dólar;
+ Deploy em nuvem para monitoramento contínuo;
+ Inserção de outros ativos para monitoramento.

---

## Autor
Eduardo Pereira - [github.com/Dulagwagon](https://github.com/Dulagwagon/)



