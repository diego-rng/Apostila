print("---------------------------------")
print("     Fortalecimento de clima     ")
print("---------------------------------")
print("")
print("A primeira linha da entrada contém um valor 'N' (1 <= N <= 1000) que representa o número de pokémon que serão fortalecidos pelo clima. Já cada uma das próximas 'N' linhas contém o valor 'P' (1 <= P <= 1000) de pontos de dano do ataque principal de um pokémon e o seu valor 'M' (0 <= M <= 1000) de acréscimo.")
print("")
print("A saída é composta de 'N' linhas, cada uma representando o valor final de pontos de dano de cada linha da entrada.")
print("---------------------------------")
print("")

while True:
    N = int(input("Insira o número de pokémon que serão fortalecidos pelo clima: "))
    print("")
    if 1 <= N <= 1000:
        break
    else:
        print("Insira um valor correto!")
        print("")

listP = []
listM = []
for i in range(0, N):
    while True:
        P, M = input(f"Insira os valor de dano original e o aumento de clima do pokémon número {i + 1}: ").split()
        print("")
        P = int(P)
        M = int(M)
        if 1 <= P <= 1000 and 1 <= P <= 1000:
            break
        else: 
            print("Insira um valor correto!")
            print("")
            continue
    listP.append(P)
    listM.append(M)
    
for i in range(0, N):
    resP = listP.pop(0)
    resM = listM.pop(0)
    res = resP + resM
    print(res)


