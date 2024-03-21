import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json

# Carregar dados do arquivo JSON
with open('D:/CDMI/AED/lista/ex7.json', 'r') as f:
    data_dict = json.load(f)

# Converter o dicionário em DataFrame
df = pd.DataFrame(data_dict)

# Renomear a coluna 'Cotacao (Venda - R$)' para 'Cotacao_Venda_R'
df.rename(columns={'Cotacao (Venda - R$)': 'Cotacao_Venda_R', 'Variação(%)': 'Variacao'}, inplace=True)

# Adicionar um índice numérico ao DataFrame
df['Index'] = range(1, len(df) + 1)

# Criar figura e eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar gráfico de superfície
surface = ax.plot_trisurf(df['Index'], df['Cotacao_Venda_R'], df['Variacao'], cmap="Blues")

# Adicionar rótulos dos eixos
ax.set_xlabel('Índice')
ax.set_ylabel('Cotação (Venda - R$)')
ax.set_zlabel('Variação(%)')

# Adicionar título
plt.title('Variação da Cotação do Dólar (Agosto/2022)')

# Mostrar o gráfico
plt.show()
