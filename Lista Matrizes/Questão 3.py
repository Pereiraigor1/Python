

# 3 Questão
def crie_matriz (n_linha,n_coluna):
    matriz =[];
    for i in range (n_linha) :
        linha = []
        for j in range (n_coluna):
            elemento = int(input(f"Digite o elemento {i+1}x{j+1} da matriz: "))
            linha.append(elemento)
            if (i>j):
                matriz.append(elemento);
    return matriz
a = crie_matriz(2,2);
b = sum(a);
arit = len(a);
mediaarit = (b/arit);

print(f"A média aritmética dos elementos abaixo da diagonal principal é de {mediaarit}");
