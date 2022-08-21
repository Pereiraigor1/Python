

x = float(input("Digite um valor de x qualquer: "))
soma = 0;

for i in range (1,101):
    y = x+i;
    soma = y + soma;
print(f"O valor de y para o x = {x} é : {soma}");
