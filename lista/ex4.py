import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from indice import read_excel

# Lê os dados do Excel
df = read_excel()

# Conversos de datas
df['Data'] = pd.to_datetime(df['Data'])

#Config gráfico (tem q mudar depois)
plt.figure(figsize=(10, 6))
plt.plot(df['Data'], df['Indice'], marker='o', linestyle='-')

# Formatação das datas E.X
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.gcf().autofmt_xdate()

#Nomenclatura gráfico
plt.title('Índice Pluviométrico ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Índice Pluviométrico')
plt.grid(True)
#Printar gráfico
plt.show()
