

# Questão 3 - VETOR DE INTEIROS 

# (a) Retornar a ordem inversa

Vet = [];
VetPa =[];
VetIm =[];
n = True
somador = 0;
cont = 0;
media = 0;
maior = 0;
menor = 0;

while n :
    for i in range (1,6):
        num = int(input("Digite os números para o Vetor: "));
        Vet.append(num);
        a = num % 2;
        cont = cont + num;
        somador = somador +1;
        if (num > maior):
            maior = num;
            n_pos = Vet.index(maior);
        if (num < menor):
            menor = num;
            n_posi = Vet.index(menor) 
        if (a == 0):
            VetPa.append(num);
        elif (a !=0 ):
            VetIm.append(num);
    n = str(input("Você deseja continuar [S/N] ? "));
    if (n == "N"):
        break;
        
Vet.reverse();
print(f"Os vetores na ordem inversa é {Vet}");

# (b) Retorna somente os pares

print(f"Os vetores pares são {VetPa}");

# (c) Retornar somente os impares 

print(f"Os vetores impares são {VetIm}");

# (d) Calcular a média dos elementos
media = cont/num;

print(f"A soma dos elementos do vetor é {cont}\n");
print(f"A quantidade dos elementos: {somador}\n");
print(f"A média é de {media}");

# (e) Maior valor e sua posição no vetor

print(f"O maior valor é {maior} e sua posição é : {n_pos+1}º");

# (f) Menor valor e sua posição no vetor
print(f"O menor valor é {menor} e sua posição é : {n_posi+1}º");

# (g) Elementos repetidos 
   

 
        
        