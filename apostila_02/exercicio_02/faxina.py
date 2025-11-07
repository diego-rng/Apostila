print("----------------")
print("     Faxina     ")
print("----------------")
print("")
print("A primeira linha da entrada contém dois inteiros N e T, respectivamente o número de livros na estante e o número máximo de consoantes permitidas no título de cada livro. As próximas N linhas contêm os títulos dos livros, que tem no máximo 20 símbolos. Estes são apenas letras minúsculas e espaços.")
print("")
print("Para cada livro, seu programa deve imprimir 0 caso o livro deva ser doado e 1 caso ele fique na estante, seguidos de um fim de linha.")
print("----------------")
print("")

N, T = input("Insira o número de livros perimitidos e o número de consoantes, respectivamente: ").split()
N = int(N); T = int(T)
estante = []
consonants= set("bcdfghjklmnpqrstvwxyz")

for num in range(N):
    books = str(input())
    estante.append(books)

for j in range(N):
    count = 0
    count = sum(1 for c in estante[j] if c in consonants)
    if count > T:
        print("0\n")
    else:
        print("1\n")