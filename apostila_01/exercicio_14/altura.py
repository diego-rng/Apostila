print("----------------")
print("     Altura     ")
print("----------------")
print("")
print("A entrada é composta por três números inteiros diferentes, A, B e C, a altura de cada um dos amigos (em centímetros) respectivamente, separados por um espaço em branco.")
print("")
print("Você deve imprimir em uma única linha a altura do maior dos três amigos.")
print("----------------")
print("")

while True:
    A, B, C = input("Insira a altura dos 3 amigos. ").split()
    A = int(A)
    B = int(B)
    C = int(C)
    print("")
    if 100 <= A <= 200 and 100 <= B <= 200 and 100 <= C <= 200:
        break
    else: 
        print("Insira números válidos!")
        print("")

if A >= B and A >= C:
    print(A)
elif B >= A and B >= C:
    print(B)
else: print (C)