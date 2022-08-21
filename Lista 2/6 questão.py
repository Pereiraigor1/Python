soma = 0; 
homem = 0;  
maior = 0;   
mulher = 0;   
concu = 0;
somador = 0;
somatura = 0; 
media = 0;      
while True:
    matricula = int(input("Digite a matricula do funcionário: "))
    if matricula == 0:
        print("Matricula indeferida. Fim do programa !")
        break
    idade= int(input("Digite a idade do funcionário: "))
    sexo = str(input("Digite o sexo do funcionário [M ou F]: "))
    altura =float(input("Digite a altura do funcionário: "))
    concursado = str(input("Digite se o funcionário é concursado ou não [S ou N]: "))
    if (concursado == "S" or concursado =="s") and (sexo =="F" or sexo =="f"):
        soma = soma+1;
    print(f"(a) A quantidade de funcionárias concursadas é de: {soma}.");
    if sexo == "M" or sexo =="m":
        homem = homem +1;
    print(f"(b) Quantidade de funcionários homens: {homem}.")
    if maior < idade and (sexo == "M" or sexo =="m") and (concursado =="S" or concursado =="s"):
        maior = idade
    print(f"(c) A maior idade dos homens concursados : {maior} anos");
    if (sexo =="F" or sexo =="f") and idade > 30 and (concursado =="N" or concursado =="n"):
        mulher = mulher + 1;
    print(f"(d) Quantidade de mulheres com mais de 30 anos sem concurso: {mulher}.");
    if concursado == "S" or concursado =="s":
        concu = concu +1;
    print(f"(e) Quantidade de concursados: {concu}.");
    if idade < 40 and (sexo == "M" or sexo =="m"):
        somador = somador + 1;
        somatura = somatura + altura;
        media = (somatura/somador);
    print(f"(f) Média das alturas dos homens com menos de 40 anos : {media}");
    
