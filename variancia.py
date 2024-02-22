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
    return (desvio_padrao / media ) * 100

def user_input():
    try:
        n = int(input("Numero de valores: "))
        valores = [float(input(f"Valor {i+1}: ")) for i in range(n)]
        return valores
    except ValueError:
        print("Verificar número inserido.")
        return user_input()
    
def main():
    # Se você quiser inserir diretamente desvio padrão e média:
    desvio_padrao = float(input("Standard Deviation: "))
    media = float(input("Mean: "))
    coeficiente_variacao = calcular_coeficiente_variacao(desvio_padrao=desvio_padrao, media=media)

    print(f"\nStandard Deviation: {desvio_padrao}")
    print(f"Mean: {media}")
    print(f"Coefficient of Variation: {coeficiente_variacao}%")

    # Se você quiser inserir diretamente os valores e calcular tudo:
    # valores = get_user_input()
    # variancia = calcular_variancia(valores)
    # desvio_padrao = calcular_desvio_padrao(variancia)
    # media = sum(valores) / len(valores)
    # coeficiente_variacao = calcular_coeficiente_variacao(desvio_padrao=desvio_padrao, media=media)

    # print(f"\nVariance: {variancia}")
    # print(f"Standard Deviation: {desvio_padrao}")
    # print(f"Mean: {media}")
    # print(f"Coefficient of Variation: {coeficiente_variacao}%")


if __name__ == "__main__":
    main()
