import math
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def calcular_variancia(valores):
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia

def calcular_desvio_padrao(variancia):
    return math.sqrt(variancia)

def calcular_coeficiente_variacao(desvio_padrao=None, media=None, valores=None):
    if valores is not None:
        media = sum(valores) / len(valores)
        desvio_padrao = calcular_desvio_padrao(calcular_variancia(valores))

    if media == 0:
        return 0
    coeficiente_variacao = (desvio_padrao / media) * 100

    if coeficiente_variacao < 1:
        coeficiente_variacao *= 100

    return coeficiente_variacao

def calcular_amplitude(valores):
    amplitude = max(valores) - min(valores)
    return amplitude

def realizar_anova(grupos):
    return f_oneway(*grupos)

def calcular_intervalo_confianca(resultados_tukeyhsd, confianca=0.95):
    intervalos_confianca = []

    for i, diff in enumerate(resultados_tukeyhsd.meandiffs):
        intervalo = resultados_tukeyhsd.confint[i]
        intervalos_confianca.append(intervalo)

    return intervalos_confianca


def user_input(grupo):
    try:
        n = int(input(f"Numero de valores para o Grupo {grupo}: "))
        valores = [float(input(f"Valor {i+1}: ")) for i in range(n)]
        return valores
    except ValueError:
        print("Verificar número inserido.")
        return user_input(grupo)

def main():
    escolha = input("Escolha uma opção:\n1 - Calcular variância, desvio padrão, média e amplitude.\n2 - Calcular o coeficiente de variação.\n3 - ANOVA.\n").strip()

    if escolha == '1':
        numero_grupos = int(input("Número de grupos: "))
        for i in range(numero_grupos):
            grupo = user_input()
            variancia = calcular_variancia(grupo)
            desvio_padrao = calcular_desvio_padrao(variancia)
            media = np.mean(grupo)
            coeficiente_variacao = calcular_coeficiente_variacao(desvio_padrao=desvio_padrao, media=media)
            amplitude = calcular_amplitude(grupo)

            print(f"\nGrupo {i + 1} - Variância: {variancia}, Desvio Padrão: {desvio_padrao}, Média: {media}, Coeficiente de Variação: {coeficiente_variacao:.2f}%, Amplitude: {amplitude}")

    elif escolha == '2':
        desvio_padrao = float(input("Desvio Padrão: "))
        media = float(input("Média: "))
        coeficiente_variacao = calcular_coeficiente_variacao(desvio_padrao=desvio_padrao, media=media)

        print(f"Coeficiente de variação: {coeficiente_variacao:.2f}%")

    elif escolha == '3':
        numero_grupos = int(input("Número de grupos (mínimo 2): "))
        grupos = [user_input(i + 1) for i in range(numero_grupos)]  # Adicionado um índice para mostrar o número do grupo
        anova_resultado = realizar_anova(grupos)

        print("\nResultados da ANOVA:")
        print(f"Valor-p: {anova_resultado.pvalue}")
        print(f"Valor F: {anova_resultado.statistic}")

        print("Conclusão: Os grupos têm médias significativamente diferentes." if anova_resultado.pvalue < 0.05 else "Conclusão: Não há diferença significativa entre as médias dos grupos.")

        # Realizar comparações múltiplas e calcular intervalos de confiança usando Tukey HSD
        dados_combinados = np.concatenate(grupos)
        rotulos_grupos = [f'Grupo {i+1}' for i in range(numero_grupos) for _ in grupos[i]]
        resultados_tukeyhsd = pairwise_tukeyhsd(dados_combinados, rotulos_grupos)

        print("\nIntervalo de Confiança para as Diferenças entre Grupos:")
        confianca = float(input("Nível de confiança (entre 0 e 1): "))
        intervalo_confianca = calcular_intervalo_confianca(resultados_tukeyhsd, confianca)
        for i, diff in enumerate(resultados_tukeyhsd.meandiffs):
            intervalo = intervalo_confianca[i]
            grupo1 = resultados_tukeyhsd.groupsunique[i][0]
            grupo2 = resultados_tukeyhsd.groupsunique[i][1]
            #Arrumar isso aq
            print(f"Diferença entre Grupo {grupo1} e Grupo {grupo2}: {diff:.2f} (Intervalo de Confiança: {intervalo})")

    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
