from math import sqrt

N1= float(input("Digite a primeira nota do Aluno: "))
N2 = float(input("Digite a segunda nota do Aluno: "))
N3 = float(input("Digite a terceira nota do Aluno: "))
N4 = float(input("Digite a quarta nota do Aluno: "))
Media =sqrt(pow(N1,2)+pow(N2,2)+pow(N3,2)+pow(N4,2))
print(f"A média quadrática é {Media}")