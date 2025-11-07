print("----------------------")
print("     Torre Xadrez     ")
print("----------------------")
print("")
print("A entrada será primeiramente uma grade de tamanho '8 x 8', representando o tabuleiro de xadrez. Cada uma das '8' linhas do tabuleiro possuirá '8' inteiros 'Q' (0 <= Q <= 2), separados por espaço. Portanto, cada posição do tabuleiro possuirá 3 valores possíveis: 0 – para indicar que naquela posição não tem peça; 1 – para indicar uma peça aliada; 2 – para indicar que naquela posição há uma peça inimiga. Por fim, serão dados dois inteiros 'X' e 'Y' (0 <= X, Y <= 7), representando a coordenada inicial da torre, sendo que 'X' representa uma linha e 'Y' representa uma coluna. Além disso, na posição X – Y terá o valor 1, pois representa a própria torre.")
print("")
print("Você deverá imprimir a quantidade de peças inimigas no caminho da torre.")
print("----------------------")
print("")

grid = []
enemyCount = 0
visible = False

for i in range(8):
    entry = input().split()
    grid.append(entry)

X, Y = input().split()

X = int(X); Y = int(Y)

# vvvv debug autoset vvvv
# grid= [['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['2', '0', '1', '1', '2', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '2', '0', '0', '0', '0', '0'], ['0', '0', '2', '0', '0', '0', '0', '0']]
# X = int(2); Y = int(2)

for j in range(8):
    for k in range(8):
        # check every row and column individually
        if j == X:
            if grid[j][k] == "2":
                if k == 7: break
                # find enemy, check for LoS horizontally
                row = k+1
                for l in range(8):
                    if l == 7: break
                    if row == 8: break
                    if grid[j][row] == "1":
                        if (row-1) == Y:
                            visible = True
                        else: visible = False
                    elif grid[j][row] == "2":
                        visible = False
                    if visible == True:
                        break
                    else: 
                        row += 1        
            if visible == True:
                enemyCount += 1
                visible = False
            
        if k == Y:
            if grid[j][k] == "2":
                if j == 0: break
                # find enemy, check for LoS vertically
                column = j-1
                for n in range(8):
                    if grid[column][k] == "1":
                        if (column) == X:
                            visible = True
                        else:
                            visible = False
                    elif grid [column][k] == "2":
                        visible = False
                        break
                    if visible == True:
                        break
                    else: 
                        column -= 1
                        if column == 0: break
            if visible == True:
                enemyCount += 1
                visible = False
print (enemyCount)