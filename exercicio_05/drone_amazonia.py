print("---------------------------")
print("     Drone da Amazônia     ")
print("---------------------------")
print("")
print("A primeira linha da entrada consiste de dois inteiros, X1 e Y1, que correspondem às coordenadas para a entrega. A segunda linha consiste de dois inteiros, X2 e Y2, correspondentes às coordenadas atuais do drone. Saiba que 1 <= X1, Y1, X2, Y2 <= 1000.")
print("")
print("Seu programa deve imprimir em uma única linha “Soltar pacote” (sem aspas), caso as coordenadas da entrega e do drone sejam iguais, ou “Nao soltar pacote” (sem aspas e sem til), caso as coordenadas sejam diferentes.")
print("---------------------------")


while True:
    x1, y1 = input("Qual são as coordenadas atuais do drone? ").split()
    x1 = int(x1)
    y1 = int(y1)
    print("")
    if 1 >= x1 >= 1000:
        print("Coordenadas inválidas! A primeira coordenada deve ser um número inteiro entre 1 e 1000.")
        print("")
        continue
    elif 1 >= y1 >= 1000:
        print("Coordenadas inválidas! A segunda coordenada deve ser um número inteiro entre 1 e 1000.")
        print("")
        continue
    else: 
        break

while True:
    x2, y2 = input("Quais são as coordenadas de entrega? ").split()
    x2 = int(x2)
    y2 = int(y2)
    print("")
    if 1 >= x2 >= 1000:
        print ("Coordenadas inválidas! A primeira coordenada deve ser um número inteiro entre 1 e 1000.")
        print("")
        continue
    elif 1 >= y2 >= 1000:
        print ("Coordenadas inválidas! A segunda coordenada deve ser um número inteiro entre 1 e 1000.")
        print("")
        continue
    else: 
        break

if x1 == x2 and y1 == y2:
    print("Soltar pacote")
else:
    print("Nao soltar pacote")
    