

nasc = int(input("Digite o número de crianças nascida em um certo período: "))
sexo = str;
crian = 0;
contmas = 0;
contmeses = 0;
while (sexo != "vazio" or sexo != "VAZIO"): 
    sexo = str(input("Digite o sexo da criança morta (M ou F ou vazio): "))
    if (sexo =="vazio" or sexo =="VAZIO"):
       break;
    mesesvida = int(input("Digite os meses de vida da criança: "));
    crian = crian +1;
    porce = (crian * 100)/nasc;
    if (sexo == "M" or sexo =="m"):
        contmas = contmas +1;
        porcemas = (contmas*100)/nasc;
    if (mesesvida <= 24):
        contmeses = contmeses +1;
        porcemese = (contmeses*100)/nasc;
print(f"A porcentagem de crianças mortas foi de {porce} %")
print(f"A porcentagem de crianças do sexo masculino mortas foi de {porcemas} %");
print(f"A porcentagem de crianças que viveram 24 meses ou menos foi de {porcemese} %");


