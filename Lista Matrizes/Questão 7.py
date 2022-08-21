def somamatriz(matrizA, matrizB):
    for i in range(0, 2):
        linha = []
        for j in range(0, 2):
            elemento = int(matrizA[i][j]) + int(matrizB[j][i])
            linha.append(elemento)
        matrizab.append(linha)
    print("a soma entre as duas matrizes é: ")
    for i in range(0, 2):
        for j in range(0,2):
            print(f"{matrizab[i][j]}")
matrizA = []
matrizB = []
matrizab = []
for i in range(0,2):
    linhaa = []
    for j in range(0,2):
        elemento = input(f"Digite os elementos da matriz A {i+1}x{j+1}: ")
        linhaa.append(elemento)
    matrizA.append(linhaa)
for i in range(0,2):
    linhab = []
    for j in range(0,2):
        elemento = input(f"Digite os elementos da matriz B {i+1}x{j+1}: ")
        linhab.append(elemento)
    matrizB.append(linhab)
    
somamatriz(matrizA, matrizB)