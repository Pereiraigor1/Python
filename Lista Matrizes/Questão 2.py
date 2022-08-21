

# Questão 2 

matriz = [];
for i in range (1,6):
    linha = [];
    for j in range (1,6):
        elemento = int(input(f"Digite o elemento {i}x{j} da matriz: "));
        linha.append(elemento);
        if (i<j):
            matriz.append(elemento);
 
print(f"Os elementos que formam o triângulo superior são: {matriz}")