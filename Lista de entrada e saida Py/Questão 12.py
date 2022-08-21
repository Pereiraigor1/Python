
Salmin = float(input("Digite o valor do salário-mínimo: "))
Quant = float(input("Digite a quantidade de Quilowatts gasto na residência: "))
Cada = (Salmin/7)/100;
Valp = Cada*Quant
Desconto =(Valp*10)/100
print(f"O valor de cada quilowatt em reais é de {Cada}")
print(f"O valor em reais a ser pago é de {Valp}")
print(f"O valor novo a ser pago com desconto de 10% é de {Desconto}")