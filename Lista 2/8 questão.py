idade = 1;
quantidade = 0;
soma = 0;
media = 0;
for  i  in range (1,8):
        idade = int(input("Digite a idade: "));
        peso = float(input("Digite o peso: "));
        soma = idade + soma;
        media = soma/7;
        if peso > 90 :
            quantidade = quantidade + 1;
print(f"Quantidade de pessoas com mais de 90 quilos: {quantidade}");
print(f"Média das idades das setes pessoas : {media}");
