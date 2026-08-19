import requests
import os

# URL da API para buscar as cotações atuais do Dólar, Euro e Bitcoin em relação ao Real
api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(api)
cotacao = resposta.json()

# Extrai o valor de compra ("bid") de cada moeda e converte para float
dolar = float(cotacao['USDBRL']['bid'])
euro = float(cotacao['EURBRL']['bid'])
btc = float(cotacao['BTCBRL']['bid'])

def cotacao_moedas():
    print(f"Dólar: R$ {dolar:.2f}")
    print(f"Euro: R$ {euro:.2f}")
    print(f"BTC: R$ {btc:.2f}")

def limpar_tela():
    # Compatibilidade para limpar o terminal em diferentes sistemas operacionais
    os.system("cls" if os.name == "nt" else "clear")

while True: # Loop principal do programa, que continua até o usuário escolher sair
    limpar_tela()

    print("""O que você deseja fazer?
    1 - Ver cotações 
    2 - Calcular conversão
    3 - Sair
    """)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        limpar_tela()
        cotacao_moedas()
        input()

    elif opcao == "2":
        limpar_tela()
        print("""Escolha a moeda que deseja converter:\n
        1 - Dólar\n
        2 - Euro\n
        3 - Bitcoin
        """)
        conv = input()

        if conv == "1":
            limpar_tela()
            valor = float(input("Digite o valor em reais: "))
            print(f"Valor em dólares: ${valor / dolar:.2f}")
            input()
            
        elif conv == "2":
            limpar_tela()
            valor = float(input("Digite o valor em reais: "))
            print(f"Valor em euros: €{valor / euro:.2f}")
            input()
            
        elif conv == "3":
            limpar_tela()
            valor = float(input("Digite o valor em reais: "))
            print(f"Valor em bitcoins: ₿{valor / btc:.8f}")
            input()

    elif opcao == "3":
        limpar_tela()
        # Encerra o loop principal e finaliza a execução do programa
        break