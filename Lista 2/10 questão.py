# -*- coding: utf-8 -*-



anterior = 0;
atual = 1;
proximo = 1;
elemento = 1;
a=1;
prox =1;
at=1;
ant=0;
n =int(input("Digite um número para mostrar sua série de Fibonacci :"))


print(f"Elemento: {elemento} Fibonacci: {anterior}");
for i in range (1,n):
    proximo = atual + anterior;
    anterior = atual;
    atual = proximo;
    elemento = elemento+1;
    print(f"Elemento: {elemento} Fibonacci: {anterior}");
while (n>1):
    teste = str(input("Digite S para executar novamente: ")) 
    if teste == "S" or teste =="s":
        n =int(input("Digite um número para mostrar sua série de Fibonacci :"))
        print(f"Elemento: {a} Fibonacci: {ant}");
        for i in range (1,n):
            prox = at + ant;
            ant = at;
            at = prox;
            a = a + 1;
            print(f"Elemento: {a} Fibonacci: {ant}");
    else:
        break;
        

        
    