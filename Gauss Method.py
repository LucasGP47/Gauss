def metodoGauss(matriz1, result, max_iter=100):
    n = len(matriz1)
    x = [0] * n
    total = 0

    for i in range(n):
        maximo = i
        for j in range(i + 1, n):
            if abs(matriz1[j][i]) > abs(matriz1[maximo][i]):
                maximo = j
                max_iter -= 1
             

        # Trocar as linhas
        matriz1[i], matriz1[maximo] = matriz1[maximo], matriz1[i]
        result[i], result[maximo] = result[maximo], result[i]

        for j in range(i + 1, n):
            factor = matriz1[j][i] / matriz1[i][i]
            
            for k in range(i, n):
                matriz1[j][k] -= factor * matriz1[i][k]
                
                
            result[j] -= factor * result[i]
            

    if max_iter < 100:
        print("O método não convergiu após {} iterações.".format(max_iter))
        print("Matriz parcial:")
        for row in matriz1:
            print(row)
        return x

    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += matriz1[i][j] * x[j]
        x[i] = (result[i] - soma) / matriz1[i][i]

    return x

def main():
    matriz = [[7, 3, 2],
             [3, 14, 4],
             [2, 1, 9]]
   
    resultado = [2,
                 4,
                -10]
   
    finalM = metodoGauss(matriz, resultado)

    print("Resultado Final:")
    for i, valor in enumerate(finalM):
        print(f'x[{i}] = {round(valor, 3)}')

if __name__ == "__main__":
    main()
