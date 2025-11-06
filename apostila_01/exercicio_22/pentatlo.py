print("------------------")
print("     Pentatlo     ")
print("------------------")
print("")
print("Serão dados em uma única linha o número inteiro 'X' de inscrição do candidato (1 <= X <= 1000), seguido de mais 5 notas inteiras N1, N2, N3, N4 e N5 (0 <= N1, N2, N3, N4, N5 <= 10), relativas ao Tiro ao alvo, Natação, Esgrima, Hipismo e Corrida.")
print("")
print("A saída deve imprimir o número de inscrição do atleta seguido de sua média final com uma casa decimal de precisão.")
print("------------------")
print("")

while True:
    X, N1, N2, N3, N4, N5 = input("Insira o número de inscrição do candidato, seguido pelas notas do mesmo: ").split()
    print("")
    X = int(X)
    N1 = int(N1)
    N2 = int(N2)
    N3 = int(N3)
    N4 = int(N4)
    N5 = int(N5)
    if 1 <= X <= 1000 and 0 <= N1 <= 10 and 0 <= N2 <= 10 and 0 <= N3 <= 10 and 0 <= N4 <= 10 and 0 <= N5 <= 10:
        break
    else: 
        print("Insira números válidos!")
        print("")
        continue

med = float((N1 + N2 + N3 + N4 + N5) / 5)

print(f"A média do candidato {X} foi de {med:.1f}")
