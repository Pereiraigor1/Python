

# 1 Questão 

matriz = [];

for i in range (1,6,1):
    linha = [];
    for j in range (1,6,1):
        elemento = int(input(f"Digite o elemento {i} x {j} da matriz: "));
        linha.append(elemento)
        if (i==j):
            matriz.append(elemento);
    
print(f"A diagonal principal é: {matriz}");
    