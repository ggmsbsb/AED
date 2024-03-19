import pandas as pd
import json
import os

# Construa o caminho completo para o arquivo JSON
caminho_arquivo = os.path.join(os.getcwd(), 'lista', 'ex6.json')

# Carrega os dados do arquivo JSON
with open(caminho_arquivo, 'r') as f:
    data = json.load(f)

# Acessa a lista de legendasfabricantes
legendasfabricantes = data['legendasfabricantes']

# Agora você pode usar a lista como desejar
print(legendasfabricantes)
