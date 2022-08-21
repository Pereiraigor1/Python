# Questão 6

def pede_matriz ():
    m = int(input("Digite o número de linhas da matriz A: "))
    n = int(input("Digite o número de colunas da matriz A: "))
    A = le_matriz(m,n)
    
    p = int(input("Digite o numero de colunas da matriz B: "))
    B = le_matriz (n,p)
    
    C = []
    for i in range (m):
        C.append([]);
        for j in range(p):
            soma = 0
            for k in range (n):
                soma += A [i][k] * B [k][j]
            C[i].append(soma)
            
    print("O resultado da multiplicação de A por B é: ")
    imprime_matriz(C)
def le_matriz(m,n):
    print(f"Digite os elementos da matriz de tamanho {m}x{n}: ")
    matriz = []
    for i in range (m):
        matriz.append([])
        for j in range (n):
            elemento = int(input(f"Elemento {i+1}x{j+1}: "))
            matriz[i].append(elemento);
    return matriz

def imprime_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end = " ")
        print()

pede_matriz()