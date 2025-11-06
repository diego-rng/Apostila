print("--------------------------------")
print("     CONTINHA - EXERCÍCIO 2")
print("--------------------------------")
print("")
print("A entrada contém 6 valores inteiros: A, B, C, D, E, F (0 <= A, B, C, D, E, F <= 100.")
print("")
print("Imprima a mensagem “Eu sou FERA nas continhas e o resultado é ”, sem as aspas, em seguida o resultado da expressão, que é um número real com uma casa decimal de precisão")
print("--------------------------------")


print("A conta é ((A + B) * (C - D) * (E + F)) / 2")
A = input("Qual o valor de A? ")
intA = int(A)
B = input("Qual o valor de B? ")
intB = int(B)
C = input("Qual o valor de C? ")
intC = int(C)
D = input("Qual o valor de D? ")
intD = int(D)
E = input("Qual o valor de E? ")
intE = int(E)
F = input("Qual o valor de F? ")
intF = int(F)

result = ((intA + intB) * (intC - intD) * (intE + intF)) / 2

print("Eu sou FERA nas continhas e o resultado é ", result)