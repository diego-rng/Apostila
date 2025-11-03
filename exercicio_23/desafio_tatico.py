print("------------------------")
print("     Desafio Tático     ")
print("------------------------")
print("")
print("ENTRADA:")
print("Um número inteiro 'P', representando o número de jogadores. Um número inteiro 'S', representando a quantidade de soldados que cada jogador possui. 'P' blocos de 'S' linhas cada, onde cada linha contém dois números inteiros separados por espaço. O primeiro número representa o valor de ataque e o segundo número representa o valor de defesa de um soldado. Os valores de ataque e defesa estão na faixa de 1 a 100.")
print("")
print("SAÍDA:")
print("'N' linhas com dois números inteiros separados por espaço, representando a soma dos valores de ataque e defesa para cada jogador.")
print("------------------------")
print("")

while True:
    P = int(input("Insira o número de Jogadores: "))
    print("")
    if 1 <= P <= 4:
        break
    else: 
        print("Tente novamente com uma quantidade válida de jogadores.")
        print("")
        continue

while True:
    S = int(input("Insira o número de Blocos cada jogador terá: "))
    print("")
    if 1 <= S <= 10:
        break
    else: 
        print("Tente novamente com uma quantidade válida de blocos.")
        print("")
        continue

numJ = 1
pl1Atk = []
pl1Def = []
pl2Atk = []
pl2Def = []
pl3Atk = []
pl3Def = []
pl4Atk = []
pl4Def = []
while True:
    print(f"{numJ}° Jogador")
    numB = 1
    while True:
        print(f"{numB}° Bloco")
        tempA, tempD = input("Insira o Ataque e defesa do Soldado em ordem: ").split()
        tempA = int(tempA)
        tempD = int(tempD)
        match numJ:
            case 1:
                pl1Atk.append(tempA)
                pl1Def.append(tempD)
            case 2:
                pl2Atk.append(tempA)
                pl2Def.append(tempD)
            case 3:
                pl3Atk.append(tempA)
                pl3Def.append(tempD)
            case 4:
                pl4Atk.append(tempA)
                pl4Def.append(tempD)
        numB = numB + 1
        if numB == (S + 1):
            break
    numJ = numJ + 1
    if numJ == (P + 1):
        break

print(f"{sum(pl1Atk)} {sum(pl1Def)}")
if P >= 2:
    print(f"{sum(pl2Atk)} {sum(pl2Def)}")

if P >= 3:
    print(f"{sum(pl3Atk)} {sum(pl3Def)}")

if P > 3:
    print(f"{sum(pl4Atk)} {sum(pl4Def)}")
