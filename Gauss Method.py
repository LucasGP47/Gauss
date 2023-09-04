def metodoGauss(matriz1, result):
    n = len(matriz1)
    x = [0] * n

    for i in range(n):
        maximo = i
        for j in range(i + 1, n):
            if abs(matriz1[j][i]) > abs(matriz1[maximo][i]):
                maximo = j

        # Trocar as linhas
        matriz1[i], matriz1[maximo] = matriz1[maximo], matriz1[i]
        result[i], result[maximo] = result[maximo], result[i]

        for j in range(i + 1, n):
            factor = matriz1[j][i] / matriz1[i][i]
            for k in range(i, n):
                matriz1[j][k] -= factor * matriz1[i][k]
            result[j] -= factor * result[i]

    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += matriz1[i][j] * x[j]
        x[i] = (result[i] - soma) / matriz1[i][i]

    return x

def main():
    matriz = [[6, 1, -2], [-2, -3, 1], [-1, -2, 4]]
    resultado = [6, -5, -6.5]
    finalM = metodoGauss(matriz, resultado)

    print("Resultado Final:")
    for i, valor in enumerate(finalM):
        print(f'x[{i}] = {round(valor, 3)}')

if __name__ == "__main__":
    main()
