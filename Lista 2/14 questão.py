


a = int(input("Digite um número: "));
b = int(input("Digite um número menor que a: "))

mdc = a;
while (a % mdc != 0) or (b % mdc != 0):
    mdc = mdc -1 ;
print(f"O maior divisor comum é: {mdc}.");