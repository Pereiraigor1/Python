N = 1;
while N:
    N = int(input("Digite um número: "));
    print("\n");
    print("A tabuada da soma é :\n");
    for i in range (1,11):
        soma = N +i;
        print(f" {N} + {i} = {soma}");
    print("\n");
    print("A tabuada da subtração é :\n");
    for i in range (1,11):
        a = N+i;
        subtracao = a-N;
        print(f" {a} - {N} = {subtracao}");
    print("\n");
    print("A tabuada da multiplicação é :\n");   
    for i in range (1,11):
        multiplicacao = N*i;
        print(f" {N} x {i} = {multiplicacao}");
    print("\n");
    print("A tabuada da divisão é :\n");  
    for i in range (1,11):
        b = N*i;
        divisao = int(b/N);
        print(f"{b} : {N} = {divisao}");
