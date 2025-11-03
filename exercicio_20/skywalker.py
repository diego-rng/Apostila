print("-------------------------")
print("     Ajude Skywalker     ")
print("-------------------------")
print("")
print("A entrada é composta por cinco inteiros, 'A', 'B', 'C', 'D' e 'E', representando respectivamente, o total de naves sondadas no quadrante, o total de naves amigas detectadas a frente de Skywalker, o total de naves amigas a direita, o total de naves amigas a esquerda e o total de naves amigas atrás da nave de Skywalker. Saiba que 0 <= A, B, C, D, E <= 1000 e que (B + C + D + E) <= A.")
print("")
print("A saída será composta por apenas um número inteiro, ou seja, o total de naves inimigas no quadrante em que Skywalker se encontra.")
print("-------------------------")
print("")

while True:
    A, B, C, D, E = input("Insira, respectivamente, o número de naves sondadas no quandrante, e o número de naves aliadas detectadas à frente, à direita, à esquerda e atrás da nave de Skywalker: ").split()
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    E = int(E)
    print("")
    validCheck = (B + C + D + E) <= A
    if 0 <= A <= 1000 and 0 <= B <= 1000 and 0 <= C <= 1000 and 0 <= D <= 1000 and 0 <= E <= 1000 and validCheck:
        break
    else: 
        print("Essas leituras não fazem sentido!")
        continue

enemyCheck = (A - (B + C + D + E))

print(f"Há {enemyCheck} inimigos na área")
