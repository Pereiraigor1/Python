
n = int(input("Informe o valor de n: "))
vazio = 0
v = str(" ")
s = str("*")

for i in range (-n, n, 2):
    asterisco = n - 1 - i 
    vazio = vazio + 1   
    print(vazio * v, asterisco * s )