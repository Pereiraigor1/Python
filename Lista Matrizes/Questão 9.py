def vetor(matriz):
    somamatriz = 0
    numlinha = len(matriz)
    for i in range(0, 12, 1):
        for j in range(0, 12, 1):
            somamatriz += int(matriz[j][i])
        matrizt.append(somamatriz)
        somamatriz = 0
    print(matrizt)
matriz = []
matrizt = []
for i in range(0, 12, 1):
    linha = []
    for j in range(0, 12, 1):
        elemento = input("digite os elementos [%d] [%d] " % (i, j))
        linha.append(elemento)
    matriz.append(linha)
vetor(matriz)