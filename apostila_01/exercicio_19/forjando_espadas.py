print("--------------------------")
print("     Forjando Espadas     ")
print("--------------------------")
print("")
print("A entrada consiste de três números inteiros: A,M,C, que representam respectivamente aquantidade de fragmentos de aço valiriano, pedaços de madeira e tiras de couro.")
print("")
print("Seu programa deverá imprimir a quantidade máxima de espadas que Gendry poderá forjar.")
print("--------------------------")
print("")

while True:
    A, M, C = input("Insira a quantidade de Aço Valiriano, Pedaços de Madeira e Tiras de Couro Gendry terá para trabalhar, respectivamente: ").split()
    print("")
    A = int(A)
    M = int(M)
    C = int(C)
    if 1 <= A <= 100 and 1 <= M <= 100 and 1 <= C <= 100:
        break
    else:
        print("Insira um número válido!")
        print("")
        continue
    
quantA = int(A / 2)
quantM = int(M / 3)
quantC = int(C / 5)

ammSwd = min(quantA, quantM, quantC)
print(ammSwd)