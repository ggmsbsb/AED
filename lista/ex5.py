import math 
import numpy as np 
import random 
 
 
numrespond=300 # PODE afetar o tamanho MÍNIMO da amostra; 
numquest=5 # NÃO afeta o tamanho MÍNIMO da amostra. 
E=0.2 
escalamax=5 # AFETA o tamanho MÍNIMO da amostra 
matriz = np.zeros((numrespond, numquest)) 
mediaq =np.empty(numquest) 
somaq =np.empty(numrespond) 
somaquad =np.empty(numrespond) 
var =np.empty(numquest) 
desvio =np.empty(numquest) 
arraysomaq =np.empty(numrespond) 
somarespostas = np.zeros(numrespond) 
somadasvar = 0 
varianciasomaresp = 0 
tamanhon = 0 
 
 
for j in range(numquest): 
  for i in range(numrespond): 
   numaleatorio=round(random.random()*escalamax,0) 
   correcao=0 
   if numaleatorio==0: 
    correcao=1 
   if numaleatorio==escalamax: 
    correcao=0 
   matriz[i][j]=numaleatorio+correcao 
 
for j in range(numquest): 
  somaq=0 
  somaquad=0 
 
  for linha in range(numrespond): 
   somaq=somaq+matriz[linha,j] 
 
  mediaq[j]=somaq/numrespond 
 
  for linha in range(numrespond): 
   somaquad=somaquad+(matriz[linha,j]-mediaq[j])**2 
 
  var[j]=somaquad/(numrespond-1) 
  desvio[j]=math.sqrt(var[j]) 
  somadasvar+=var[j] 
 
for linha in range(numrespond): 
  for j in range(numquest): 
   somarespostas[linha]=somarespostas[linha]+matriz[linha,j] 
 
 
varianciasomaresp=(np.std(somarespostas, ddof=0))**2 
mediadesvio=np.mean(desvio) 
tamanhon=(1.96*mediadesvio/E)**2 
 
 
 
print(matriz) 
print(round(tamanhon,0))