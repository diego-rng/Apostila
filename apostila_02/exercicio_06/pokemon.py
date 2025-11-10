print("--------------------------")
print("     Caçando Pokémons     ")
print("--------------------------")
print("")
print("Na primeira linha serão dados dois inteiros 'N' e 'M' (1 <= N, M <= 100) que diz a quantidade de linhas e colunas da matriz, respectivamente. As próximas 'N' linhas terão 'M' inteiros 'T' (0 <= T <= 100) em cada, representando o tipo do pokémon ou se não há pokémon. Por fim, na última linha, será dado um inteiro 'P' (1 <= P <= 100), representando o tipo do pokémon a ser pego por Ash.")
print("")
print("A saída consiste em 1 linha contendo a frase 'Ash pegou 'Q' pokemon' onde 'Q' deve ser a quantidade de pokémons do tipo 'P' pegos por Ash, podendo ser inclusive 0 (zero).")
print("--------------------------")
print("")

N, M = input("Insira o tamanho da área: ").split()
N = int(N); M = int(M)
pokeTypes = []

for i in range(N):
    T = [int(i)for i in input().split()]
    pokeTypes.append(T)

P = int(input())
Q = 0

for j in range(N):
    for k in range(M):
        if pokeTypes[j][k] == P:
            Q += 1

print(f"Ash pegou {Q} pokemon")
