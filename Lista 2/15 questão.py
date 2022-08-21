
n = int(input("Digite um número para ver a aproximação inteira da raiz :"))
a = 1;
soma = n;
cont = 0;
while n > 1  and soma >= a:
    soma = soma - a;
    cont = cont +1;
    a = a + 2;

print(f"A resposta da raiz por uma aproximação inteira é de {cont}.")
    