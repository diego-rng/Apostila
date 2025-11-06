print("-------------------------------")
print("     Energia de Aceleração     ")
print("-------------------------------")
print("")
print("A entrada consiste em dois valores inteiros positivos correspondentes à massa (o peso) atual do Flash em quilos (40 ≤ P ≤ 100) e a velocidade em que o Flash está correndo em determinado momento, em metros por segundo (0 ≤ V ≤ 300.000.000).")
print("")
print("A saída corresponde a um inteiro que é a energia necessária para o Flash chegar a essa velocidade considerando as limitações descritas pela teoria da relatividade (Energia = Massa x Velocidade²).")
print("-------------------------------")
print("")

while True:
    M, V = input("Insira o peso atual do Flash e a Velocidade em que ele está correndo nesse momento: ").split()
    print("")
    M = int(M)
    V = int(V)    
    if 40 <= M <= 100 and 0 <= V <= 300000000:
        break
    else:
        print("Insira números válidos!")
        print("")
        continue

ener = int(M * (V**2))

print(f"Flash precisa de {ener} Joules em Energia Cinética para correr nessa velocidade.")