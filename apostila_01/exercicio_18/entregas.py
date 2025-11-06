print("------------------------------")
print("     Entregas do Lobo Mau     ")
print("------------------------------")
print("")
print("A entrada é composta na primeira linha por 2 inteiros, 'T' e 'D' (1 <= 'T','D' <= 1000), representando o tamanho da estrada e a distância entre os pedágios. Na próxima linha serão fornecidos outros 2 inteiros, 'V' e 'P' (1 <= 'V', 'P' <= 100), representando o valor por km de estrada e o valor por cada pedágio.")
print("")
print("Na saída será apresentado o valor total pela travessia da floresta.")
print("------------------------------")
print("")

while True:
    T, D = input("Insira o tamanho da estrada e a distância entre os pedágios, respectivamente: ").split()
    print("")
    T = int(T)
    D = int(D)
    if 1 <= T <= 1000 and 1 <= D <= 1000:
        break
    else: 
        print("Insira um número válido!")
        print("")
        
while True:
    V, P = input("Insira o custo por km e o valor de cada pedágio, respectivamente: ").split()
    print("")
    V = int(V)
    P = int(P)
    if 1 <= V <= 100 and 1 <= P <= 100:
        break
    else: 
        print("Insira um número válido!")
        print("")
        
valDist = int(V * T)
pedPas = int((T/D))
valPed = int(pedPas * P) 
cust = valDist + valPed

print (cust)
