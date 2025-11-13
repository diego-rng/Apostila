print("-------------------")
print("     Operações     ")
print("-------------------")
print("")
print("Receber 2 números")
print("")
print("Imprimir a soma, subtração, multiplicação e divisão dos mesmos.")
print("-------------------")
print("")

N1, N2 = input().split()
N1 = int(N1); N2 = int(N2)

sum = int(N1 + N2)
sub = int(N1 - N2)
mul = int(N1 * N2)
div = int(N1 / N2)

print(f"Soma - {sum}\nSubtração - {sub}\nMultiplicação - {mul}\nDivisão - {div}")