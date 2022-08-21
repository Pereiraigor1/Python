
vendedor = str(input("Digite o nome do vendedor: "))
fixo = int(input("O seu salário fixo : "))
tvendas = int(input("O total de vendas realizadas pelo vendedor: "))
percentual = int(input("Percentual ganhado em cima da venda :"))
saltotal = fixo + tvendas*percentual;
print(f" O nome do vendedor é {vendedor} e seu salário é de {saltotal}")