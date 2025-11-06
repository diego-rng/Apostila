print("----------------------------")
print("     Escolha do Campeão     ")
print("----------------------------")
print("")
print("A entrada consiste na primeira linha de um número inteiro 'N' (1 < N < 100) que representa o número de campeões favoritos de Lucas. Nas próximas 'N' linhas será fornecido em cada uma, um número inteiro 'P' (0 <= P <= 10000) que representa o nível de poder de cada um dos 'N' campeões.")
print("")
print("A saída deverá conter apenas o nível de poder do campeão mais forte.")
print("----------------------------")

while True:
    N = int(input("Lucas tem quantos campeões favoritos? "))
    print("")
    if 1 < N < 100: 
        break
    else: 
        print("Insira um número válido.")
        print("")

champs = []
num = int(0)
while True: 
    tempC = int(input(f"Qual o nível de poder do {num + 1}° campeão? "))
    print("")
    champs.append(tempC)
    num = int(num + 1)
    if num == N:
        break
    else: 
        continue

strChamp = max(champs)

print(f"O campeão mais forte tem poder equivalente a {strChamp}.")

    