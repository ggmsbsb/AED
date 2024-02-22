import math

def calcular_variancia(valores):
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia

def calcular_desvio_padrao(variancia):
    return math.sqrt(variancia)

def main():
    try:
        n = int(input("Quantos valores você gostaria de inserir? "))
        valores = []
        for i in range(n):
            valor = float(input(f"Informe o valor {i+1}: "))
            valores.append(valor)

        variancia = calcular_variancia(valores)
        desvio_padrao = calcular_desvio_padrao(variancia)

        print(f"\nVariância: {variancia}")
        print(f"Desvio Padrão: {desvio_padrao}")

    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    main()
