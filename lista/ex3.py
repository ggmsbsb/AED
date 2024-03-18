import numpy as np

#Import da planilha
from indice import read_excel
df = read_excel()
#print(df)

def media_mensal(df):
    mes = df['Indice']
    media_mensal = mes.mean()
    return media_mensal

def desvio_padrao(df):
    desvio_padrao = df['Indice'].std(ddof=1) #DDOF = Grau de liberdade
    return desvio_padrao

print("O valor médio mensal é: ", round(media_mensal(df), 2))
print("O valor do desvio padrão amostral é: ", desvio_padrao(df))
if desvio_padrao(df) > 0.9: 
        print("Houve grande variação de precipitação pluviométrica!") 
else: 
        print("NÃO houve grande variação de precipitação pluviométrica!") 