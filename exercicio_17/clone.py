print("----------------------------")
print("     Clones das Sombras     ")
print("----------------------------")
print("")
print("A primeira linha da entrada consiste de um inteiro 'N' (1 <= N <= 5000), que representa a quantidade de ninjas inimigos.")
print("")
print("A saída consiste em uma linha contendo 'Dattebayo', caso seja possível ter o número de narutos exatamente igual ao número de inimigos, ou 'Tururuuu', caso não seja possível.")
print("----------------------------")
print("")

while True: 
    N = int(input("Quantos ninjas foram avistados? "))
    print("")
    if 1 <= N <= 5000:
        break
    else:
        print("Insira um número válido!")
        print("")

if N == 1:
    print("Dattebayo")
    exit()
clone = 1    
while True:
    clone = (clone * 2)
    if clone >= N:
        break
    else: 
        continue

if clone == N:
    print("Dattebayo")
else: 
    print("Tururuuu")
    
    
    