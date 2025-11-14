print("-----------------")
print("     Fábrica     ")
print("-----------------")
print("")
print("Ler o custo de fábrica de um carro")
print("")
print("Imprimir o custo do consumidor, com a percentagem do distribuidor e os impostos.")
print("-----------------")
print("")

cust = float(input())

res = float(cust + (cust * .45))

cons = float(res + (res * .28))

print(f"\nR${cons:.2f}")