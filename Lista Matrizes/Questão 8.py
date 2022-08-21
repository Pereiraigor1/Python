def somamatriz(matrizA):
    for i in range(0, 6, 1):
        linha = []
        for j in range(0, 6, 1):
                elemento = int(matrizA[j][i]) * int(matrizA[i][i])
                linha.append(elemento)
        matrizaxb.append(linha)
    print("a soma entre as duas matrizes é= ")
    for i in range(0, 6, 1):
        for j in range(0, 6, 1):
            print(f' {matrizaxb[i][j]} ', end='')
        print()
matrizA = []
matrizaxb = []
for i in range(0, 6, 1):
    linhaa = []
    for j in range(0, 6, 1):
        elemento = input("digite os elementos da matriz A [%d] [%d] " % (i, j))
        linhaa.append(elemento)
    matrizA.append(linhaa)
somamatriz(matrizA)