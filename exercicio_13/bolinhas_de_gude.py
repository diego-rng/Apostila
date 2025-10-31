print("--------------------------")
print("     Bolinhas de Gude     ")
print("--------------------------")
print("")
print("A entrada é composta por um número inteiro N (1 ≤ N ≤ 50), que representa a quantidade de familiares que irão presenteá-lo com bolinhas de gude e um inteiro Q (1 ≤ N ≤ 50), que representa a quantidade de bolinhas que o primeiro familiar dará de presente.")
print("")
print("A saída consiste em imprimir a quantidade total de bolinhas de gude que Yuri irá receber.")
print("--------------------------")
print("")

while True: 
    N = int(input("Insira quantos Familiares irão presentear Yuri: "))
    print("")
    if 1 <= N <= 50:
        break
    else: 
        print("Insira um número válido!")
        print("")
        continue
    
while True:
    Q = int(input("O primeiro familiar presenteou quantas bolinhas de gude para Yuri? "))
    print("")
    if 1 <= Q <= 50:
        break
    else: 
        print("Insira um número válido!")
        print("")
        continue
inQ = Q
num = 1
while True:
    Q = (Q * 2)
    if num == N:
        break
    else: 
        num = num + 1

print(Q - inQ)
        