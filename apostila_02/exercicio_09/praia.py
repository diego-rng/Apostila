print("--------------------------------")
print("     Oxi véi, cadê a praia?     ")
print("--------------------------------")
print("")
print("A entrada será dada por um mapa de dimensões 10x10. Cada uma das 10 linhas de entrada possuirá 10 caracteres separados por espaços, sendo cada caractere ou '*' para representar a água ou 't' para representar a terra.")
print("")
print("O programa deve imprimir o mapa corrigido, transformando em praia 'p', todo pedaço de terra 't' que estiver em contato direto com a água '*', verticalmente ou horizontalmente. O que estiver fora do mapa não deve ser considerado como água.")
print("--------------------------------")
print("")

map = []

# map = [["*",  "*", "*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "t", "t", "t", "t", "*", "*", "*", "*"], ["*",  "t", "t", "t", "t", "t", "t", "*", "*", "*"], ["*", "*", "*", "*", "t", "t", "t", "t", "t", "*"], ["*", "*", "*", "*", "*", "t", "t", "t", "t", "*"], ["*", "*", "*", "*", "*", "t", "t", "t", "*", "*"], ["*", "*", "*", "*", "t", "t", "t", "t", "*", "*"], ["t", "t", "t", "t", "t", "t", "t", "t", "t", "*"], ["t", "t", "t", "t", "t", "t", "t", "t", "*", "*"], ["t", "t", "t", "t", "t", "*", "*", "*", "*", "*"]]

def waterCheck(x, y):
    if x != 0:
        if map[x-1][y] == "*":
            return True
    if y != 0: 
        if map[x][y-1] == "*":
            return True 
    if y != 9:
        if map[x][y+1] == "*":
            return True
    if x != 9:
        if map[x+1][y] == "*":
            return True

for i in range(10):
    line = [str(i) for i in input().split()]
    map.append(line)

for j in range(10):
    for k in range(10):
        if map[j][k] == "t":
            if waterCheck(j,k) == True:
                map[j][k] = "p"
            else:
                continue

print("")
print("Praia: \n")

for j in range(10):
    for k in range(9):
        print(map[j][k], end= " ")
    print(map[j][k+1])
            