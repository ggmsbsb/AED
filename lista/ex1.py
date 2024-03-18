import numpy as np

#Import da planilha
from dolar import read_excel
df = read_excel()
#print(df)

def media_mensal(df):
    mes = df['Cotacao']
    media_mensal = mes.mean()
    return media_mensal

def media_movel_semanal(df):
    periodo = int(input("Qual o periodo a ser calculado?"))
    media_movel = []
    for i in range(len(df) - periodo + 1):
        media = sum(df['Cotacao'][i:i + periodo]) / periodo
        media_movel.append(media)
    return media_movel

def desvio_padrao(df):
    desvio_padrao = df['Cotacao'].std(ddof=1) #DDOF = Grau de liberdade
    return desvio_padrao

def menu():
    print("---------------------------------------")
    print("1. Média mensal")
    print("2. Média móvel semanal")
    print("3. Desvio padrão")
    print("4. Parar loop")
    print("---------------------------------------")


while True:
    menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        print("A média mensal é:", media_mensal(df))
    elif escolha == "2":
        print("A média móvel semanal é:", media_movel_semanal(df))
    elif escolha == "3":
        print("O desvio padrão é:", desvio_padrao(df))
    elif escolha == "4":
        print("Break")
        break
    else:
        print("Digitou o numero errado")