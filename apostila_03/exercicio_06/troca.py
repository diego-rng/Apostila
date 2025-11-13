print("---------------")
print("     Troca     ")
print("---------------")
print("")
print("Ler 2 variáveis")
print("")
print("Trocar o valor das duas e imprimir.")
print("------------------")
print("")

A, B = input().split()

temp = A

A = B
B = temp


print(f"{A}, {B}")

