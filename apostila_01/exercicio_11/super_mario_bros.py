print("--------------------------")
print("     Super Mario Bros     ")
print("--------------------------")
print("")
print("Considerando as três áreas secretas, a entrada consiste nos itens que você conseguiu encontrar, sendo três números inteiros 'SC' (0 <= SC <= 30), 'MM' (0 <= MM <= 6) e 'CK' (0 <= CK <= 3) representando, respectivamente, Star Coins, Mega Mushrooms e Carapaças Koopa Azul.")
print("")
print("A saída consiste em uma única linha. Caso você não tenha encontrado todas as Star Coins, deve ser impresso a quantidade de itens ainda por serem descobertos no mundo atual, sendo impresso primeiro a quantidade de Star Coins, seguido pela quantidade de Mega Mushrooms e por fim, a quantidade de Carapaças Koopa Azul. Caso você tenha conseguido encontrar todas as Star Coins você deve imprimir a mensagem 'PROXIMO MUNDO'.")
print("--------------------------")
print("")

WORLD_SC = 30
WORLD_MM = 6 
WORLD_CK = 3

while True:
    SC, MM, CK = input("Insira os itens que conseguiu encontrar até agora, Star Coins, Mega Mushrooms e Carapaças Koopa Azuis em respectiva ordem: ").split()
    print("")
    SC = int(SC)
    MM = int(MM)
    CK = int(CK)
    check = 0 <= SC <= 30, 0 <= MM <= 6, 0 <= CK <= 3
    
    if check:
        break
    else:
        print("Insira números válidos.")
        print("")
        continue


if SC == 30:
    print("PROXIMO MUNDO")
else:
    print(f"{WORLD_SC - SC} {WORLD_MM - MM} {WORLD_CK - CK}")