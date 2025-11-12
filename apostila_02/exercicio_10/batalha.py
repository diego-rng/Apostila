print("--------------------------")
print("     Batalha de Yavin     ")
print("--------------------------")
print("")
print("A primeira linha da entrada possui um inteiro 'N' (3 ≤ N ≤ 100), indicando que a matriz que representa o espaço possui dimensões NxN, e um inteiro 'M'(1 ≤ M ≤ 1000), indicando o número de teleportes realizados por Luke. As próximas 'N' linhas possuem 'N' inteiros em cada uma, cujos valores podem ser 0 (se não existe nave naquele quadrante) ou 1 (se existe uma nave naquele quadrante). Nas próximas 'M' linhas serão dadas as coordenadas inteiras (L – linha C - coluna) de cada teleporte de Luke, um por linha. É garantido que Luke não aparecerá numa coordenada que possui uma nave, já que dois corpos não podem ocupar o mesmo lugar no espaço ao mesmo tempo. Os teleportes ocorrerão somente dentro do espaço dado.")
print("")
print("A saída consiste de apenas um inteiro que é o número de naves destruídas por Luke.")
print("--------------------------")
print("")

grid = []
teleListL = []
teleListC = []
locL = 0
locC = 0
count = 0

N, M = input().split()

N = int(N); M = int(M)

for i in range(N):
    line = [int(i) for i in input().split()] 
    grid.append(line)

for j in range(M):
    L, C = input().split()
    teleListL.append(int(L))
    teleListC.append(int(C))

for k in range(M):
    locL = teleListL.pop(0)
    locC = teleListC.pop(0)
    testL = int(locL - 1)
    currentTest = grid[testL][locC]
    for l in range(N):
        if testL < 0: break
        if grid[testL][locC] == 1:
            count += 1
            break
        else:
            testL -= 1

print("")
print(count)