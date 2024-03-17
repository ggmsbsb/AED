import numpy as np

#Import da planilha
from excel import read_excel
df = read_excel()
#print(df)

def moda(df):
    moda = df['Cotacao'].mode()
    return moda

def mediana(df):
    mediana = df['Cotacao'].median()
    return mediana

def menu():
    print("---------------------------------------")
    print("1. Moda")
    print("2. Mediana")
    print("3. Parar loop")
    print("---------------------------------------")


while True:
    menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        print("A moda é:", moda(df))
    elif escolha == "2":
        print("A mediana é:", mediana(df))
    elif escolha == "3":
        print("Break")
        break
    else:
        print("Digitou o numero errado")
