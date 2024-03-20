import numpy as np
import matplotlib.pyplot as graph

#Variaveis gráfico
preco = np.array([50, 20.5328, 8.8642, 4.023, 1.9194, 0.9627, 0.5076, 0.2814, 0.164,
                  0.1005, 0.0647, 0.0438, 0.0312, 0.0233, 0.0183, 0.0151, 0.0131, 0.012, 
                  0.0115, 0.0116, 0.0123, 0.0137])
frequencia =np.array([11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 21, 22, 23, 24, 24, 25, 25, 25, 25, 25, 25])


retorno=[]

#Preço[1:] é uma fatia de 1 até o ultimo elemento e "-1" é até o penultimo
retorno = np.log(preco[1:] / preco[:-1])

#graph print
#graph.hist(retorno, bins=20, edgecolor='black')
graph.bar(np.arange(len(retorno)), frequencia, width=0.5)
graph.xlabel('Retorno Diário')
graph.ylabel('Frequência')
graph.title("Distribuição de Frequência - Retorno Diário de um Ativo Financeiro")
graph.show()
