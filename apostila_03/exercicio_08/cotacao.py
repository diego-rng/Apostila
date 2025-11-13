print("-----------------")
print("     Cotação     ")
print("-----------------")
print("")
print("Ler a quantidade de dólares que o usuário tem e a cotação atual do dólar")
print("")
print("Converter a quantidade de dólares que o usuário tem para Reais")
print("-----------------")
print("")

quant, cot = input().split()

quant = float(quant); cot = float(cot)

quantD = quant * cot

print(f"{quantD:.2f}")