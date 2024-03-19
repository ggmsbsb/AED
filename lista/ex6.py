import pandas as pd
import json
import os

#Caminho JSON (tem q mudar dps)
caminho_arquivo = os.path.join(os.getcwd(), 'lista', 'ex6.json')
#Carregar json
with open(caminho_arquivo, 'r') as f:
    data = json.load(f)
legendasfabricantes = data['legendasfabricantes']
#print(legendasfabricantes) Só pra testar, depois remover


df = pd.DataFrame(legendasfabricantes, columns=['Legenda'])
#Qtd de cada legenda
qtd = df['Legenda'].value_counts().sort_index()
#Per 100tual
pcem = qtd / len(df) * 100

#Solicitação da legenda desejada
legenda_desejada = input("Legenda para consulta: ")

if legenda_desejada in qtd.index:
    qtd_legenda = qtd[legenda_desejada]
    pct_legenda = pcem[legenda_desejada]

#resultados 
    print(f"A legenda especificada possui as seguintes características:") 
    print(f"Legenda solicitada: {legenda_desejada}") 
    print(f"Quantidade de fabricantes com essa legenda: {qtd_legenda}") 
    print(f"Percentual em relação ao total: {pct_legenda:.2f}%") 
else: 
    print("Legenda não encontrada no DataFrame.")