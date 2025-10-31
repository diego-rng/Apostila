print("---------------------------------")
print("     Ajude o pequeno Kurumin     ")
print("---------------------------------")
print("")
print("Na primeira linha há um inteiro 'N' (1 <= N <= 20) que representa a quantidade de gaiolas. Em cada uma das próximas 'N' linhas serão dados 4 inteiros 'A', 'B', 'C', 'D' (-20 <= A, B, C, D <= 50), representando os números nos lados de cada gaiola.")
print("")
print("No final do teste, Kurumin deverá informar a soma 'S' de todos os resultados de cada gaiola. Segundo o curandeiro da tribo, isso representará a quantidade de anos que Kurumin viverá entre eles. Portanto, imprima somente a frase 'S anos de vida'")
print("--------------------")
print("")

while True:
    N = int(input("Insira a quantidade de gaiolas: "))
    print("")
    if 1 <= N <= 20:
        break
    else: 
        print("Insira uma quantidade correta!")
        print("")

cageTotal = []
num = 0

while True:
    A, B, C, D = input("Insira os números escritos em cada gaiola: ").split()
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    if -20 <= A <= 50 and -20 <= B <= 50 and -20 <= C <= 50 and -20 <= D <= 50:
        sum1 = (A + B + C + D)
        if sum1 < 100:
            num = num + 1
        else: 
            num = num + 1
            sum1 = (A - B - C - D)
        
        cageTotal.append(sum1)
    else: 
        print("Insira números válidos!")
        print("")
        continue

    if num == N:
        break
    

finalNum = sum(cageTotal)

print(f"{finalNum} anos de vida.")