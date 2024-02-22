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

def user_input(numero_grupo):
    try:
        n = int(input(f"Numero de valores para Grupo {numero_grupo}: "))
        valores = [float(input(f"Valor {i+1}: ")) for i in range(n)]
        return valores
    except ValueError:
        print("Verificar número inserido.")
        return user_input(numero_grupo)

def main():
    escolha = input("Já tem os valores do desvio padrão e média? (S/N): ").strip().lower()

    grupo1 = user_input(1)
    grupo2 = user_input(2)
    grupo3 = user_input(3)

    variancia_grupo1 = calcular_variancia(grupo1)
    desvio_padrao_grupo1 = calcular_desvio_padrao(variancia_grupo1)
    media_grupo1 = np.mean(grupo1)
    coeficiente_variacao_grupo1 = calcular_coeficiente_variacao(desvio_padrao=desvio_padrao_grupo1, media=media_grupo1)
    amplitude_grupo1 = calcular_amplitude(grupo1)

    variancia_grupo2 = calcular_variancia(grupo2)
    desvio_padrao_grupo2 = calcular_desvio_padrao(variancia_grupo2)
    media_grupo2 = np.mean(grupo2)
    coeficiente_variacao_grupo2 = calcular_coeficiente_variacao(desvio_padrao=desvio_padrao_grupo2, media=media_grupo2)
    amplitude_grupo2 = calcular_amplitude(grupo2)

    variancia_grupo3 = calcular_variancia(grupo3)
    desvio_padrao_grupo3 = calcular_desvio_padrao(variancia_grupo3)
    media_grupo3 = np.mean(grupo3)
    coeficiente_variacao_grupo3 = calcular_coeficiente_variacao(desvio_padrao=desvio_padrao_grupo3, media=media_grupo3)
    amplitude_grupo3 = calcular_amplitude(grupo3)

    anova_resultado = realizar_anova([grupo1, grupo2, grupo3])
    
    print(f"\nGrupo 1 - Variância: {variancia_grupo1}, Desvio Padrão: {desvio_padrao_grupo1}, Média: {media_grupo1}, Coeficiente de Variação: {coeficiente_variacao_grupo1:.2f}%, Amplitude: {amplitude_grupo1}")
    print(f"\nGrupo 2 - Variância: {variancia_grupo2}, Desvio Padrão: {desvio_padrao_grupo2}, Média: {media_grupo2}, Coeficiente de Variação: {coeficiente_variacao_grupo2:.2f}%, Amplitude: {amplitude_grupo2}")
    print(f"\nGrupo 3 - Variância: {variancia_grupo3}, Desvio Padrão: {desvio_padrao_grupo3}, Média: {media_grupo3}, Coeficiente de Variação: {coeficiente_variacao_grupo3:.2f}%, Amplitude: {amplitude_grupo3}")

    print("\nResultados da ANOVA:")
    print(f"Valor-p: {anova_resultado.pvalue}")
    print("Conclusão: Os grupos têm médias significativamente diferentes." if anova_resultado.pvalue < 0.05 else "Conclusão: Não há diferença significativa entre as médias dos grupos.")

    # Realizar comparações múltiplas e calcular intervalos de confiança usando Tukey HSD
    dados_combinados = np.concatenate([grupo1, grupo2, grupo3])
    rotulos_grupos = ['Grupo 1'] * len(grupo1) + ['Grupo 2'] * len(grupo2) + ['Grupo 3'] * len(grupo3)
    resultados_tukeyhsd = pairwise_tukeyhsd(dados_combinados, rotulos_grupos)

    print("\nIntervalo de Confiança para as Diferenças entre Grupos:")
    confianca = float(input("Nível de confiança (entre 0 e 1): "))
    intervalo_confianca = calcular_intervalo_confianca(resultados_tukeyhsd, confianca)
    for i, diff in enumerate(resultados_tukeyhsd.meandiffs):
        intervalo = intervalo_confianca[i]
        print(f"Diferença entre Grupo {resultados_tukeyhsd.groupsunique[i][0]} e Grupo {resultados_tukeyhsd.groupsunique[i][1]}: {diff:.2f} (Intervalo de Confiança {confianca * 100}%: {intervalo})")

if __name__ == "__main__":
    main()