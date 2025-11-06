print("-------------------------------")
print("     Pirâmide de limonadas     ")
print("-------------------------------")
print("")
print("A entrada possui um número inteiro 'N' (1 <= N <= 9) representando o número de níveis da pilha piramidal.")
print("")
print("A saída consiste em 'N' linhas que representam os níveis da pirâmide em ordem crescente, ou seja, nível com mais taças por último. Cada nível começa com 'N – J' espaços em branco, seguidos pelos 'J * 2 - 1' algarismos que representam as taças daquela fileira.")
print("-------------------------------")
print("")

while True:
    N = int(input("Insira o número de níveis da pirâmide: "))
    print("")
    if 1 <= N <= 9:
        break
    else: 
        print("Insira um número válido!")
        print("")
        continue

        

loopNum = 1
fill = (N * 2 + 1)
while True:
    numb = (str(loopNum) * ((loopNum * 2) - 1)).center(fill)
    print (numb)
    if loopNum == N:
        break
    else: 
        loopNum+=1

# lines = res.splitlines()
# centerLines = [line.center(N * 2 - 1) for line in lines]
# correctLines = "\n".join(centerLines)

# print(correctLines)