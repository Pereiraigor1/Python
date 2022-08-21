import math
N = 1;
while N:
    N = int(input("Digite um número: "));
    if N % 2 == 0 :
        soma = math.sqrt(N);
    else:
        soma = math.pow(N,2);
    print(soma);
