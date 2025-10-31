print("--------------------")
print("     Cai pro x1     ")
print("--------------------")
print("")
print("A entrada consiste em 3 linhas contendo 2 inteiros 'L', 'P' (1 <= 'L', 'P' <= 100) em cada uma, sendo que L indica a pontuação de Lucas e P a pontuação de Pedro.")
print("")
print("A saída consiste em uma linha contendo a palavra “Empate”, caso os dois empatem, o nome “Pedro” caso Pedro tenha obtido uma pontuação de abates total maior que a de Lucas, ou o nome “Lucas”, caso Lucas tenha abates total maior que Pedro.")
print("--------------------")
print("")

while True: 
    L1, P1 = input("Round 1: \nInsira a pontuação de Lucas e Pedro, respectivamente: ").split()
    print("")
    L1 = int(L1)
    P1 = int(P1)
    if 0 <= L1 <= 100 and 0 <= P1 <= 100:
        break
    else:
        print("Insira um número válido!")
        print("")
        continue

while True: 
    L2, P2 = input("Round 2: \nInsira a pontuação de Lucas e Pedro, respectivamente: ").split()
    print("")
    L2 = int(L2)
    P2 = int(P2)
    if 0 <= L2 <= 100 and 0 <= P2 <= 100:
        break
    else:
        print("Insira um número válido!")
        print("")
        continue

while True: 
    L3, P3 = input("Round 3: \nInsira a pontuação de Lucas e Pedro, respectivamente: ").split()
    print("")
    L3 = int(L3)
    P3 = int(P3)
    if 0 <= L3 <= 100 and 0 <= P3 <= 100:
        break
    else:
        print("Insira um número válido!")
        print("")
        continue
    
L = int(L1 + L2 + L3)
P = int(P1 + P2 + P3)

if L == P:
    print("Empate")
elif L > P:
    print("Lucas")
elif L < P:
    print("Pedro")
    