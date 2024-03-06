from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import math

def media_mensal(data):
    mes = dados['Cotacao']
    media_mensal = mes.mean()
    return media_mensal

def media_movel_semanal(dados):
   periodo = int(input("Valor do periodo: "))
   media_movel = []
   for i in range(len(dados) - periodo + 1):
    media = sum(dados['Cotacao'][i:i+periodo]) / periodo
    media_movel.append(media)
 return media_movel

arquivo = "dolar.xlsx"
dados = carregar_dados(arquivo)

opcao = int(input("Selecione uma opção:\n1) Valor médio mensal em agosto\n2) Média móvel semanal"))


if opcao == 1:
 media_mensal = media_mensal(dados)
 print("O valor médio mensal em agosto é:", round(media_mensal,2))
elif opcao == 2:
 media_movel = media_movel_semanal(dados)
 print("A média móvel semanal da cotação do dólar é dada pela lista abaixo:")
 display(media_movel)
else:
 print("Opção inválida.")
