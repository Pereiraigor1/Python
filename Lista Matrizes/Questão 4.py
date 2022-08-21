

#Questão 4

matriz = [];
soma = 0;
for i in range (1,4):
    linha = [];
    for j in range (1,5):
        elemento = int(input(f"Digite o elemento {i}x{j} da matriz: "));
        linha.append(elemento);
        soma = soma +elemento;
    matriz.append(linha);
        
print(f"A matriz é : {matriz}\n");
print(f"A soma desses elementos é igual a {soma}");