print("-----------------")
print("     Consumo     ")
print("-----------------")
print("")
print("Receber a distância percorrida e o total de combustível gasto")
print("")
print("Imprimir o consumo médio do veículo")
print("-----------------")
print("")

dist, tot = input().split()

cons = int(tot) / int(dist)

cons = int(cons)

print(f"O consumo médio do veículo é igual a {cons} L por km")
