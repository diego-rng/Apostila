print("---------------------------------")
print("     Contabilizando Pokémons     ")
print("---------------------------------")
print("")
print("A entrada é composta de 2 linhas. A primeira linha contém três inteiros que representam o número de pokémons já registrados na Pokédex de cada região, na ordem 'K' (Kanto), 'J' (Johto) e 'H' (Hoenn). A segunda linha contém o número de novos pokémons capturados de cada região na mesma ordem da primeira linha.")
print("")
print("Imprima, na ordem da entrada (K J H), o número total de pokémons de cada região após a nova contagem, separados por espaço. Imprima uma quebra de linha no fim.")
print("---------------------------------")
print("")

while True:
    K, J, H = input("Insira o número de pokémons nas regiões Kanto, Johto e Hoenn respectivamente: ").split()
    print("")
    K = int(K)
    J = int(J)
    H = int(H)
    valid = 0 <= K <= 100, 0 <= J <= 100, 0 <= H <= 100
    if valid: 
        break
    else: 
        print("Insira números corretos.")
        print("")
        continue

while True:
    Kn, Jn, Hn = input("Insira o número de pokémons capturados nas regiões Kanto, Johto e Hoenn respectivamente: ").split()
    print("")
    Kn = int(Kn)
    Jn = int(Jn)
    Hn = int(Hn)
    valid = 0 <= Kn <= 100, 0 <= Jn <= 100, 0 <= Hn <= 100
    if valid: 
        break
    else: 
        print("Insira números corretos.")
        print("")

nK = int(K + Kn)
nJ = int(J + Jn)
nH = int(H + Hn)

print(f"Kanto tinha {K} pokémons registrados, agora tem {nK}.")
print(f"Johto tinha {J} pokémons registrados, agora tem {nJ}.")
print(f"Hoenn tinha {H} pokémons registrados, agora tem {nH}.\n")

