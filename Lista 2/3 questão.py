idades = [ ]
idade_qualquer = 1
while idade_qualquer:
     idade_qualquer = int(input("Digite uma idade ou 0 para terminar: "))
     if idade_qualquer:
     	idades.append(idade_qualquer)
print("Média de idade",sum(idades)/len(idades))
