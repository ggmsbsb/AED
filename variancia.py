import math

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
    coeficiente_variacao = (desvio_padrao / media ) * 100

    if coeficiente_variacao < 1:
        coeficiente_variacao *= 100

    return coeficiente_variacao

def calcular_amplitude(valores):
    amplitude = max(valores) - min(valores)
    return amplitude

def user_input():
    try:
        n = int(input("Numero de valores: "))
        valores = [float(input(f"Valor {i+1}: ")) for i in range(n)]
        return valores
    except ValueError:
        print("Verificar número inserido.")
        return user_input()
    
def main():
    # Escolha entre inserir diretamente desvio padrão e média ou usar conjunto de dados
    escolha = input("Já tem os valores do desvio padrão e média? (S/N): ").strip().lower()

    if escolha == 's':
        desvio_padrao = float(input("Desvio Padrão: "))
        media = float(input("Média: "))
        coeficiente_variacao = calcular_coeficiente_variacao(desvio_padrao=desvio_padrao, media=media)

        print(f"Coeficiente de variação: {coeficiente_variacao:.2f}%")
    elif escolha == 'n':
        valores = user_input()
        variancia = calcular_variancia(valores)
        desvio_padrao = calcular_desvio_padrao(variancia)
        media = sum(valores) / len(valores)
        coeficiente_variacao = calcular_coeficiente_variacao(desvio_padrao=desvio_padrao, media=media)
        amplitude = calcular_amplitude(valores)

        print(f"\nVariance: {variancia}")
        print(f"Desvio Padrão: {desvio_padrao}")
        print(f"Média: {media}")
        print(f"Amplitude: {amplitude}")
        print(f"Coeficiente de variação: {coeficiente_variacao:.2f}%")
    else:
        print("Digitou errado")

if __name__ == "__main__":
    main()
