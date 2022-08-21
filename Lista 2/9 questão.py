numero = int(input("Determine o valor de N: ") )
num=1;
resultado=1;
count=1;
E = 0;
while count <= numero:
    resultado *= count
    count += 1
    E+= (num/resultado);
print(E+1);   
