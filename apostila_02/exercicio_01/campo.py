print("---------------------------")
print("     Campo de Abóboras     ")
print("---------------------------")
print("")
print("Seu programa receberá primeiramente um inteiro 'N' (1 ≤ 'N' ≤ 100), representando o tamanho da plantação de abóboras, que é um campo de proporção NxN (N linhas horizontais por N linhas verticais). A seguir serão dadas 'N' linhas, onde em cada uma serão dados 'N' inteiros 'P' (1 <= P <= 100), que representam o peso de cada abóbora no campo. Há uma abóbora em cada posição do campo NxN. Por fim, a última linha da entrada contêm as linhas 'X' e 'Y' (0 <= X,Y < N) que Harry e Ron irão coletar, respectivamente. Cuidado que a linha de Ron na verdade se trata de uma coluna na matriz da plantação.")
print("")
print("Imprima o peso total da colheita de Harry e a seguir, na linha de baixo, imprima o peso total da colheita de Ron, como nos exemplos da Apostila.")
print("---------------------------")
print("")

# Basic number validation, you will see this in the start of basically every single one of my exercises here.
while True:
    N = int(input("Insira o tamanho da plantação: "))
    print("")
    if 1 <= 100 <= 100:
        break
    else:
        print("Insira um número válido!")
        print("")

pumpkinList = []
for i in range(N):
    tempList = input(f"Insira o peso das abóboras na linha {i + 1}: ").split()
    print("")
    pumpkinList.append(tempList)

X, Y = input("Insira a linha que Harry e Ron devem colher primeiro: ").split()

X = int(X)
Y = int(Y)
har = []
ron = []
ronTemp1 = []
ronTemp2 = []
harTemp1 = []
harTemp2 = []
for i in range(N):
    for j in range(N):
        # if Y == j:
        #     if j == X:
        #         tempRon = pumpkinList[i].pop(j)
        #         ron += int(tempRon)
        #         pumpkinList[i].insert(j, 0)
        #     elif j < X:
        #         tempRon = pumpkinList[i].pop(j)
        #         ron += int(tempRon)
        #         pumpkinList[i].insert(j, 0)
        #     else:
        #         continue
        # if X == i:
        #     tempHar = pumpkinList[i].pop(j) 
        #     har += int(tempHar)
        #     pumpkinList[i].insert(j, 0)
        if Y == j:
            ronTemp1.append(i)
            ronTemp2.append(j)
        if X == i:
            harTemp1.append(i)
            harTemp2.append(j)
    
for i in range(N):
    pos1 = ronTemp1.pop(0)
    pos2 = ronTemp2.pop(0)
    ron.append(pumpkinList[pos1].pop(pos2))
    pumpkinList[pos1].insert(pos2, 0)
    pos1 = harTemp1.pop(0)
    pos2 = harTemp2.pop(0)
    har.append(pumpkinList[pos1].pop(pos2))
    pumpkinList[pos1].insert(pos2, 0)

resH = 0
resR = 0
for i in range(N):
    temp = har.pop()
    resH += int(temp)
    tempo = ron.pop()
    resR += int(tempo)

    
print(f"Harry {resH} \nRon {resR}")


# for i in range(0, N):
#     while True:
#         P = input(f"Insira o peso das abóboras na linha {i+1}: ").split(" ", N)
#         print("")
#         if len(P) != N:
#             print("Insira uma quantidade válida!")
#             print("")
#             continue
#         else: 
#             break
#     pumpkinList.append(P)
#     i += 1

# print (pumpkinList)

# while True:
#     X, Y = input("Insira as linhas que Harry e Ron devem colher primeiro: ").split()
#     print("")
#     X = int(X)
#     Y = int(Y)
#     if 0 <= X < N and 0 <= Y < N:
#         break
#     else: 
#         print("Insira uma linha válida! (0 a N)")
#         print("")

# har = []
# ron = []