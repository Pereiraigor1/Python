
#Questão 2 - VETOR - 10 INTEIROS IMPRIMIR O QUADRADO DE CADA NUMERO LIDO

Vet = [];
Quadrado =[];
for i in range (1,11):
    num = int(input("Digite 10 números inteiros : "));
    Vet.append(num);
    Quadrado.append(num**2);
print(f"Os números digitados foram : {Vet}\n");

print(f"O quadrado desses números são {Quadrado}");
