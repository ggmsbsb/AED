import math

def media(numbers):
    """
    Retorna a média aritmética de uma lista de números.
    """
    return sum(numbers) / len(numbers)

def covariancia(x, y, x_media, y_media):
    """
    Retorna a covariância entre duas listas de números.
    """
    cov = 0
    n = len(x)
    for i in range(n):
        cov += (x[i] - x_media) * (y[i] - y_media)
    return cov / n

def variancia(x, media):
    """
    Retorna a variância de uma lista de números.
    """
    variancia = 0
    n = len(x)
    for i in range(n):
        variancia += (x[i] - media) ** 2
    return variancia / n

def pearson_r(x, y):
    """
    Calcula o coeficiente de correlação de Pearson (r) entre duas listas de números.
    """
    x_media = media(x)
    y_media = media(y)

    cov = covariancia(x, y, x_media, y_media)
    var_x = variancia(x, x_media)
    var_y = variancia(y, y_media)

    correlacao = cov / (math.sqrt(var_x) * math.sqrt(var_y))
    return correlacao

def main():
    """
    Função principal para obter entradas do usuário e calcular o coeficiente de correlação de Pearson.
    """
    while True:
        n = int(input("Quantos pares de números você deseja inserir? "))
        
        if n == 0:
            print("O número de pares de números não pode ser 0. Por favor, insira um valor válido.")
            continue
        elif n < 0:
            print("O número de pares de números deve ser um valor positivo. Por favor, insira um valor válido.")
            continue

        x_values = []
        y_values = []

        for i in range(n):
            x = float(input("Digite o valor de x{}: ".format(i + 1)))
            y = float(input("Digite o valor de y{}: ".format(i + 1)))
            x_values.append(x)
            y_values.append(y)

        correlacao = pearson_r(x_values, y_values)
        print("O coeficiente de correlação de Pearson entre os conjuntos de dados é:", correlacao)

        continuar = input("Denovo? ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()

#Comentarios gerados automaticamente por uma extenção.