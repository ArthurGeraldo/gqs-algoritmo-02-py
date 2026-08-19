# GQS Algoritmo 02 - Python

![Python Version](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Esse é um conversor de moedas em tempo real via terminal, desenvolvido em Python. Ele consome dados de uma API pública para buscar as cotações atuais e oferece um menu interativo com as seguintes funcionalidades:
- Consulta de Cotações Atuais
- Conversão de Valores

### Detalhamento do Código

O código foi estruturado utilizando os seguintes comandos e conceitos em Python:

* **`import requests` e `os`:** Bibliotecas utilizadas para consumir a API externa e interagir com o sistema operacional (limpeza de tela), respectivamente.
* **`requests.get()` e `.json()`:** Responsáveis por fazer a requisição HTTP e converter os dados recebidos para o formato de dicionário.
* **`float()`:** Converte os dados de texto recebidos da API e os valores digitados pelo usuário em números decimais para a realização dos cálculos matemáticos.
* **`def`:** Utilizado para criar funções personalizadas e reaproveitáveis, como `cotacao_moedas()` e `limpar_tela()`.
* **`while True`:** Estrutura de repetição que cria um loop infinito, mantendo o menu principal ativo até que o usuário decida sair.
* **`print()` e `input()`:** Comandos de entrada e saída de dados. O `input()` captura as escolhas e os valores digitados pelo usuário, enquanto o `print()` exibe os resultados na tela.
* **`if`, `elif` e `break`:** Estruturas condicionais que direcionam o programa com base na escolha do menu, além do comando `break` para interromper o loop e encerrar a aplicação.

## Pré-requisitos

Certifique-se de ter o **Python 3.12** (ou superior) instalado em sua máquina. Você pode verificar a versão instalada executando o seguinte comando no seu terminal:

```
  python --version
  # ou
  python3 --version
```

## Como Executar

Siga o passo a passo abaixo pelo terminal ou linha de comando para rodar o programa:

**1. Entre na pasta do projeto:**
```
  cd gqs-algoritmo-02-py
```
**2. Execute o arquivo principal usando o Python:**
```
  python main.py
```

## Exemplo de Saída

Abaixo está a simulação exata do que o console exibe durante a execução do programa. Neste exemplo real de uso, o usuário escolhe a opção de conversão, seleciona a moeda Dólar, converte R$ 100,00 e, em seguida, encerra o programa:

```
O que você deseja fazer?
    1 - Ver cotações 
    2 - Calcular conversão
    3 - Sair
    
Escolha uma opção: 2

Escolha a moeda que deseja converter:

    1 - Dólar

    2 - Euro

    3 - Bitcoin
        
1

Digite o valor em reais: 100
Valor em dólares: $19.45
```

## Sobre o Autor
**Nome:** Arthur Geraldo Santos Silva  
**RA:** 4251924719  
**Disciplina:** Garantia da Qualidade de Software  
**Professor:** Daniel Henrique Matos de Paiva
