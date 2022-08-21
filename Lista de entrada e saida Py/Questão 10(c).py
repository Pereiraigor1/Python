
from math import sqrt

N1 = float(input("Digite a primeira nota do Aluno: "))
N2 = float(input("Digite a segunda nota do Aluno: "))
N3 = float(input("Digite a terceira nota do Aluno: "))
N4 = float(input("Digite a quarta nota do Aluno: "))
Media = sqrt(sqrt(N1*N2*N3*N4))
print(f"A média Harmônica é {Media}")