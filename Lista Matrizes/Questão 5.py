

# Questão 5 

matriz = [];
for i in range (1,6):
    linha = [];
    for j in range (1,4):
        elemento = int(input(f"Digite o elemento {i}x{j} da matriz: "))
        linha.append(elemento);
    matriz.append(linha);
a=int(input("Digite uma linha para ser apresentada[1..5]: "));
    
if (a == 1):
    print(matriz[0]);
elif (a == 2):
    print(matriz[1]);
elif (a==3):
    print(matriz[2]);
elif (a==4):
    print(matriz[3]);
elif (a==5):
    print(matriz[4]);
else:
    print("Linha inexistente! \n")
        